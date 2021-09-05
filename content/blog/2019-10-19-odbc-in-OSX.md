---
title: "How to set up ODBC in Mac OS to connect to MS SQL Server for use with Python and R"
date: 2019-10-19
tags: [r, python, workflow]
categories: [workflow]
summary: "My local data mart runs on MS SQL Server, and I want to pull data directly into R or Python for data analysis. This is **really** easy on Windows with its' built-in ODBC manager, but I spent a weekend figuring out how to do this after switching to OSX. A lot of documentation out there is old (from 2012), so I decided to make this for anyone still looking for an answer in 2019."
mathjax: "true"
---

My local data mart runs on MS SQL Server, and I want to pull data directly into R or Python for data analysis. This is **really** easy on Windows with its' built-in ODBC manager, but I spent a weekend figuring out how to do this after switching to OSX. A lot of documentation out there is old (from 2012), so I decided to make this for anyone still looking for an answer in 2019.

* Microsoft Open Database Connectivity (ODBC) Docs: [link](https://docs.microsoft.com/en-us/sql/odbc/reference/what-is-odbc?view=sql-server-ver15)

Below are my notes for a quickstart setup for getting your MacOS (OSX) machine set up to connect to a Microsoft SQL Server via ODBC for use with R's ODBC library and Python's PyODBC library. This assumes you have [homebrew](https://brew.sh) installed to manage your packages and you have the necessary admin rights on your machine.

* Homebrew installation: [link](https://docs.brew.sh/Installation)

## 1. Install unixodbc
I like unixodbc as the ODBC manager, it just works. Install with your shell/terminal:
```console
brew install unixodbc
```
* UnixODBC docs: [link](https://docs.brew.sh/Installation)

## 2. Install FreeTDS
After getting an ODBC manager, you'll need drivers. FreeTDS works.
In your shell/terminal:
```console
brew install FreeTDS
```
* FreeTDS userguide: [link](https://www.freetds.org/userguide/)

## 3. Locate your odbc installation with odbcinst -j
After installing unixodbc as your odbc manager and freeTDS for drivers, you'll need to edit your connections in the .odbc.ini file. You can find out where this is by using the ```odbcinst -j``` command. 

In your shell/terminal:
```console
odbcinst -j

unixODBC 2.3.7
DRIVERS............: /etc/odbcinst.ini
SYSTEM DATA SOURCES: /etc/odbc.ini
FILE DATA SOURCES..: /etc/ODBCDataSources
USER DATA SOURCES..: /Users/yourname/.odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8
```
The item in ```USER DATA SOURCES..:``` is what you're looking for. Don't know why, but Python and R like to use that one first before looking elsewhere. Navigate there and edit the ```.odbc.ini``` file using your favorite text editor. Here's nano:

```console
nano /Users/yourname/.odbc.ini
```

## 4. Update the .odbc.ini file
Use your text editor and enter in the required server, port, and the Data Source Name (DSN) in brackets. We'll use the DSN to connect 

```
[my_server]
Description = my_server
TDS_Version = 7.4
Driver = /usr/local/lib/libtdsodbc.so
Server = YOUR.SERVERNAME.HERE.com
Port = 1234
```

* What is a DSN: [link](https://support.microsoft.com/en-us/help/966849/what-is-a-dsn-data-source-name)

## 5. Python to connect to your MS SQL Server with pyodbc

```python
import pandas as pd
import pyodbc

cnxn = pyodbc.connect('dsn=my_server;'
                      'Trusted_Connection=yes;')
query= "yourqueryhere"

res = pd.read_sql_query(query,cnxn)

cnxn.close()
```

## 6. R to connect to your MS SQL Server with odbc

```r
library(odbc)
con <- dbConnect(odbc::odbc(), "my_server")
res <- odbc::dbGetQuery(con, "your query here")
odbc::dbDisconnect(con)
```
