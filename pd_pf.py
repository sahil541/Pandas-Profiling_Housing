# Coded by Md Sahil Kaif

# pip install pandas
import pandas as pd 

# pip install pandas-profiling
from pandas_profiling import ProfileReport

# read .csv file and store in variable
df = pd.read_csv('housing.csv')
print(df)

# Make profile report of .csv file
profile = ProfileReport(df)

# Convert the output in html
profile.to_file(output_file="housing.html")