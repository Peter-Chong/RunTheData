Data Cleaning
================
Peter Chong

The data I scrapped was according to age group. So for a specific year,
I will have 15 age group x 2 gender. A total of 30 csv file per year.

``` r
#Read csv files
df <- read.csv("/Users/wengliangchong/Desktop/MarathonScraper/Marathon15_F.csv", header = T,
                stringsAsFactors = FALSE)
newdf <- read.csv("/Users/wengliangchong/Desktop/MarathonScraper/Marathon15_F15.csv", header = T,
                  stringsAsFactors = FALSE)
```

``` r
#Remove rows with incomplete data
newdf <- newdf[!(newdf$X40k=="" | newdf$X35k=="" | newdf$X30k=="" | newdf$X25k=="" | newdf$X20k=="" |
                   newdf$X15k=="" | newdf$X10k=="" | newdf$X5k=="" | newdf$Clock.Time=="" | newdf$Net.Time==""), ]
df <- df[!(df$X40k=="" | df$X35k=="" | df$X30k=="" | df$X25k=="" | df$X20k=="" |
                   df$X15k=="" | df$X10k=="" | df$X5k=="" | df$Clock.Time=="" | df$Net.Time==""), ]
new <- rbind(df, newdf)
```

``` r
#Export into a new csv file
write.csv(new, "/Users/wengliangchong/Desktop/MarathonScraper/Marathon15_F.csv", row.names = FALSE)
```

I repeated the above code for every gender. Ended up with 2 gender x 4
years. A total of 8 files. Next, I add a new Gender column for every csv
file and export it.

``` r
#Read csv files
df_m <- read.csv("/Users/wengliangchong/Desktop/MarathonScraper/Marathon15_M.csv", header = T,
                stringsAsFactors = FALSE)
df_f <- read.csv("/Users/wengliangchong/Desktop/MarathonScraper/Marathon15_F.csv", header = T,
                stringsAsFactors = FALSE)
```

``` r
#Add Gender columns
df_m <- cbind(rep("Male", nrow(df_m)), df_m)
df_m <- df_m[,c(2,3,4,1,5,6,7,8,9,10,11,12,13,14,15,16,17,18)]
colnames(df_m)[4] <- "Gender"

df_f <- cbind(rep("Female", nrow(df_f)), df_f)
df_f <- df_f[,c(2,3,4,1,5,6,7,8,9,10,11,12,13,14,15,16,17,18)]
colnames(df_f)[4] <- "Gender"
```

``` r
#Bind the two csv file into one
new <- rbind(df_m, df_f)
```

``` r
#Export into a new csv file
write.csv(new, "/Users/wengliangchong/Desktop/RunTheData/Marathon15.csv", row.names = FALSE)
```

Lastly, I add a year column and merge all 4 years together.

``` r
#Read csv files
df <- read.csv("/Users/wengliangchong/Desktop/RunTheData/MarathonData.csv", header = T,
                stringsAsFactors = FALSE)
df_new <- read.csv("/Users/wengliangchong/Desktop/RunTheData/Data/Marathon18.csv", header = T,
                stringsAsFactors = FALSE)
```

``` r
#Add Year columns
df_new <- cbind(rep("2018", nrow(df_new)), df_new)
df_new <- df_new[,c(2,3,4,5,1,6,7,8,9,10,11,12,13,14,15,16,17,18,19)]
colnames(df_new)[5] <- "Year"
```

``` r
#Bind the two csv file into one
new <- rbind(df, df_new)
```

``` r
#Export into a new csv file
write.csv(new, "/Users/wengliangchong/Desktop/RunTheData/MarathonData.csv", row.names = FALSE)
```
