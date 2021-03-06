############################
### PROJECT REQUIREMENTS ###
############################

# FIPS # is a unique ID for each county

# Return the cumulative # of COVID cases for each county
## (This data is reported by day)

# Find the difference between each day for a single county

# If the county population is less than 500k, get the state daily difference

# First put it in
########################################
### IMPORTS NEEDED FOR ALL LIBRARIES ###
########################################

# General syntax to import specific functions in a library:
## from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions:
## import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib # only needed to determine Matplotlib version number

# Enable inline plotting
%matplotlib inline

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

################
### GET DATA ###
################

read_csv?
# Variable to hold the USA facts csv file location
Location1 = r'C:\Users\onebo\Documents\Non_System_Directories\Python_Training\PANDAS\covid_confirmed_usafacts.csv'

read_csv?
# Variable to hold the population csv file location
Location2 = r'C:\Users\onebo\Documents\Non_System_Directories\Python_Training\PANDAS\covid_county_population_usafacts.csv'

read_csv?
# Variable to hold the deaths csv file location
Location3 = r'C:\Users\onebo\Documents\Non_System_Directories\Python_Training\PANDAS\covid_deaths_usafacts.csv'

# For all data frames, the 1st line (0) is the header
# Argument is the name of the variable that holds the location of the file
ccs = pd.read_csv(Location1)
# Argument is the name of the variable that holds the location of the file
pops = pd.read_csv(Location2)
# Argument is the name of the variable that holds the location of the file
deaths = pd.read_csv(Location3)

######################
## HELPFUL COMMANDS ##
######################

# Add a new column to the data frame that will hold the values of column 4 * 4
ccs['TestColumn'] = ccs.iloc[:,4:5] * 4
ccs['TestColumn']

# Sums all values in each column from column 4 to 1000
ccs['Cases Total'] = ccs.iloc[:, 4:1000].sum(axis = 1)

# Displays rows based on cell value
ccs.loc[ccs['County Name'] == 'Los Angeles County']

# Displays the difference between two columns
ccs.iloc[:,101].subtract(ccs.iloc[:,100])

# Get the total populations
pops.groupby('County Name').population.sum()

# Plot data in a graph
%matplotlib inline
pops.groupby('County Name').population.agg(['sum']).plot(kind='bar')

# Sum population of counties
pops.groupby('County Name').population.agg(['sum'])
## OR to see the sum descending
pops.groupby('County Name').population.agg(['sum']).sort_values(by=['sum'],ascending=False)
## Counties with populations >= 500000
pops[pops.population >= 500000]['County Name']
### OR
pops.loc[pops.population >= 500000,'County Name']
### OR
pops.loc[pops.population >= 500000, :]

# Variable to create a data frame with just the rows from the pops data frame where the population is >= 500000
highPopFilter = pops.loc[pops.population >= 500000, :]
# Variable to create a data frame with just the rows from the pops data frame where the population is >= 500000 with just two columns
highPop = pops.loc[pops.population >= 500000, ['County Name','population']]
# Variable to create a data frame with just the first row from the pops data frame where the population is >= 500000
highPopFirst = highPop.head(1)
# Variable to create a data frame with just the first row from the pops data frame where the population is >= 500000 and just the County Name column
highPopFirst['County Name']

#################################
######## ACTUAL DEV CODE ########
#################################
# First field: County Name/sum of the country with the high population sum --
highPopCounty = pops.loc[pops.population >= 500000, ['County Name', 'population']]
highPopCountySorted = highPopCounty.groupby('County Name').population.agg(['sum']).sort_values(by=['sum'],ascending=False)
highPopCountySorted.head(1)

# Find the difference between two days for all counties
ccs['New'] = ccs['11/9/2020'] - ccs['11/8/2020']

# Find the difference between two days for all counties with populations >= 500K
ccs['New'] = ccs['11/9/2020'] - ccs['11/8/2020']

# Find the difference between two days for all states where the associated counties have populations < 500K
ccs['New'] = ccs['11/9/2020'] - ccs['11/8/2020']

### RESET NEW DATA FRAME ###
ccsCalc = 1
# Create a new data frame to show the:
## County Names
## Two days to compare
## Difference in the amount of cases for the days being compared
ccsCalc = pd.DataFrame()
# Add a column to the df with the county names
ccsCalc['County Name'] = ccs['County Name']
# Create variables for the days
day1 = '11/8/2020'
day2 = '11/9/2020'
# Add a column to the df with the cases of day 1
ccsCalc[day1] = ccs[day1]
# Add a column to the df with the difference of cases between day1 and day2
ccsCalc['Cases diff between days'] = ccs[day2] - ccs[day1]
# Add a column to the df with the cases of day2
ccsCalc[day2] = ccs[day2]
# Return data frame
ccsCalc

# ### RESET NEW DATA FRAME ###
# ccsCalc500k = 1
# # Create a new data frame to show the:
# ## County names where county population is greater than 500k
# ## Two days to compare from the counties with populations greater than 500k
# ## Difference in the amount of cases for the days being compared
# ccsCalc500k = pd.DataFrame()
# # Add a column to the df with the county names where county population is greater than 500k
# ccsCalc500k['County Name'] = pops[pops.population >= 500000]['County Name']
# # Add a column to the df with the sum of the county populations where county population is greater than 500k
# if ccs.iloc[:, 4:1000].sum(axis = 1) < 500000:
#     ccsState = pops[pops.State = ccs.State]['State']
# ccsCalc500k['County Population Sums'] =
# # Add a column to the df with the cases of day 1 where county population is greater than 500k
# ccsCalc500k[day1] =  pops[pops.population >= 500000][day1]
# # Add a column to the df with the difference of cases between day1 and day2 where county population is greater than 500k
# ccsCalc500k['Cases diff between days'] = pops[pops.population >= 500000][day2] - pops[pops.population >= 500000][day1]
# # Add a column to the df with the cases of day2 where county population is greater than 500k
# ccsCalc500k[day2] = pops[pops.population >= 500000][day2]
# # Return data frame
# ccsCalc500k
