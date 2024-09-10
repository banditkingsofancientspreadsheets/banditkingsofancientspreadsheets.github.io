---
title: 'A SQL to Julia DataFrames Cheatsheet'
date: 2022-03-27
categories: [julia, modeling]
description: 'What would common SQL expressions look like in Julia DataFrames and Julia DataFramesMeta?'
aliases:
  - /SQL-to-Julia
canonicalUrl: https://www.nelsontang.com/blog/2022-03-27-sql-to-julia
---

A SQL to Julia DataFrames dictionary using DataFrames and DataFramesMeta. In general, I use DataFramesMeta since it abstracts away some lower level nuance and it makes for a tidier workflow when I'm constructing queries.

# Overview

## Querying in `DataFrames` and `DataFramesMeta`

| SQL Clause                                             | DataFrames Equivalent                                           | DataFramesMeta Equivalent                                                                                                         |
| ------------------------------------------------------ | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `SELECT`                                               | `select`                                                        | `@select`                                                                                                                         |
| `WHERE`                                                | `subset(df, :colnm => ByRow(x -> x>1))`                         | `@rsubset(df, :colnm > 1)`                                                                                                        |
| `LIKE`                                                 | `subset(df, :colnm=>ByRow(x -> occursin(r"string", x)))`        | `@rsubset(df, occursin(r"string", :colnm))`                                                                                       |
| `GROUP BY`                                             | `gd = groupby(df, :colnm)`<br></br>`combine(gd, :colnm=>sum)`   | `gd = groupby(df, :colnm)`<br></br>`@combine(gd, :newcol=sum(:colnm))`<br></br>or<br></br> `@by(df, :colnm, :newcol=sum(:colnm))` |
| `SUM(colnm) OVER (PARTITION BY other_colnm) AS newcol` | `gd = groupby(df, :colnm)`<br></br>`transform(gd, :colnm=>sum)` | `gd = groupby(df, :colnm)`<br></br>`@transform(gd, :newcol=sum(:colnm))`                                                          |
| `ORDER BY colnm ASC`                                   | `sort(df, :colnm)`                                              | `@orderby(df, :colnm)`                                                                                                            |
| `ORDER BY colnm DESC`                                  | `sort(df, :colnm, rev=true)`                                    | `@orderby(df, sort(:colnm, rev=true)`                                                                                             |

## Joins

| SQL Clause                                                                 | DataFrames Equivalent                                                            |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `INNER JOIN`                                                               | `innerjoin(df, df2, on=:colnm)`<br></br>`innerjoin(df, df2, on=[:left=>:right])` |
| `LEFT JOIN`                                                                | `leftjoin(df, df2, on=:colnm)`<br></br>`leftjoin(df, df2, on=[:left=>:right])`   |
| `RIGHT JOIN`                                                               | `rightjoin(df, df2, on=:colnm)`<br></br>`rightjoin(df, df2, on=[:left=>:right])` |
| `OUTER JOIN`                                                               | `outerjoin(df, df2, on=:colnm)`<br></br>`outerjoin(df, df2, on=[:left=>:right])` |
| `SELECT * FROM table1, table2` <br></br>aka cartesian product or crossjoin | `crossjoin`                                                                      |

# A Worked Example

## The Dataset

We'll manually create a dataset of employees `df`:

```julia
using CSV, DataFramesMeta, Statistics, Dates

# DataFrame(column=data)
df = DataFrame(id=1:8,
               first_name=["Michael", "Dwight", "Angela", "Jim", "Pam", "Oscar", "Meredith", "Creed"],
               last_name=["Scott", "Schrute", "Martin", "Halpert", "Beesly", "Nunez", "Palmer", "Bratton"],
               department=["Management & Admin", "Sales", "Accounting", "Sales", "Management & Admin", "Accounting",
                           "Purchasing", "Purchasing"],
               salary=[5100, 4200, 3750, 4300, 2200, 3400, 3300, 3200])

8×5 DataFrame
 Row │ id     first_name  last_name  department          salary
     │ Int64  String      String     String              Int64
─────┼──────────────────────────────────────────────────────────
   1 │     1  Michael     Scott      Management & Admin    5100
   2 │     2  Dwight      Schrute    Sales                 4200
   3 │     3  Angela      Martin     Accounting            3750
   4 │     4  Jim         Halpert    Sales                 4300
   5 │     5  Pam         Beesly     Management & Admin    2200
   6 │     6  Oscar       Nunez      Accounting            3400
   7 │     7  Meredith    Palmer     Purchasing            3300
   8 │     8  Creed       Bratton    Purchasing            3200
```

Let's create a sales database called `db_sales` with client information (thanks to [this site](https://theoffice.fandom.com/wiki/Clients_of_Dunder_Mifflin))

```julia
# Parse dates as Date objects
dates = ["1-2-2006", "1-29-2006", "2-1-2006", "2-14-2006", "3-1-2006", "3-20-2006"]
dates = parse.(Date, dates, dateformat"m-d-y")

db_sales = DataFrame(id=1:6,
                     transaction_date=dates,
                     employee_id=[4, 2, 4, 2, 4, 2],
                     quantity=[100, 500, 600, 200, 400, 250],
                     customer=["Dunmore High School", "Harper Collins", "Blue Cross of Pennsylvania",
                                "Apex Technology", "Blue Cross of Pennsylvania",
                                "Stone, Cooper, and Grandy: Attorneys at Law"])

6×5 DataFrame
 Row │ id     transaction_date  employee_id  quantity  customer
     │ Int64  Date              Int64        Int64     String
─────┼───────────────────────────────────────────────────────────────────────────────────
   1 │     1  2006-01-02                  4       100  Dunmore High School
   2 │     2  2006-01-29                  2       500  Harper Collins
   3 │     3  2006-02-01                  4       600  Blue Cross of Pennsylvania
   4 │     4  2006-02-14                  2       200  Apex Technology
   5 │     5  2006-03-01                  4       400  Blue Cross of Pennsylvania
   6 │     6  2006-03-20                  2       250  Stone, Cooper, and Grandy: Attor…
```

## Subsetting Rows

Subsetting rows is possible in base `DataFrames`, but the syntax in `DataFramesMeta` is easier for beginners to follow. The special `@rsubset` macro saves on having to write anonymous functions so it's one less syntactical thing to keep typing every time.

```julia
#DataFrames
subset(df, :department => ByRow(x -> occursin("Admin", x)))

#DataFramesMeta
@rsubset(df, occursin("Admin", :department))

2×5 DataFrame
 Row │ id     first_name  last_name  department          salary
     │ Int64  String      String     String              Int64
─────┼──────────────────────────────────────────────────────────
   1 │     1  Michael     Scott      Management & Admin    5100
   2 │     5  Pam         Beesly     Management & Admin    2200
```

### Matching Text

What if you want to do some string matching with wildcards, i.e. SQL `WHERE` clause with the `LIKE` or `%` operator?

We can use the `occursin()` function and pass it as an argument to `@rsubset`, like:

```julia
#DataFrames
subset(df, :department => ByRow(x -> occursin("Admin", x)))

#DataFramesMeta
@rsubset(df, occursin("Admin", :department))

2×5 DataFrame
 Row │ id     first_name  last_name  department          salary
     │ Int64  String      String     String              Int64
─────┼──────────────────────────────────────────────────────────
   1 │     1  Michael     Scott      Management & Admin    5100
   2 │     5  Pam         Beesly     Management & Admin    2200
```

Adding the `r` in front of the string lets you use regex to use wildcards and more complex string matching criteria.

## Aggregation

i.e. `GROUP BY Column` and `SUM(column)`

For regular `GROUP BY` you first use `groupby()` and then either `combine` or `@combine`, or you can use the `@by` function as shorthand.

### Grouping with `@by`

```julia
@by(df, :department,
        :"Average Salary" = mean(:salary),
        :count=length(:salary))

4×2 DataFrame
 Row │ department          Average Salary
     │ String              Float64
─────┼────────────────────────────────────
   1 │ Management & Admin          3650.0
   2 │ Sales                       4250.0
   3 │ Accounting                  3575.0
   4 │ Purchasing                  3250.0
```

### Grouping with `combine` and `@combine`

```julia
gd = groupby(df, :department)
#DataFrames
combine(gd, :salary => mean => :"Average Salary",
            :department => length => :count)

#DataFramesMeta
@combine(gd, :"Average Salary" = mean(:salary),
             :count = length(:department))

4×2 DataFrame
 Row │ department          Average Salary
     │ String              Float64
─────┼────────────────────────────────────
   1 │ Management & Admin          3650.0
   2 │ Sales                       4250.0
   3 │ Accounting                  3575.0
   4 │ Purchasing                  3250.0
```

## Window Functions with `@transform`

In SQL:

```sql
AVG(colnm) OVER (PARTITION BY other_colnm) AS newcol
```

i.e. the `PARTITION BY` clause, similar to groupby but it returns a value for each row in your table after doing the aggregations in each partition.

In Julia, you can use the `@transform` macro to do this after grouping.

```julia
# Example: add a column that
gd = groupby(df, :department)
#DataFrames
transform(gd, :salary => mean => :"avg_dept_salary")

#DataFramesMeta
@transform(gd, :"avg_dept_salary"=mean(:salary))

8×6 DataFrame
 Row │ id     first_name  last_name  department          salary  avg_dept_salary
     │ Int64  String      String     String              Int64   Float64
─────┼──────────────────────────────────────────────────────────────────────────
   1 │     1  Michael     Scott      Management & Admin    5100          3650.0
   2 │     2  Dwight      Schrute    Sales                 4200          4250.0
   3 │     3  Angela      Martin     Accounting            3750          3575.0
   4 │     4  Jim         Halpert    Sales                 4300          4250.0
   5 │     5  Pam         Beesly     Management & Admin    2200          3650.0
   6 │     6  Oscar       Nunez      Accounting            3400          3575.0
   7 │     7  Meredith    Palmer     Purchasing            3300          3250.0
   8 │     8  Creed       Bratton    Purchasing            3200          3250.0
```

And we see indeed that we have the same number of rows as the initial dataset.

## Putting together a query with `@chain`

```julia
sales = @chain db_sales begin
    groupby(:employee_id)
    @combine(:total_quantity=sum(:quantity),
             :number_of_customers=length(:customer))
end

result = @chain df begin
                @select(:id, :first_name, :last_name, :department)
                @rsubset(:department=="Sales")
                leftjoin(sales, on=[:id=>:employee_id])
                @orderby(sort(:total_quantity, rev=true))  # descending
          end

2×6 DataFrame
 Row │ id     first_name  last_name  department  total_quantity  number_of_customers
     │ Int64  String      String     String      Int64?          Int64?
─────┼───────────────────────────────────────────────────────────────────────────────
   1 │     4  Jim         Halpert    Sales                 1100                    3
   2 │     2  Dwight      Schrute    Sales                  950                    3
```

# Alternative: Use DuckDB

Another amazing alternative is to use [`DuckDB`](https://duckdb.org/docs/api/julia) to query dataframes, CSV files, parquet files, etc directly with SQL.

Assuming we had the dataframes created above, we'd query it with SQL with a few lines:

```julia
using DuckDB

# create a new in-memory dabase
con = DBInterface.connect(DuckDB.DB)

# register it as a view in the database
DuckDB.register_data_frame(con, df, "my_df")

queryStr = """
SELECT
first_name
, last_name
, department
, salary
, AVG(salary) OVER (PARTITION BY department) AS avg_dept_salary
FROM my_df
"""

# run a SQL query over the DataFrame
results = DBInterface.execute(con, queryStr)
print(results)

# 8×5 DataFrame
#  Row │ first_name  last_name  department          salary  avg_dept_salary
#      │ String?     String?    String?             Int64?  Float64?
# ─────┼────────────────────────────────────────────────────────────────────
#    1 │ Angela      Martin     Accounting            3750           3575.0
#    2 │ Oscar       Nunez      Accounting            3400           3575.0
#    3 │ Michael     Scott      Management & Admin    5100           3650.0
#    4 │ Pam         Beesly     Management & Admin    2200           3650.0
#    5 │ Meredith    Palmer     Purchasing            3300           3250.0
#    6 │ Creed       Bratton    Purchasing            3200           3250.0
#    7 │ Dwight      Schrute    Sales                 4200           4250.0
#    8 │ Jim         Halpert    Sales                 4300           4250.0
```
