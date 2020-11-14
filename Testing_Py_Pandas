#USAFacts COVID
#
# Cumulative # of Covid cases for each county
# reported by day
#
#Using both files
#FIPS # is a unique ID for each county
#Find the difference in each day 
#
#County file has # for each day
#
#Difference from day to day for a single county
#
#If the county population is less than 500k, get the state daily difference
#
#Look up PANDAs

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
%matplotlib inline

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

low_memory=False
# GET DATA
read_csv?

Location = r'C:\Users\onebo\Documents\Non_System_Directories\Python_Training\PANDAS\covid_confirmed_usafacts.csv'

# 1st line is header
# Argument is the name of the variable that holds the location of the file
countyCases = pd.read_csv(Location)
countyCases

# Numbers for header
#countyCases = pd.read_csv(Location, header=None)
#countyCases


# Make your own header
#countyCases = pd.read_csv(Location, names=['Names','Births'])
#countyCases

# Sort the dataFrame by a column
# Argument is the column name
Sorted = countyCases.sort_values(['11/3/2020'], ascending=False)
# Show the top row as sorted
Sorted.head(1)


grouped = countyCases.groupby('County Name')

for name,group in grouped:
    print(name)
	
test = countyCases.groupby('County Name')['1/22/2020'].sum()

#grouped = countyCases.groupby('County Name').cumcount()
#grouped = countyCases.groupby('County Name').cumsum(float('countyFIPS'))
#print(grouped)
#for name,group in grouped:     print(name)

# test = countyCases.groupby('County Name')['1/22/2020','5/12/2020'].sum().sort_values(by='5/12/2020')
# print(test)

# subsetCC = countyCases.sum(axis=1)
# print(subsetCC)

compareTwoDays = countyCases.loc[countyCases['County Name'] == 'Los Angeles County']
#print(compareTwoDays)

#countyCases.columns.

countyCases[countyCases.countyFIPS == 50926425]

countyCases.iloc[:,4:1000]

# First field: Population of each county
# 
