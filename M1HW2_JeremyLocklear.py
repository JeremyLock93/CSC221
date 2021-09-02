# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:38:03 2021

@author: Super
"""
# =============================================================================
# # Creating and Mainpulating Dataframes
# # 09/01/21
# # CSC221 M1HW2 – DataFrame
# # Jeremy Locklear
# 
# =============================================================================
# The purpose of this program is the create a dataframe using the pandas library
# By creating a dataframe dictionary the program shows the different results,
# of mainpulation of the data through various means.
# =============================================================================




import pandas as pd


temperatures = {'Maxine': [75, 80, 66], 'James': [68, 86, 70], 'Amanda': [81, 95, 78]}

temp = pd.DataFrame(temperatures, index=['Morning', 'Afternoon', 'Evening'])

print("Dataframe Temperatures")
'''This is the creation of the dataframe for the temperatures with the index'''
print(temp)
print()

print("Maxine's Temperature Readings")
print(temp["Maxine"])
print()

print("Temperature readings for the Morning")
print(temp.loc['Morning'])
print()

print("Temperature Readings for both Morning and Evening")
print(temp.loc[['Morning', 'Evening']])
print()

print("Temperature selection of Maxine and Amadnda's Readings")
print(temp[["Maxine", "Amanda"]])
print()

print("Tempearture Readings from using Morning and Afternoon for Maxine and Amanda")
print(temp.loc[['Morning', 'Afternoon'], ['Maxine', 'Amanda']])
print()

print("Using the Describe Method to show the statsitics")
print(temp.describe())
print()

print("Transposed the Dataframe")
print(temp.T)
print()

print("Sorted the Colomuns in Alphabetical Order")
print(temp.sort_index(axis=1))
