######################
## HELPFUL COMMANDS ##
######################

# Sums all values in each column from column 4 to 1000
countyCases['Cases Total'] = countyCases.iloc[:, 4:1000].sum(axis = 1)

# Displays rows based on cell value
countyCases.loc[countyCases['County Name'] == 'Los Angeles County']

# Displays the difference between two columns
ccs.iloc[:,101].subtract(ccs.iloc[:,100])

# Get the total populations
pops.groupby('County Name').population.sum()

#######################
######## TO DO ########
#######################

# First field: Population of a county
