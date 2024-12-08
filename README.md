# Freight Transportation Services Index (TSI) Analysis

## Overview

This project focuses on analyzing and forecasting the **Freight Transportation Services Index (TSI)**, a key indicator of the volume of freight and passenger transportation services in the United States. Using advanced time series models, the project evaluates the impact of external shocks, such as the COVID-19 pandemic, and develops predictive models for the TSI. The analysis incorporates methods like ARIMA, ARIMAX, and GARCH to capture trends, seasonality, and volatility in the data.

---

## Table of Contents

1. [Objective](#objective)
2. [Dataset Description](#dataset-description)
3. [Methodology](#methodology)
4. [Key Findings](#key-findings)
5. [Technologies Used](#technologies-used)
6. [Project Structure](#project-structure)
7. [How to Run](#how-to-run)
8. [Future Enhancements](#future-enhancements)
9. [References](#references)

---

## Objective

The goal of this project is to:
- Forecast future values of the TSI using time series models.
- Assess the impact of external factors, such as the COVID-19 pandemic, on transportation trends.
- Provide insights for stakeholders, including policymakers, transportation analysts, and businesses.

---

## Dataset Description

- **Data Source**: [Freight Transportation Services Index](https://data.bts.gov/Research-and-Statistics/Freight-Transportation-Service-Index/n68x-u7m7)
- **Period**: January 2000 to December 2023
- **Variables**:
  - `tsi_total`: Monthly index of transportation services.
  - `obs_date`: Observation date.
  - `covid_indicator`: A manually added binary variable indicating the COVID-19 impact.

---

## Methodology

### 1. Data Preprocessing
- Cleaned and standardized column names.
- Converted `obs_date` to datetime format.
- Differenced the data to achieve stationarity.

### 2. Exploratory Data Analysis (EDA)
- Visualized time series data to identify trends, seasonality, and external shocks.
- Conducted ACF and PACF analyses to select ARIMA model orders.

### 3. Modeling
- **ARIMA Models**: Evaluated multiple orders like (0,1,0), (3,1,2), and (1,1,2).
- **ARIMAX Models**: Incorporated `covid_indicator` as an exogenous variable.
- **GARCH Models**: Assessed volatility clustering and ARCH effects.

### 4. Diagnostics
- Residual analysis (ACF, PACF, histogram, and Q-Q plots).
- Shapiro-Wilk and Ljung-Box tests for normality and autocorrelation.
- McLeod-Li test for ARCH effects.

---

## Key Findings

1. **Impact of COVID-19**:
   - The `covid_indicator` variable showed limited effect on the ARIMAX model's performance, indicating the pandemic's complexity.
2. **Best-Performing Models**:
   - ARIMA(1,1,2) provided robust predictions with well-behaved residuals.
   - GARCH(1,1) effectively captured volatility clustering without significant ARCH effects.
3. **Residual Analysis**:
   - Residuals from ARIMA models showed minimal autocorrelation but deviated from normality.
   - GARCH residuals exhibited desired characteristics, supporting the model's adequacy.

---

## Technologies Used

- **Languages**: Python, R
- **Libraries**:
  - **Python**: `pandas`, `numpy`, `statsmodels`, `matplotlib`, `arch`, `scipy`
  - **R**: `tidyverse`, `tseries`, `forecast`, `zoo`, `janitor`
- **Visualization**: Matplotlib, ggplot2

---

## Project Structure

```
Freight-Service-Index-Forecasting/
├── data/
│   ├── TSIS_With_covid_indicator.csv
|   ├── Transportation_Services_Index_and_Seasonally.csv
├── scripts/
│   ├── FTS_Covid_Indicator.py
│   ├── Freight_Transportation_Service.qmd.Rmd
├── report/
│   └── final_report_ts.pdf
├── README.md
└── requirements.txt
```

---

## How to Run

### Prerequisites
- Install Python 3.8+ and R.
- Install required Python libraries:
  ```bash
  pip install -r requirements.txt
  ```
- Ensure R is configured with necessary packages (`tidyverse`, `forecast`, `tseries`).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/lohitmarla-uconn/Freight-Service-Index-Forecasting.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Freight-Service-Index-Forecasting
   ```
3. Run the Python scripts:
   ```bash
   python scripts/FTS_Covid_Indicator.py
   ```
4. Analyze results in the `reports/` directory.

---

### Running the R Script

The R script `Freight_Transportation_Service.qmd.Rmd` is used for data analysis and time series forecasting. Follow the steps below to run the script:

#### Prerequisites
1. **Install R**:
   - Download and install R from [CRAN](https://cran.r-project.org/).
   - Optionally, install RStudio for a user-friendly interface.

2. **Install Required R Packages**:
   Open R or RStudio and run the following command to install the necessary packages:
   ```R
   install.packages(c("tidyverse", "janitor", "tseries", "zoo", "forecast", "astsa", "TSA"))
   ```

3. **Install Quarto**:
   - Quarto is required to render the `.qmd` file. Install it from [Quarto's website](https://quarto.org/).

---

#### Running the Script

To execute the R script and generate the output:
1. **Navigate to the Project Directory**:
   ```bash
   cd Freight-Service-Index-Forecasting/scripts
   ```

2. **Render the Quarto File**:
   Use the following command to render the Quarto `.qmd` file and generate the report:
   ```bash
   quarto render Freight_Transportation_Service.qmd.Rmd
   ```

3. **Output**:
   - The rendered output (HTML) will be saved in the same directory as the `.qmd` file by default.

---

## Future Enhancements

1. **Incorporate Advanced Models**:
   - Explore deep learning methods (e.g., LSTM, GRU) for improved forecasting.
2. **Dashboard**:
   - Create an interactive dashboard for real-time monitoring of TSI trends.
3. **Broader Analysis**:
   - Include other components of TSI (freight and passenger indices) for a holistic view.

---

## References

- Data Source: [Freight Transportation Services Index](https://data.bts.gov/Research-and-Statistics/Freight-Transportation-Service-Index/n68x-u7m7)
- Bureau of Transportation Statistics (BTS)

