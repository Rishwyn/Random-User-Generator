import csv
import operator 
import pandas
  
#creating a pandas dataframe out of users.csv file
data = pandas.read_csv("users.csv") 

#sorting the data in the ascending order of first_name                   
data.sort_values(data.columns[1], axis=0, inplace=True) 
  
#exporting the csv file of sorted data
data.to_csv('users-sorted.csv', index=False) 


