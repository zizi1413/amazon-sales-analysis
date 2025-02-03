
#import helpful analytics libraries
import pandas as pd
import numpy as np  

#Read the file and read the first and last five rows
data = pd.read_csv('/Users/zohrehsamieekadkani/Desktop/python-files/Abgabe/amazon.csv')    
print(data.head())

#It cleans and converts specific columns in a Pandas DataFrame (data) from strings containing symbols (₹, %, ,, etc.) into proper numeric values.
for col in ['discounted_price',	'actual_price',	'discount_percentage','rating',	'rating_count']:
  data[col]=data[col].astype(str).str.replace('₹','').str.replace('%','').str.replace(',','').str.replace('nan','0')
  data[col] = pd.to_numeric(data[col].str.replace('[^0-9.]','',regex=True),errors='coerce').fillna(0)


print(data[['discounted_price','actual_price','discount_percentage']])
print(data[['discounted_price','actual_price','discount_percentage']].describe())


print(data.tail())
print(data.columns)
print(data.isnull().sum())
print(data.duplicated().sum())

#The function data.nunique() returns the number of unique values in each column of the Pandas DataFrame (data).
print(data.nunique())

#information about the DataFrame
print(data.info())
print(data.shape)

#summary statistics (count, mean, std, min, max, etc.) for numeric columns.
print(data[['discounted_price','actual_price','discount_percentage']].describe())


#Returns the highest actual_price in the dataset.
print(data['actual_price'].max())

#Counts how many times each rating appears in the dataset.
print(data['rating'].value_counts())

#Sort by rating_count and Show Top 10 Products
print(data.sort_values(by='rating_count',ascending=False).head(10)[['product_name','rating','rating_count']])


# Calculate Average rating for Each category
print(data.groupby('category')['rating'].mean())


#Count Number of Products per category
print(data['category'].value_counts())


# Find Categories with Highest Average Discount
print(data.groupby('category')['discount_percentage'].mean().sort_values(ascending=False))


#Find Categories with Highest Average Rating
print(data.groupby('category')['rating'].mean().sort_values(ascending=False))