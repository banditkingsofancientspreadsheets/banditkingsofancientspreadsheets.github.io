---
title: "Make a Basic PnL Dataframe"
date: 2020-06-30
classes: wide
tags: [cheatsheets, python]
excerpt: "Code snippet to create a PnL (Profit and Loss Statement) Dataframe in Pandas"
mathjax: "true"
---

This code creates a practice dataframe for instruction in a format that is familiar with finance analysts. Analysts typically deal with profit and loss statement data in excel spreadsheets, often pulled or aggregated from an ERP source system and this example shows a toy example that has some relevant fields and formatting.

```python
import pandas as pd

# For convenience while using a Jupyter Notebook, 
# display dataframe floats as currency & round to two decimal places
pd.options.display.float_format = '${:,.2f}'.format

def make_pnl():
    df = pd.DataFrame(data={'ProductLine': ['A', 'A', 'B', 'B'],
                            'FunctionalArea': ['REV', 'COS']*2,
                            'AccountL1': ['Revenue', 'Cost of Sales']*2,
                            '201901 ACT': [200., 100., 150., 75.],
                            '202001 ACT': [210., 105., 150., 75.],
                            '202001 POR': [205., 105., 150., 75.]
                        })
    return df

df = make_pnl()
```

![](/assets/images/example_pnl.png)

This is a very simplified version of the data that would be familiar to analysts. In reality, there would be many more fields and values, depending on the level of granularity that's available. The columns like '201901 ACT' are time periods in a YYYYQQ format and the last three letters signify whether it is an actual or forecast (POR or Plan of Record) value.

