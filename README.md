# Los Angeles Marathon Finishing Time Estimator

<img src="https://github.com/Peter-Chong/RunTheData/blob/master/Images/Screenshot%202020-07-26%20at%2010.17.11%20PM.png" width="1000" height="250" />

## Problem Statement

As an avid marathon runner, I always wonder if I can predict my finishing time before the marathon day based on my marathon day's temperature, humidity, age and gender. By using these four predictors, I was able to predict XXX. In order to obtain a more accurate prediction, I added my running split times which greatly increase my prediction ability.

My ultimate goal is to predict marathon finishing time in general and not only for Los Angeles Marathon. In order to do this, I will require more data which I intend to do in the future.

## Project Overview

* Built a web scrapper from scratch and scraped over 75,000 marathon runners data from Los Angeles Marathon official website using python and selenium
* Engineered features and cleaned data by binding all datasets, parsing marathon times into seconds and adding appropriate columns
* Performed deep exploratory data analysis which includes 12 different charts and comments
* Optimized Linear, XXX, and Random Forest Regressors using GridsearchCV (XXX) to reach the best model
* Metrics of XXX R^2 and RMSE (Root Mean Squared Error) are used to measure the results

## Code and Resources Used

**Programming Language:** R and Python
**Packages:** Selenium, Pandas, ggplot2, dplyr, ggridges
**Data Source:** [www.trackshackresults.com/lamarathon/results/2015_Marathon/]

## Data Preprocessing

Initially 

Initially there were 4 data sets, one for each year of 2015-2018, with approximately 25k runners per year or 100k runners in total. The following features were given in each set:
