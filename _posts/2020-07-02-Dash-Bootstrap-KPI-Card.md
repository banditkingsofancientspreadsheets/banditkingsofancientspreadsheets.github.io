---
title: "KPI Card with Dash Bootstrap Components"
date: 2020-07-02
classes: wide
tags: [cheatsheets, python]
excerpt: "Code snippet to create a starter KPI card with Dash Bootstrap Components"
---

[Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai) has a fantastic library of plug and play [components](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/) that make it easy to get started.

Plotly's documentation is focused on making tables, charts, and graphs, but for executives I find myself relying on KPI cards like this:
![](/assets/images/dbc_kpi1.png)

You can find better styled examples of these all over the place if you google 'HTML/CSS dashboard examples.'

The magic of using Dash is that you can style these to your heart's content with CSS and all of the values can be generated with Python, and the whole thing can be reproducible and components can be shared across projects. And the flexbox system is just fine rather than fiddling with positioning in PowerBI.

Here's the sketch of the starter KPI dashboard:
![](/assets/images/dbc_kpi2.png)

Python Code for your `app.py` file:
```python
import dash  # (version 1.12.0) pip install dash

import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

header = html.Div([
    dbc.Row(dbc.Col(html.H1("H1 Text"))),
])

card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "$10.5 M",
                    className="card-value",
                ),
                html.P(
                    "Target: $10.0 M",
                    className="card-target",
                ),
                html.Span(
                    "Up ",
                    className="card-diff-up",
                ),
                html.Span(
                    "5.5% vs Last Year",
                    className="card-diff-up",
                ),

            ]
        ),
    ],
)

row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card),
                dbc.Col(card),
                dbc.Col(card),
            ]
        ),
    ], style={'padding': '25px'}
)

app.layout = html.Div([
    header, 
    row,
    row
])

if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
```

And some basic CSS styling:
```css
.card {
    text-align: center;
}
.card .card-title {
    text-align: left;
    font-weight: lighter;
}

.card .card-value {
    font-size: 2rem;
}

.card .card-target {
    font-size: 1rem;
    font-weight: lighter;
}

.card .card-diff-down {
    color: red
}

.card .card-diff-up {
    color: green
}
```