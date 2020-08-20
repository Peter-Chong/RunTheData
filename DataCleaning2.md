Data cleaning 2
================
Peter Chong

``` r
#Input files
df <- read.csv("/Users/wengliangchong/Desktop/RunTheData/MarathonData.csv", header = T, stringsAsFactors = F)
```

I will like to add the following columns:  
a) Temperature at 8:47am for every year in celcius  
b) Humidity at 8:47am for every year in percentage  
c) Age Group  
d) Every leg in seconds  
e) Pace f)
Hubris

## Adding temperature at 8:47am for every year in celcius

``` r
df$Temp <- ifelse(df$Year == 2015, 23, ifelse(df$Year == 2016, 14, ifelse(df$Year == 2017, 17, 11)))
```

## Adding humidity at 8:47am for every year in percentage

``` r
df$Humid <- ifelse(df$Year == 2015, 31, ifelse(df$Year == 2016, 81, ifelse(df$Year == 2017, 73, 66)))
```

## Adding age group

``` r
df$AgeGroup <- ifelse(df$Age < 25 , "1 ~ 24", ifelse(df$Age < 35 , "25 ~ 34", ifelse(df$Age < 45 , "35 ~ 44",
                  ifelse(df$Age < 55 , "45 ~ 54", ifelse(df$Age < 65 , "55 ~ 64", "65 ~ 90")))))
```

## Time to seconds function

``` r
time_to_sec <- function(string) {
  time_segments = strsplit(string, split = ":")[[1]]
  if (length(time_segments) == 2) {
    mins = as.numeric(time_segments[1])
    sec = as.numeric(time_segments[2])
    time = mins*60 + sec
  } else {
    hours = as.numeric(time_segments[1])
    mins = as.numeric(time_segments[2])
    sec = as.numeric(time_segments[3])
    time = hours*3600 + mins*60 + sec
  }
  return(time)
}
```

## Changing time to seconds and add the columns

``` r
df$X5ks <- sapply(df$X5k, time_to_sec)
df$X10ks <- sapply(df$X10k, time_to_sec)
df$X15ks <- sapply(df$X15k, time_to_sec)
df$X20ks <- sapply(df$X20k, time_to_sec)
df$X25ks <- sapply(df$X25k, time_to_sec)
df$X30ks <- sapply(df$X30k, time_to_sec)
df$X35ks <- sapply(df$X35k, time_to_sec)
df$X40ks <- sapply(df$X40k, time_to_sec)
df$X42ks <- sapply(df$Net.Time, time_to_sec)
```

## Adding pace for every legs

``` r
first5k <- second5k <- third5k <- fourth5k <- c()
fifth5k <- sixth5k <- seventh5k <- eighth5k <- last2k <- c()
for (i in 1:nrow(df)) {
  first5k[i] <- df$X5ks[i]/5
  second5k[i] <- (df$X10ks[i] - df$X5ks[i])/5
  third5k[i] <- (df$X15ks[i] - df$X10ks[i])/5
  fourth5k[i] <- (df$X20ks[i] - df$X15ks[i])/5
  fifth5k[i] <- (df$X25ks[i] - df$X20ks[i])/5
  sixth5k[i] <- (df$X30ks[i] - df$X25ks[i])/5
  seventh5k[i] <- (df$X35ks[i] - df$X30ks[i])/5
  eighth5k[i] <- (df$X40ks[i] - df$X35ks[i])/5
  last2k[i] <- (df$X42ks[i] - df$X40ks[i])/2.195
}
df$first5kpace <- first5k
df$second5kpace <- second5k
df$third5kpace <- third5k
df$fourth5kpace <- fourth5k
df$fifth5kpace <- fifth5k
df$sixth5kpace <- sixth5k
df$seventh5kpace <- seventh5k
df$eighth5kpace <- eighth5k
df$last2kpace <- last2k
```

Next, I would like to measure the speed difference in the first 5km and
the rest of the legs. However, I notice that the data does not make
sense for the 5km pace. Let’s look at the 10 fastest 5km
    time.

``` r
head(sort(df$X5ks, decreasing = FALSE), 10)/60
```

    ##  [1]  5.216667  5.783333  6.600000  6.916667  6.916667  7.216667  9.550000
    ##  [8] 10.300000 11.000000 11.216667

Please note that the world record for 5km is 12 minute. If the data is
accurate, it means that all these 10 runners are the new world record
holders. Since the data collection is wrong, I will measure the speed
difference between the fifth km to the 10th km and the rest of the legs.
I will explain more about this column in the EDA and model building.

# Adding Hubris columns

``` r
d10to15k <- d15to20k <- d20to25k <- c()
d25to30k <- d30to35k <- d35to40k <- d40to42k <- c()
for (i in 1:nrow(df)) {
  d10to15k[i] <- (df$third5kpace - df$second5kpace)/df$second5kpace*100
  d15to20k[i] <- (df$fourth5kpace - df$second5kpace)/df$second5kpace*100
  d20to25k[i] <- (df$fifth5kpace - df$second5kpace)/df$second5kpace*100
  d25to30k[i] <- (df$sixth5kpace - df$second5kpace)/df$second5kpace*100
  d30to35k[i] <- (df$seventh5kpace - df$second5kpace)/df$second5kpace*100
  d35to40k[i] <- (df$eighth5kpace - df$second5kpace)/df$second5kpace*100
  d40to42k[i] <- (df$last2kpace - df$second5kpace)/df$second5kpace*100
}
df$Hubris15 <- d10to15k
df$Hubris20 <- d15to20k
df$Hubris25 <- d20to25k
df$Hubris30 <- d25to30k
df$Hubris35 <- d30to35k
df$Hubris40 <- d35to40k
df$Hubris42 <- d40to42k
```

## Finally, exporting into a new csv file

``` r
write.csv(df, "/Users/wengliangchong/Desktop/RunTheData/MarathonData.csv", row.names = FALSE)
```
