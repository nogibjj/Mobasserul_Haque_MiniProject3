# Pandas Descriptive Script Mini Project
[![CI](https://github.com/nogibjj/Mobasserul_Haque_MiniProject2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mobasserul_Haque_MiniProject2/actions/workflows/cicd.yml)

This project performs exploratory data analysis (EDA) on a dataset containing customer purchasing behavior, providing insights into various patterns and relationships using `Polars`, `Matplotlib`.

## Table of Contents
- [Overview](#overview)
- [Source](#source)
- [About Dataset](#about-dataset)
  - [Dataset Columns](#dataset-columns)
- [Features](#features)
- [Summary Statistics](#summary-statistics)
- [Data Visualization](#data-visualization)
- [Setup](#setup)
  - [Development Environment (Dev Container)](#development-environment-dev-container)
  - [Makefile](#makefile)
  - [GitHub Actions](#github-actions)
- [Usage](#usage)
  - [Histograms](#histograms)
  - [Bar Plot by Category](#bar-plot-by-category)
- [Running Tests](#running-tests)
- [Dependencies](#dependencies)
- [License](#license)

## Overview
This project focuses on analyzing customer purchasing behavior using a dataset in CSV format using `Polars`. It generates various statistical summaries and visualizations to help understand trends, relationships, and distributions in the data.

## Source
The dataset used in this project is **Customer Purchasing Behaviors**, which can be found on Kaggle:  
[Customer Purchasing Behaviors Dataset](https://www.kaggle.com/datasets/hanaksoy/customer-purchasing-behaviors)

## About Dataset

### Dataset Columns
- **customer_id**: Unique ID of the customer.
- **age**: The age of the customer.
- **annual_income**: The customer's annual income (in USD).
- **purchase_amount**: The total amount of purchases made by the customer (in USD).
- **purchase_frequency**: Frequency of customer purchases (number of times per year).
- **region**: The region where the customer lives (North, South, East, West).
- **loyalty_score**: Customer's loyalty score (a value between 0-100).

This dataset includes information on customer profiles and their purchasing behaviors. 
The data features columns for user ID, age, annual income, purchase amount, loyalty score, region, and purchase frequency. It is intended for analyzing customer segmentation and loyalty trends, and can be used for various machine learning and data analysis tasks related to customer behavior and market research.

## Features
- Display summary statistics, including median, range, and variance.
- Visualize data distributions with histograms.
- Plot scatter plots with categories (hue).
- Compare distributions across categories using box plots.
- Analyze correlations between numerical variables with a heatmap.
- Create scatter plots with trend lines for relationship analysis.
- Generate bar plots comparing categorical data.

## Summary Statistics
The `summary_statistics` function displays key metrics like the median, range, and variance for each numerical column.

| Metric | column | column_0 | column_1 | column_2 | column_3 | column_4 | column_5 | column_6 | column_7 | column_8 |
|--------|------|------|------|------|------|------|------|------|------|------|
| statistic | statistic | count | null_count | mean | std | min | 25% | 50% | 75% | max |
| user_id | user_id | 238.0 | 0.0 | 119.5 | 68.84886830345629 | 1.0 | 60.0 | 120.0 | 179.0 | 238.0 |
| age | age | 238.0 | 0.0 | 38.6764705882353 | 9.35111812969458 | 22.0 | 31.0 | 39.0 | 47.0 | 55.0 |
| annual_income | annual_income | 238.0 | 0.0 | 57407.56302521008 | 11403.875717398343 | 30000.0 | 50000.0 | 59000.0 | 67000.0 | 75000.0 |
| purchase_amount | purchase_amount | 238.0 | 0.0 | 425.6302521008403 | 140.0520617813922 | 150.0 | 320.0 | 440.0 | 530.0 | 640.0 |
| loyalty_score | loyalty_score | 238.0 | 0.0 | 6.794117647058823 | 1.8990468014330923 | 3.0 | 5.5 | 7.0 | 8.3 | 9.5 |
| region | region | 238 | 0 | None | None | East | None | None | None | West |
| purchase_frequency | purchase_frequency | 238.0 | 0.0 | 19.798319327731093 | 4.562884260556764 | 10.0 | 17.0 | 20.0 | 23.0 | 28.0 |

## Data Visualization

Below are sample visualizations produced by the project:

### Histograms for Selected Columns
![Histograms](Histogram_column_distributions.png)

### Bar Plot: Average purchase_amount by region
![Bar Plot](bar_plot_average_purchase_amt_by_regions.png)

## Setup

### Development Environment (Dev Container)
This project includes a development container setup, enabling you to develop in a fully configured environment. The container is based on the official Python image and installs all necessary dependencies.

To use the development container, ensure you have Docker installed and a supported code editor like VSCode. The editor will prompt you to "Reopen in Container" when the project is loaded.

### Makefile
The repository includes a `Makefile` to simplify the setup and execution of key commands.

- Install dependencies:
    ```bash
    make install
    ```

- Run linting checks using `pylint`:
    ```bash
    make lint
    ```

- Run tests:
    ```bash
    make test
    ```

- Clean up the environment:
    ```bash
    make clean
    ```

### GitHub Actions
This repository is equipped with GitHub Actions for continuous integration (CI). The workflow runs linting and testing automatically upon each push or pull request.

To view the status of the CI pipeline, navigate to the **Actions** tab of your repository on GitHub.

## Usage

### Histograms
The `plot_histograms` function generates histograms for specified columns in the dataset, displaying the distribution of values. The histograms are saved as images and embedded in the summary report. 

To use this function, you can call it with the following code:

```python
plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'], output_report)
```
This will produce histograms for the columns `age`, `annual_income`, `purchase_amount`, and `purchase_frequency`, showing the distribution of values for each. The generated histogram images are saved as `Histogram_column_distributions.png` and are included in the summary report.

### Bar Plot by Category
The `plot_bar_by_category` function compares the average values of a numerical column across different categories using a bar plot. The bar plot is saved as an image and embedded in the summary report.

To use this function, you can call it with the following code:

```python
plot_bar_by_category(df, 'region', 'purchase_amount', output_report)
```
This will generate a bar plot comparing the `average purchase_amount by region`. The generated bar plot image is saved as `bar_plot_average_purchase_amt_by_regions.png` and is included in the summary report.

