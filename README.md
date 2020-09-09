# Los Angeles Marathon Finishing Time Estimator

<img src="https://github.com/Peter-Chong/RunTheData/blob/master/Images/Screenshot%202020-07-26%20at%2010.17.11%20PM.png" width="900" height="230" />

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
**Data Source:**  
www.trackshackresults.com/lamarathon/results/2015_Marathon/  
www.timeanddate.com/weather/usa/los-angeles

## Data Preprocessing

Initially there were 120 data sets (4 years x 15 age groups x 2 genders) with approximately 75k runners in total. The following features were scrapped using my web scrapper:  

* Name - name of each runner
* Bib - race number given to each runner
* Age - age of each runner
* Position - overall ranking of runner
* Gender Position - ranking of runner based on gender
* Division Position - ranking of runner based on age division
* 5K, 10K, 15K, 20K, 25K, 30K, 35K, 40K - elapsed time at each 5 kilometers split
* Clock Time - finishing time since the race started
* Net Time - finishing time since the runner cross the starting line
* Hometown - hometown of each runner

### Feature enginering and external data

For each of the datasets, I removed all the rows with NULL split times, added gender and year columns and merge all 120 datasets together into one big csv file.
  
Historical weather data (temperature and humidity) from the [internet](https://www.timeanddate.com/weather/usa/los-angeles) for each year was collected and added. The time for these weather data was 8:47am since the marathon started at 8am.  
  
The variables 5K, 10K, 15K, 20K, 25K, 30K, 35K, 40K, Clock Time and Net Time were transformed into seconds to make arithmetic easier. Age Group and the pace for each legs were added too.

Lastly, I added a variable called Hubris which essentially is the percentage changed in each leg compared to their 5k to 10k pace. By assuming each runners' ideal pace is ran between 5k to 10k, I was hoping this variable can show us a different analysis during EDA.  

## Exploratory data analysis

Below are a few highlights from the my EDA.  
  
The graph below shows the standard deviation of the pace for the 9 time split computed individually for each runner, where one circle represents a runner. The darker the circle, the higher standard deviation of the pace for the runner. In other words, the darker the circle means that the runner changes his or her pace greatly every 5 kilometers split; a more uneven pace.  
  
By looking at the graph, we can observe that the more uneven pace leads to longer finishing time. It is clear that it would be advantageous if the runners kept an even pace throughout the marathon.

<img src="https://github.com/Peter-Chong/RunTheData/blob/master/EDA_files/figure-gfm/unnamed-chunk-14-1.png"  width="500"/>
  
## Things I wish to improve on if I were to do this project again

* Use a better historical weather dataset. Instead of constant values for each year, the weather variable should based on each runners' halfway point and location
* Insert more data variables such as race elevation and runner's past marathon results
* Create a map that visualize where the runners came from









