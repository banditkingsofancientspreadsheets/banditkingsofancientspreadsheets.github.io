---
title: "Python Pandas - Merging With Wildcards and Conditions"
date: 2021-11-25
tags: [python]
categories: [modeling]
summary: "Merging two dataframes with pandas but only if certain conditions are true."
aliases:
    - /pandas-conditional-merging
---
*Updated 28 Jan 2022 to use a newer pandas crossjoin method with `.merge(how='cross')`, which works on pandas versions >1.2*

What happens when you want to merge (join) two dataframes together, but only if certain conditions are true? This is easy to do when you are simply looking for matching key-value pairs in two tables, but I had a real life scenario where I had complex combinations of joins to consider.

## The Challenge

Here's a simplified version of the issue I was facing:

1. The date in the left table was between two dates (a start and end date) in the second table
2. ...AND the values in two other columns matched each other, OR the column on the right table was equal to 'ANY' (aka a 'wildcard' value)

For a concrete example, let's say you're working for an apparel retailer, and you offer limited-time promotions where the customer can apply for a rebate if they buy a certain brand of jacket during the promotion period. The wrinkle: you also offer a global discount across ANY brand of jacket bought in a separate promotion.

You have a table of sales volume and you're trying to map that data with a table of promotions that you're offering:


### `sales_volume_table`

| date       | quantity |  brand  
| ---        | ---      |  ---
| 2021-11-15 | 1        |  Outdoor
| 2021-11-20 | 2        |  Leisure
| 2021-11-25 | 3        |  Athletic
| 2021-11-26 | 2        |  Outdoor

### `promos_table`

| start_date    | end_date      | brand          | rebate_per_unit |
| ---           | ---           | ---            | ---            |
| 2021-11-01    | 2021-11-25    | ANY            | 3            |
| 2021-11-25    | 2021-11-26    | Outdoor        | 5            |
| 2021-12-29    | 2021-12-30    | Leisure        | 10           |

You can't do a simple left join because of the 'ANY' option on the right table. One way of dealing with this is modifying the data in `promos_table` so that it covers all possible `brand` categories (i.e. Outdoor, Leisure, Athletic) but for the sake of argument let's imagine that's not feasible in the real-world example.

## Merge Everything You Think You'll Need and Sort it Out Later

The simplest thing I found is to merge everything you think you'll need and then filter it out later. I tried dictionaries and set logic, but couldn't find anything faster than doing the big join.

Specifically, you can do a *Cartesian Product* (aka a Cross Join), and [here's a great example from StackOverflow](https://stackoverflow.com/questions/47472207/how-to-merge-with-wildcard-pandas) when faced with having to merge two pandas dataframes with a wildcard value. I'll walk through each step below using the StackOverflow example and our sample scenario:

```python
import pandas as pd

# Create our two dataframes
sales_volume_table = pd.DataFrame.from_dict([
    {'date':'2021-11-15', 'quantity':1, 'brand':'Outdoor'},
    {'date':'2021-11-20', 'quantity':2, 'brand':'Leisure'},
    {'date':'2021-11-25', 'quantity':3, 'brand':'Athletic'},
    {'date':'2021-11-26', 'quantity':2, 'brand':'Outdoor'},    
])

promos_table = pd.DataFrame.from_dict([
    {'start_date':'2021-11-01', 'end_date':'2021-11-25', 'brand':'ANY', 'rebate_per_unit':3},
    {'start_date':'2021-11-25', 'end_date':'2021-11-26', 'brand':'Outdoor', 'rebate_per_unit':5},
])

# Create a column to join on and save the results with a Cartesian Product
results = sales_volume_table.merge(promos_table, how='cross')
```

The Cartesian Product matches every row in the right dataframe with every row in the left dataframe. Here's the output below:

| date       |   quantity | brand_x   | start_date   | end_date   | brand_y   |   rebate_per_unit |
|:-----------|-----------:|:----------|:-------------|:-----------|:----------|------------------:|
| 2021-11-15 |          1 | Outdoor   | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-15 |          1 | Outdoor   | 2021-11-25   | 2021-11-26 | Outdoor   |                 5 |
| 2021-11-20 |          2 | Leisure   | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-20 |          2 | Leisure   | 2021-11-25   | 2021-11-26 | Outdoor   |                 5 |
| 2021-11-25 |          3 | Athletic  | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-25 |          3 | Athletic  | 2021-11-25   | 2021-11-26 | Outdoor   |                 5 |
| 2021-11-26 |          2 | Outdoor   | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-26 |          2 | Outdoor   | 2021-11-25   | 2021-11-26 | Outdoor   |                 5 |

And then once the results are joined together in this way, you can then apply all of your conditions using pandas indexing. I like using the `query` method since it's a little easier to read.

```python
# Filter the results where the two columns match, OR the right column is 'ANY'
results = results.query("brand_x == brand_y | brand_y=='ANY'")
```

| date       |   quantity | brand_x   | start_date   | end_date   | brand_y   |   rebate_per_unit |
|:-----------|-----------:|:----------|:-------------|:-----------|:----------|------------------:|
| 2021-11-15 |          1 | Outdoor   | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-15 |          1 | Outdoor   | 2021-11-25   | 2021-11-26 | Outdoor   |                 5 |
| 2021-11-20 |          2 | Leisure   | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-25 |          3 | Athletic  | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-26 |          2 | Outdoor   | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-26 |          2 | Outdoor   | 2021-11-25   | 2021-11-26 | Outdoor   |                 5 |

But we're not done yet - we still need to filter out the dates that are relevant, so we edit our above query to incorporate additional conditions, and do a little cleanup:

```python
# Instead of one long string, we can break up the query into multiple parts
condition1 = "(brand_x == brand_y | brand_y=='ANY')"
condition2 = "(start_date <= date <= end_date)"
qry = condition1 + " & " + condition2
results = results.query(qry)
```

Which gives us our result (skipping the part where you drop some columns for clarity)

| date       |   quantity | brand_x   | start_date   | end_date   | brand_y   |   rebate_per_unit |
|:-----------|-----------:|:----------|:-------------|:-----------|:----------|------------------:|
| 2021-11-15 |          1 | Outdoor   | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-20 |          2 | Leisure   | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-25 |          3 | Athletic  | 2021-11-01   | 2021-11-25 | ANY       |                 3 |
| 2021-11-26 |          2 | Outdoor   | 2021-11-25   | 2021-11-26 | Outdoor   |                 5 |

## Performance

Since we had $4$ rows in the left dataframe and $2$ in the right, the result of the Cartesian Product is $4 \times 2$ or $8$ rows long. Something to keep in mind if your datasets get large. So if you had 5K rows of sales data and 1K rows of promotions, you'd end up with 5M rows of data after this join.

But you don't need to do a full Cartesian Product here, the key idea is to get the superset of all the data that would be relevant and then filter it down. In my real-world case I had 55k rows and 15k rows of promotions, and I had about 12 different conditions to check (a mix of date and wildcards). I started with nested for-loops, dictionaries, and set logic and it took about 30s on my 2018 MBP, but with some smarter filtering and joining with this method I was able to get the same operation done in <10s.

## SQL Is Faster

But instead of doing this in Pandas, it turns out this is trivial to do in SQL. To do a Cartesian Product of the two dataframes in SQL is simply:

```sql
SELECT *
FROM sales_volume, promos
```

And it's even simpler to do your filtering with a `WHERE` clause, making the entire statement:

```sql
SELECT * 
FROM sales_volume, promos 
WHERE (sales_volume.brand=promos.brand or promos.brand='ANY')
AND (start_date <= date AND date <= end_date)
```

On my computer the pandas merging and filtering took about 4.7 ms while the sql query took 700 µs, so a little under 7x improvement in performance.

## Key Takeaway

The bottom line to take away from this is to solve a problem when you want to conditionally join two dataframes and handle things like wildcards, the easiest thing to do is to big join and filter it down from there. Or use SQL instead of Pandas.

### Final Python/Pandas Result:

```python
import pandas as pd

# Create our DataFrames
sales_volume_table = pd.DataFrame.from_dict([
    {'date':'2021-11-15', 'quantity':1, 'brand':'Outdoor'},
    {'date':'2021-11-20', 'quantity':2, 'brand':'Leisure'},
    {'date':'2021-11-25', 'quantity':3, 'brand':'Athletic'},
    {'date':'2021-11-26', 'quantity':2, 'brand':'Outdoor'},    
])

promos_table = pd.DataFrame.from_dict([
    {'start_date':'2021-11-01', 'end_date':'2021-11-25', 'brand':'ANY', 'rebate_per_unit':3},
    {'start_date':'2021-11-25', 'end_date':'2021-11-26', 'brand':'Outdoor', 'rebate_per_unit':5},
])

# Merge it all
results = sales_volume_table.merge(promos_table, how='cross') # notice you don't need to set a join key!
# And Filter it Down
results = results.query("(brand_x == brand_y | brand_y=='ANY') & start_date <= date <= end_date")
```

### Same Thing, but Faster with SQL and SQLite

```python
import pandas as pd
import sqlite3

# Create our dataframes as before
sales_volume_table = pd.DataFrame.from_dict([
    {'date':'2021-11-15', 'quantity':1, 'brand':'Outdoor'},
    {'date':'2021-11-20', 'quantity':2, 'brand':'Leisure'},
    {'date':'2021-11-25', 'quantity':3, 'brand':'Athletic'},
    {'date':'2021-11-26', 'quantity':2, 'brand':'Outdoor'},    
])

promos_table = pd.DataFrame.from_dict([
    {'start_date':'2021-11-01', 'end_date':'2021-11-25', 'brand':'ANY', 'rebate_per_unit':3},
    {'start_date':'2021-11-25', 'end_date':'2021-11-26', 'brand':'Outdoor', 'rebate_per_unit':5},
])

# Create a SQL connection to our SQLite database
con = sqlite3.connect("sales.db")

# Add dataframes as tables in this database
sales_volume_table.to_sql("sales_volume", con, index=False, if_exists='replace')
promos_table.to_sql("promos", con, index=False, if_exists='replace')

# Results in a 5x speedup from pandas!
sql = """SELECT * 
FROM sales_volume, promos 
WHERE (sales_volume.brand=promos.brand or promos.brand='ANY')
AND (start_date <= date AND date <= end_date)"""

pd.read_sql_query(sql, con)
```