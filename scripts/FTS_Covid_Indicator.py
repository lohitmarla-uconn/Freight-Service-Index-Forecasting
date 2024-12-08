# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from arch import arch_model
from scipy.stats import shapiro, jarque_bera

# Load the data
tsi_data = pd.read_csv("data/TSIS_With_covid_indicator.csv")
tsi_data.columns = tsi_data.columns.str.lower()  # Clean column names
tsi_data['obs_date'] = pd.to_datetime(tsi_data['obs_date'])  # Ensure date column is in datetime format

# ARIMAX model with covid_indicator as exogenous variable
arimax_model = ARIMA(tsi_data['tsi_total'], order=(1, 1, 1), exog=tsi_data[['covid_indicator']]).fit()

# Summary of ARIMAX model
print("ARIMAX Model Summary with covid_indicator:")
print(arimax_model.summary())

# Residuals analysis for ARIMAX model
residuals = arimax_model.resid
plot_acf(residuals.dropna(), title="ACF of ARIMAX Model Residuals")
plt.show()

# Refitting ARIMA model without exogenous variable
arima_model = ARIMA(tsi_data['tsi_total'], order=(1, 1, 1)).fit()

# Summary of ARIMA model
print("ARIMA Model Summary (1,1,1):")
print(arima_model.summary())

# Residuals for ARIMA model
residuals = arima_model.resid
plt.plot(residuals, label="Residuals")
plt.title("ARIMA Model Residuals")
plt.legend()
plt.show()

# Histogram and QQ Plot of residuals
plt.hist(residuals.dropna(), bins=20, density=True, alpha=0.7, label="Residuals")
plt.title("Histogram of Residuals")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.legend()
plt.show()

plt.figure()
plt.title("Normal Q-Q Plot of Residuals")
sm.qqplot(residuals, line='s')
plt.show()

# Shapiro-Wilk Test for Normality
shapiro_test = shapiro(residuals.dropna())
print("Shapiro-Wilk Test:")
print(f"Statistic: {shapiro_test[0]}, p-value: {shapiro_test[1]}")

# Ljung-Box Test for autocorrelation
ljung_box_test = acorr_ljungbox(residuals, lags=[4, 8], return_df=True)
print("\nLjung-Box Test Results:")
print(ljung_box_test)

# ARIMA(1, 1, 2) Model
arima_model_2 = ARIMA(tsi_data['tsi_total'], order=(1, 1, 2)).fit()

# Residual Analysis
print("\nARIMA Model (1,1,2) Summary:")
print(arima_model_2.summary())

residuals = arima_model_2.resid
plot_acf(residuals.dropna(), title="ACF of ARIMA(1,1,2) Residuals")
plt.show()

# Forecasting
forecast = arima_model_2.get_forecast(steps=48)
forecast_index = pd.date_range(tsi_data['obs_date'].iloc[-1], periods=48, freq='M')
forecast_mean = forecast.predicted_mean
forecast_conf_int = forecast.conf_int()

# Plot forecast
plt.plot(tsi_data['obs_date'], tsi_data['tsi_total'], label="Original Data", color="blue")
plt.plot(forecast_index, forecast_mean, label="Forecast", color="red", linestyle="--")
plt.fill_between(forecast_index, forecast_conf_int.iloc[:, 0], forecast_conf_int.iloc[:, 1],
                 color="gray", alpha=0.3, label="Prediction Intervals")
plt.title("Forecast with ARIMA(1,1,2)")
plt.xlabel("Time")
plt.ylabel("TSI Total")
plt.legend()
plt.show()

# ARCH Effect Test and GARCH Model
returns = tsi_data['tsi_total'].diff().dropna()
plot_acf(returns ** 2, title="ACF of Squared Returns")
plt.show()

# Fit GARCH(1,1) Model
garch_model = arch_model(returns, vol="Garch", p=1, q=1).fit()
print("\nGARCH Model Summary:")
print(garch_model.summary())

# Residuals analysis for GARCH model
garch_residuals = garch_model.resid
plt.plot(garch_residuals, label="GARCH Residuals")
plt.title("GARCH Residuals Plot")
plt.legend()
plt.show()

# Jarque-Bera Test for Normality
jb_test = jarque_bera(garch_residuals)
print("\nJarque-Bera Test for GARCH Residuals:")
print(f"Statistic: {jb_test[0]}, p-value: {jb_test[1]}")

# Ljung-Box Test for Residuals Squared
ljung_box_test = acorr_ljungbox(garch_residuals ** 2, lags=[1, 5, 10], return_df=True)
print("\nLjung-Box Test Results for Residuals Squared:")
print(ljung_box_test)
