# Los Angeles Marathon Finishing Time Estimator

<img src="https://github.com/Peter-Chong/RunTheData/blob/master/Images/Screenshot%202020-07-26%20at%2010.17.11%20PM.png" width="900" height="230" />

## Table of Contents  

<!--ts-->
   * [Problem Statement](#problem-statement)
   * [Project Overview](#project-overview)
   * [Code and Resources Used](#code-and-resources-used)
   * [Data Preprocessing](#data-preprocessing)
      * [Feature Engineering and External Data](#feature-engineering-and-external-data)
   * [Exploratory Data Analysis](#exploratory-data-analysis)
   * [Model Building](#model-building)
   * [Results](#results)
   * [Multiple Linear Regressions Performance](#multiple-linear-regressions-performance)
   * [Personal Prediction Result](#personal-prediction-result)
   * [Things I wish to improve on if I were to do this project again](#things-i-wish-to-improve-on-if-i-were-to-do-this-project-again)
<!--te-->

## Problem Statement

As an avid marathon runner, I always wonder if I can predict my finishing time before the marathon day based on my marathon day's temperature, humidity, age, gender and etc. Although I have never run Los Angeles Marathon before, I would like to see if my model can predict my past marathon which was held in a different country. By using these predictors, I was able to predict my finishing time with an error of only 17 minutes. In order to obtain a more accurate prediction, I added my running split times which greatly increase my prediction ability to an error of only 5 minutes.

My ultimate goal is to predict marathon finishing time in general and not only for Los Angeles Marathon. In order to do this, I will require more data which I intend to do in the future.

## Project Overview

* Built a web scrapper from scratch and scraped over 75,000 marathon runners data from Los Angeles Marathon official website using python and selenium
* Engineered features and cleaned data by binding all datasets, parsing marathon times into seconds and adding appropriate columns
* Performed deep exploratory data analysis which includes 12 different charts and comments
* Optimized Multiple Linear Regression, Lasso, and Ridge to reach the best model
* Metrics of R^2, MAE (Mean Absolute Error) and MAPE (Mean Absolute Percentage Error) are used to measure the results

## Code and Resources Used

**Programming Language:** R and Python  
**Packages:** Selenium, Pandas, ggplot2, dplyr, ggridges  
**Data Source:**  
www.trackshackresults.com/lamarathon/results/2015_Marathon/  
www.timeanddate.com/weather/usa/los-angeles  
**Inspiration:**
www.towardsdatascience.com/half-marathon-finish-time-prediction-part-1-5807760033eb

## Data Preprocessing

Initially, there were 120 data sets (4 years x 15 age groups x 2 genders) with approximately 75k runners in total. The following features were scrapped using my web scrapper:  

* Name - name of each runner
* Bib - race number given to each runner
* Age - age of each runner
* Position - overall ranking of runner
* Gender Position - ranking of runner based on gender
* Division Position - ranking of runner based on age division
* 5K, 10K, 15K, 20K, 25K, 30K, 35K, 40K - elapsed time at every 5 kilometers split
* Clock Time - finishing time since the race started
* Net Time - finishing time since the runner crosses the starting line
* Hometown - hometown of each runner

### Feature Engineering and External Data

For each of the datasets, I removed all the rows with NULL split times, added gender and year columns, and merge all 120 datasets together into one big csv file.
  
Historical weather data (temperature and humidity) from the [internet](https://www.timeanddate.com/weather/usa/los-angeles) for each year were collected and added. The time for these weather data was 8:47am since the marathon started at 8am.  
  
The variables 5K, 10K, 15K, 20K, 25K, 30K, 35K, 40K, Clock Time and Net Time were transformed into seconds to make arithmetic easier. Age Group and the pace for each leg were added too.

Lastly, I added a variable called Hubris which essentially is the percentage changed in each leg compared to their 5k to 10k pace. By assuming each runners' ideal pace is ran between 5k to 10k, I was hoping this variable can show us a different analysis during EDA.  

## Exploratory Data Analysis

Below are a few highlights from my EDA.  
  
The graph below shows the standard deviation of the pace for the 9 time splits computed individually for each runner, where one circle represents a runner. The darker the circle, the higher the standard deviation of the pace for the runner. In other words, the darker the circle means that the runner changes his or her pace greatly every 5 kilometers split; a more uneven pace.  
  
By looking at the graph, we can observe that the more uneven pace leads to a longer finishing time. It is clear that it would be advantageous if the runners kept an even pace throughout the marathon.

<img src="https://github.com/Peter-Chong/RunTheData/blob/master/EDA_files/figure-gfm/unnamed-chunk-14-1.png" />

Other than that, it is also interesting to see the relationship between finishing time and age. The graph below is a 2d density plot of finishing time against age. From this graph, it can be observed that most of the teenagers finish their marathons at around 6.5 hours whereas most of the runners at the age of early 30s finish at around 4.5 hours. The reason behind this might be because teenagers overestimate themselves at the early stage of the race and ran at a higher pace which leads them to exhaustion at the second half of the marathon whereas runners at the age of early 30s pace themselves more carefully.  
  
<img src="https://github.com/Peter-Chong/RunTheData/blob/master/EDA_files/figure-gfm/unnamed-chunk-9-1.png" />

Lastly, to prove that teenagers do not pace themselves evenly, we plot a bar chart of Hubris against each 5k split per age group. Hubris is variable showing the percentage changed in each split compared to the runner's 5k to 10k pace. The higher the bars means that the higher the difference in pace compared to their 5k to 10k pace. It can be seen that the younger the runner is, the higher the Hubris is, which explains why I believe teenagers do not pace themselves well.  
  
<img src="https://github.com/Peter-Chong/RunTheData/blob/master/EDA_files/figure-gfm/unnamed-chunk-22-1.png" />

## Model Building

Firstly, I split the dataset into a training set (80% of the runners) and a test set (20% of the runners).

The metrics to evaluate my models will be R^2, MAE (Mean Absolute Error) and MAPE (Mean Absolute Percentage Error). This is because they are all relatively easy to interpret.

I tried three different models:
* Multiple Linear Regression
* Lasso Regression
* Ridge Regression

## Results

Below is a table of the results of each model for 3 scenarios

<img src="https://github.com/Peter-Chong/RunTheData/blob/master/Images/Screenshot%202020-09-10%20at%203.38.41%20PM.png" width="275" /><img src="https://github.com/Peter-Chong/RunTheData/blob/master/Images/Screenshot%202020-09-10%20at%203.38.56%20PM.png" width="275" /><img src="https://github.com/Peter-Chong/RunTheData/blob/master/Images/Screenshot%202020-09-10%20at%203.39.05%20PM.png" width="275" />

Multiple Linear Regression seems to be the best model for all those scenarios. 

## Multiple Linear Regressions Performance

Below is the results for 3 scenarios if we implement multiple linear regression. We can see that by just knowing our 5km and 10km split times, we can greatly decrease our MAE by more than 50%.

<img src="https://github.com/Peter-Chong/RunTheData/blob/master/Images/Screenshot%202020-09-10%20at%203.39.18%20PM.png" width="800" />

Other than that, we can visualize the predicted value against the actual value

<img src="https://github.com/Peter-Chong/RunTheData/blob/master/ModelBuilding_files/figure-gfm/unnamed-chunk-11-1.png" />

## Personal Prediction Result

Let’s see what the model predicts for my previous marathon. 

<img src="https://github.com/Peter-Chong/RunTheData/blob/master/Images/Screenshot%202020-09-10%20at%206.57.01%20PM.png" width="800" />

This is extremely surprising to me since the marathon I ran was in a totally different country, even a different continent, yet I am able to predict my finishing time to as close as 5 minutes error.

## Things I wish to improve on if I were to do this project again

* Use a better historical weather dataset. Instead of constant values for each year, the weather variable should be based on each runners' halfway point and location
* Insert more data variables such as race elevation and runner's past marathon results
* Create a map that visualizes where the runners came from
* Productionionize the model by building a flask API endpoint that takes in a list of values and returns an estimated finishing time




















