---
title: “Time Series Cheat Sheet in R”
date: 2020-01-26
tags: [R]
excerpt: "Getting started using the `forecast` package for time series data in R, as quickly as possible and no explanations."
mathjax: "true"
---

Getting started using the `forecast` package for time series data in R, as quickly as possible and no explanations. 

Source: [Forecasting: Principles and Practice](https://otexts.com/fpp2/)

# Data Prep

Coerce your data to `ts` format:
```r
library(tidyverse)
library(forecast)

myts <- ts(df, start = c(1981,1), frequency = 12)
```

# Exploring and Plotting `ts` Data

* `autoplot()`: Useful function to plot data and forecasts

## Seasonality

* `ggseasonplot()`: Create a seasonal plot
* `ggsubseriesplot()`: Create mini plots for each season and show seasonal means

## Lags and ACF

* `gglagplot()`: Plot the time series against lags of itself
* `ggAcf()`: Plot the autocorrelation function (ACF)

## White Noise and the Ljung-Box Test
White Noise is another name for a time series of iid data. Purely random. Ideally your model residuals should look like white noise. 

You can use the Ljung-Box test to check if a time series is white noise:

```r
Box.test(data, lag = 24, type="Lj")
```

p-value > 0.05 suggests data are not significantly different than white noise

# Model Selection

The `forecast` package includes a few common models out of the box. Fit the model and create a `forecast` object, and then use the `forecast()` function on the object and a number of `h` periods to predict.

Example of the workflow:

```r
train <- window(data, start = 1980)
fit <- naive(train)
checkresiduals(fit)
pred <- forecast(fit, h=4)
accuracy(pred, data)
```

## Naive Models

Benchmarking with naive and seasonal naive models.
* `naive()`
* `snaive()`

## Residuals

Residuals are the difference between the model's fitted values and the actual data. 

Residuals should look like white noise and be:

* Uncorrelated
* Have mean zero

And ideally have:
* Constant variance
* A normal distribution

`checkresiduals()`: helper function to plot the residuals, plot the ACF and histogram, and do a Ljung-Box test on the residuals.

## Evaluating Model Accuracy

Train/Test split with window function:
`window(data, start, end)`: to slice the `ts` data

Use `accuracy()` on the model and test set
`accuracy(model, testset)`: Provides accuracy measures like MAE, MSE, MAPE, RMSE etc

Backtesting with one step ahead forecasts, aka "Time series cross validation" can be done with a helper function `tsCV()`.

`tsCV()`: returns forecast errors given a `forecastfunction` that returns a `forecast` object and number of steps ahead `h`. At `h` = 1 the forecast errors will just be the model residuals.

Here's an example using the `naive()` model:

```r
tsCV(data, forecastfunction = naive, h = 1)
```

# Many Models

## Exponential Models

* `ses()`: Simple Exponential Smoothing, implement a smoothing parameter alpha on previous data
* `holt()`: Holt's linear trend, SES + trend parameter. Use `damped`=TRUE for damped trending
* `hw()`: Holt-Winters method, incorporates linear trend and seasonality. Set `seasonal`="additive" for additive version or "multiplicative" for multiplicative version

### ETS Models

The `forecast` package includes a function `ets()` for your exponential smoothing models. `ets()` estimates parameters using the likelihood of the data arising from the model, and selects the best model using corrected AIC (AICc)
    * Error = {A, M}
    * Trend = {N, A, Ad}
    * Seasonal = {N, A, M}

## Transformations

May need to transform the data if it is non-stationary to improve your model prediction. To deal with non-constant variance, you can use a **Box-Cox** transformation.

`BoxCox()`: Box-Cox uses a `lambda` parameter between -1 and 1 to stabilize the variance. A `lambda` of 0 performs a natural log, 1/3 does a cube root, etc while 1 does nothing and -1 performs an inverse transformation.

**Differencing** is another transformation that uses differences between observations to model changes rather than the observations themselves. 

## ARIMA

**Parameters**: (p,d,q)(P,D,Q)m

|Parameter|Description          |
|-------------------------------|
|p| # of autoregression lags    |
|d| # of lag-1 differences      |
|q| # of Moving Average lags    |
|P| # of seasonal AR lags       |
|D| # of seasonal differences   |
|Q| # of seasonal MA lags       |
|m| # of observations per year  |
|-------------------------------|

`Arima()`: Implementation of the ARIMA function, set `include.constant` = TRUE to include drift aka the constant

`auto.arima()`: Automatic implentation of the ARIMA function in `forecast`. Estimates parameters using maximum likelihood and does a stepwise search between a subset of all possible models. Can take a `lambda` argument to fit the model to transformed data and the forecasts will be back-transformed onto the original scale. Turn `stepwise` = FALSE to consider more models at the expense of more time. 

## Dynamic Regression
Regression model with non-seasonal ARIMA errors, i.e. we allow e_t to be an ARIMA process rather than white noise. 

Usage example:
```r
fit <- auto.arima(data, xreg = xreg_data)
pred <- forecast(fit, xreg = newxreg_data)
```

## Dynamic Harmonic Regression
Dynamic Regression with `K` fourier terms to model seasonality. With higher `K` the model becomes more flexible.

Pro: Allows for any length seasonality, but assumes seasonal pattern is unchanging. `Arima()` and `auto.arima()` may run out of memory at large seasonal periods (i.e. >200).

```r
# Example with K = 1 and predict 4 periods in the future
fit <- auto.arima(data, xreg = fourier(data, K = 1),
                  seasonal = FALSE, lambda = 0)
pred <- forecast(fit, xreg = fourier(data, K = 1, h = 4))
```

## TBATS
Automated model that combines exponential smoothing, Box-Cox transformations, and Fourier terms. 
Pro: Automated, allows for complex seasonality that changes over time.
Cons: Slow.

* T: Trigonemtric terms for seasonality
* B: Box-Cox transformations for heterogeneity
* A: ARMA errors for short term dynamics
* T: Trend (possibly damped)
* S: Seasonal (including multiple and non-integer periods)