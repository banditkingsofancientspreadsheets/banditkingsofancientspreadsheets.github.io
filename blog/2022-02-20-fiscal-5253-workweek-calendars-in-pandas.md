---
title: 'Making Custom Fiscal 52/53 Workweek Calendars in Pandas'
date: 2022-02-20
tags: [python]
categories: [modeling]
summary: 'How to build custom financial calendars that have 52 or 53 workweeks in a fiscal year (aka the 4-4-5 calendar) using `pandas`'
canonicalUrl: https://www.nelsontang.com/blog/fiscal-5253-workweek-calendar-in-pandas
---

_Last run on pandas 1.1.3_

# TLDR

- Here's the [gist](https://gist.github.com/banditkings/735fe1885a442b3457d208060ac4b970)
- Notebook versions: [[ipynb]](https://github.com/banditkings/random-python-examples/blob/main/time-series-python/pandas-time-functions.ipynb)[[html]](https://github.com/banditkings/random-python-examples/blob/main/time-series-python/pandas-time-functions.ipynb)

# Fiscal Calendars Should Be Easy, Right?

Unless your company's fiscal calendar lines up exactly with the calendar year, you'll inevitably encounter issues with custom fiscal calendars. Analysts will usually have some lookup table either in a spreadsheet or a friendly database table that they're trained to query and pull in every time someone asks: _'how did we perform this quarter compared to last quarter?'_

But what about making a lookup table _programmatically_, or what if you don't have a tidy lookup table handed to you? For example, let's say you work in a paper supplier and you have a table of forecasted supply and you need to match that data to demand that each customer sent over in spreadsheets. Now imagine each customer sent you demand according to their fiscal calendar. Welcome to hell!

# Building Standard Fiscal Calendars in `pandas`

So what can you do in basic `pandas`? Well, if your fiscal calendar is the same as the calendar year, you're in luck.

`pandas` has a variety of functions that let you create and manipulate date ranges that conform to a fiscal calendar that begins on January 1st of every year and ends on Dec 31st of every year, and where every quarter is exactly 3 calendar months long.

We can see an example of this built-in functionality if we use `pandas` to give us an array of the _last_ day in each quarter in 2021 using the `freq='Q'` parameter:

```python
import datetime
import numpy as np
import pandas as pd

start = datetime.datetime(2021, 1, 1)
end = datetime.datetime(2022, 1, 1)
# Create a DatetimeIndex with freq='Q'
# the 'Q' indicates the last day of each quarter
ts = pd.date_range(start, end, freq='Q')
ts
```

Which returns an iterable `DatetimeIndex` object with a few extra parameters:

```
DatetimeIndex(['2021-03-31', '2021-06-30', '2021-09-30', '2021-12-31'], dtype='datetime64[ns]', freq='Q-DEC')
```

We can use this index to create a dataframe with columns with various attributes, by converting this stuff to a `period` object:

```python
tp = ts.to_period()

pd.DataFrame(index=ts,
             data={'quarter':tp.quarter,
                   'fiscal_year':tp.qyear})
```

|            | quarter | fiscal_year |
| :--------- | ------: | ----------: |
| 2021-03-31 |       1 |        2021 |
| 2021-06-30 |       2 |        2021 |
| 2021-09-30 |       3 |        2021 |
| 2021-12-31 |       4 |        2021 |

However, what if you wanted to use `pandas` to handle fiscal calendars that aren't set to this standard? For example, let's say we have a fiscal calendar that starts on June 1st (i.e. Nike).

Notice that the previous creation of a `pd.date_range` with `freq='Q'` created a DatetimeIndex with a freq of `'Q-DEC'`. While there's a list of ['frequency or offset aliases'](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases) there isn't much mention of what `'Q-DEC'` is except mentioned briefly in the [Pandas user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#frequency-conversion-and-resampling-with-periodindex):

> Many organizations define quarters relative to the month in which their fiscal year starts and ends. Thus, first quarter of 2011 could start in 2010 or a few months into 2011. Via anchored frequencies, pandas works for all quarterly frequencies `Q-JAN` through `Q-DEC`.

So in other words, the default quarter system `Q-DEC` (and `A-DEC`) means that it ends in December. So if we wanted to have a fiscal calendar that ends in May and starts in June 1st, we'd use `Q-MAY`:

```python
ts = pd.date_range(start, end, freq='Q-MAY')
tp = ts.to_period()

pd.DataFrame(index=ts, data={'quarter':tp.quarter, 'fiscal_year':tp.qyear})
```

|            | quarter | fiscal_year |
| :--------- | ------: | ----------: |
| 2021-02-28 |       3 |        2021 |
| 2021-05-31 |       4 |        2021 |
| 2021-08-31 |       1 |        2022 |
| 2021-11-30 |       2 |        2022 |

So that was easy! And instead of creating the date range with just the end quarters, we can create a daily date range and then use the `to_period()` call to do the fiscal year translation for us, to create a _daily_ calendar lookup table:

```python
# create a DatetimeIndex with all days between 2021 and 2022
ts = pd.date_range(start='2021', end='2022', freq='D')

# Create a PeriodIndex from the daily range with our new freq
tp = ts.to_period(freq='Q-MAY')
df = pd.DataFrame(index=ts,
                  data={'quarter':tp.quarter,
                        'fiscal_year':tp.qyear})
df.tail()
```

|            | quarter | fiscal_year |
| :--------- | ------: | ----------: |
| 2021-12-28 |       3 |        2022 |
| 2021-12-29 |       3 |        2022 |
| 2021-12-30 |       3 |        2022 |
| 2021-12-31 |       3 |        2022 |
| 2022-01-01 |       3 |        2022 |

We can see that the correct fiscal year and fiscal quarters are represented. Nice!

# 52/53 Workweek Calendars

What if your fiscal calendar follows a [52/53-workweek calendar using the 4-4-5 quarter system](https://en.wikipedia.org/wiki/4–4–5_calendar)? I want to be able to use `pandas` methods on those, too!

An exhaustive search in `pandas` docs comes up with a custom DateOffset class that has the barest minimum in terms of [documentation](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html): `pd.tseries.offsets.FY5253`.

We can use the `pd.tseries.offsets.FY5253` DateOffset type to find the dates of the beginning of each fiscal year:

```python
variation = 'last'

# create an offset for the Intel fiscal calendar, which ends on the last Saturday of December
yoffset = pd.tseries.offsets.FY5253(n=1, weekday=5, startingMonth=12, variation=variation)

# use the offset to create a date range with intervals at each fiscal year beginning
yoffset_range = pd.date_range('2020', periods=3, freq=yoffset)
yoffset_range
```

```
DatetimeIndex(['2020-12-26', '2021-12-25', '2022-12-31'], dtype='datetime64[ns]', freq='RE-L-DEC-SAT')
```

Let's take a look at the above result - we've generated a `DatetimeIndex` with the _last_ day of each fiscal year. In this case, we are telling `pandas` to create an offset using a 52/53 workweek calendar where the last day of the fiscal calendar lands on **the last (`variation='last'`) Saturday (`weekday=5`) in December (`month=12`)**. See [documentation](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html) for an explainer on the other parameters, and the 'nearest' variation.

Notice the new `freq` string. Creating the timeseries offset object generates a new `freq` string that you can use for the `pd.date_range` function. However, unlike the previous examples you can't convert these to `Period` objects to get the quarter, month, etc (you can try it - it'll return an error).

So how can we use this to create a lookup table? We can do it manually with a loop and `pd.date_range`:

```python
# Create a '1 day' offset:
d1 = pd.tseries.offsets.DateOffset(n = 1)

# Specify the starting fiscal year
yr = (yoffset_range[0] - pd.tseries.offsets.DateOffset(n=8)).year +1

# iterate over each item in the date range we created earlier:
result = pd.DataFrame()
for i in yoffset_range:
    # recall each item is a Timestamp that represents the first day of the fiscal year,
    # so create a date_range from beginning to end of the fiscal year
    current_range = pd.date_range(i+d1, i+yoffset, freq='D')
    interim_df = pd.DataFrame(index = current_range)
    # day of year
    interim_df['DOY'] = (current_range-current_range[0]).days +1
    # fiscal year
    interim_df['FY'] = yr
    result = result.append(interim_df)
    yr += 1

# See what we get:
result.query('FY==2021').tail(10)
```

|            | DOY |   FY |
| :--------- | --: | ---: |
| 2021-12-16 | 355 | 2021 |
| 2021-12-17 | 356 | 2021 |
| 2021-12-18 | 357 | 2021 |
| 2021-12-19 | 358 | 2021 |
| 2021-12-20 | 359 | 2021 |
| 2021-12-21 | 360 | 2021 |
| 2021-12-22 | 361 | 2021 |
| 2021-12-23 | 362 | 2021 |
| 2021-12-24 | 363 | 2021 |
| 2021-12-25 | 364 | 2021 |

This loop created a dataframe with the daily `pd.DatetimeIndex` and a few columns that specify where each calendar day falls in the fiscal year.

We can also add more features, like the workweek in the year, which fiscal quarter that day falls under, and more:

```python
# workweek in year
result['WW'] = ((result['DOY']-1) //7) + 1
# fiscal quarter
result['FQ'] = np.minimum((result['WW']//13) + 1, 4)
# workweek in quarter
result['WWinQ'] = result['WW'] - ((result['FQ']-1) * 13)
# fiscal month
result['FM'] = ((result['FQ']-1)*3) + np.minimum(((result['WWinQ'] // 4)+1), 3)

# Show the result
result.query('FY==2021').tail(10)
```

|            | DOY |   FY |  WW |  FQ | WWinQ |  FM |
| :--------- | --: | ---: | --: | --: | ----: | --: |
| 2021-12-16 | 355 | 2021 |  51 |   4 |    12 |  12 |
| 2021-12-17 | 356 | 2021 |  51 |   4 |    12 |  12 |
| 2021-12-18 | 357 | 2021 |  51 |   4 |    12 |  12 |
| 2021-12-19 | 358 | 2021 |  52 |   4 |    13 |  12 |
| 2021-12-20 | 359 | 2021 |  52 |   4 |    13 |  12 |
| 2021-12-21 | 360 | 2021 |  52 |   4 |    13 |  12 |
| 2021-12-22 | 361 | 2021 |  52 |   4 |    13 |  12 |
| 2021-12-23 | 362 | 2021 |  52 |   4 |    13 |  12 |
| 2021-12-24 | 363 | 2021 |  52 |   4 |    13 |  12 |
| 2021-12-25 | 364 | 2021 |  52 |   4 |    13 |  12 |

# Summary

Great! We can summarize the function a [public gist](https://gist.github.com/banditkings/735fe1885a442b3457d208060ac4b970).

So if you have a pretty clean fiscal calendar, `pandas` has you covered. But if you use a 4-4-5 calendar (aka 52/53 workweek calendar) then you'll mostly be building one from scratch. `pandas` _does_ help a little bit with finding the beginning and end dates of each fiscal year, which helps you avoid having to write your own logic to handle leap years and deciding which years have 52 workweeks instead of 53 workweeks.

## References Used

- [Pandas user guide on time series/date functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
- [Pandas docs on `timedeltas`](https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html)
- [Pandas Reference Docs on Date offsets](https://pandas.pydata.org/docs/reference/offset_frequency.html#)
- [Docs on Period objects](https://pandas.pydata.org/docs/reference/api/pandas.Period.html)
- [Pandas frequency strings aka offset aliases](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases)
- [Pandas Info on the FY5253 offset](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html)
