#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 01:04:05 2020

@author: wengliangchong
"""

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import pandas as pd
import time

df = []

def get_running_data():
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="/Users/wengliangchong/Desktop/MarathonScraper/chromedriver", options=options)
    driver.set_window_size(1120, 1000)
    
    #Step 1: Change url
    url = 'https://www.trackshackresults.com/lamarathon/results/2015_Marathon/mar_results.php?Link=2&Type=2&Div=ZE&Ind=31'
    driver.get(url)
    #Click search
    driver.find_element_by_xpath("//*[@id=\"f1\"]/p[1]/table/tbody/tr/td[2]/input").click()
    time.sleep(0.5)
    #Step 2: Change range based on number of participant in the age group
    for i in range(3, 5):      
        name = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[2]").text
        bib = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[3]").text
        age = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[4]").text
        place = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[5]").text
        genderplace = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[6]").text
        divplace = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[1]").text
        time5k = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[7]").text
        time10k = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[8]").text
        time15k = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[9]").text
        time20k = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[10]").text
        time25k = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[11]").text
        time30k = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[12]").text
        time35k = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[13]").text
        time40k = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[14]").text
        clocktime = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[15]").text
        nettime = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[16]").text
        hometown = driver.find_element_by_xpath("//*[@id=\"f1\"]/p[2]/table/tbody/tr["+str(i)+"]/td[17]").text
        
        df.append({"Name":name,
                   "Bib":bib,
                   "Age":age,
                   "Position":place,
                   "Gender Position":genderplace,
                   "Division Position":divplace,
                   "5k":time5k,
                   "10k":time10k,
                   "15k":time15k,
                   "20k":time20k,
                   "25k":time25k,
                   "30k":time30k,
                   "35k":time35k,
                   "40k":time40k,
                   "Clock Time":clocktime,
                   "Net Time":nettime,
                   "Hometown":hometown
                   })
        print(i)
    
    return pd.DataFrame(df)

#step 3: Change desired file name
get_running_data().to_csv('Marathon15_F15.csv', index = False)