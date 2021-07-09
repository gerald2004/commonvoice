# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:29:40 2021

@author: Gerald
"""

#!/usr/bin/python3
#Importing the required packages
#import pandas as pd
#import os
#Loading the csv file
#data = pd.read_csv(r"C:\Users\Gerald\Desktop\DataScienceProject\sentences.csv")   

#Viewing the data in the csv
#print(data)

#Reading the input sentences by line using the readlines() function
#
#print(lines_seen)
def remove_duplication():
    lines_seen = set() # holds lines already seen
    with open(r"C:\Users\Gerald\Desktop\DataScienceProject\sentences.csv", "r+", encoding="utf-8") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i not in lines_seen:
                f.write(i)
                lines_seen.add(i)
                f.truncate()