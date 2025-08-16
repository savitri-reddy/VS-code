# IMPORT LIBRARY
import pandas as pd     # for DF
import numpy as np      # FOR MULTI DIMENTIONAL ARRY(ND ARRAY)
import matplotlib.pyplot as plt    # VISUALIZATION
import seaborn as sns                 # FOR STATISTICAL
import scipy.stats as stats           # SCIPY --> one of the statistical library to hanle statistican
                                                   #fun probability distribution summary, frquency all things

# create the dataset

np.random.seed(42)          # we need to generate random num using np,every time numbers changed i don't want to change my number
                            # random number won't be generate
data = {
    'product_id' : range(1,21),
    'product_name' : [f'product{i}' for i in range(1,21)],
    'category': np.random.choice(['Electronic','Clothing','Home','Sports'], 20),
    'units_sold' : np.random.poisson(lam=20,size=20),
    'sales_date' : pd.date_range(start = '2023-01-01' , periods=20, freq='D'),
} 
sales_data = pd.DataFrame(data)
 
# display the dataset
print('Sales Data:')
print(sales_data)
                        



# Sava The DtaFrame to csv File(in oour)
sales_data.to_csv('sales_data.csv' , index=False)        # index=False --> no index column will be created      


# now i want to know location where it stored csv file

import os
os.getcwd()                                                      # get current working directory


  # descriptive stats     
# descriptive stats always deal with numbers so frst u go for (units_sold) column
  
descriptive_stats = sales_data['units_sold'].describe()  

print("\nDescriptive statistics for 'units_sold':")
print(descriptive_stats)

mean_sales     = sales_data['units_sold'].mean()
median_sales   = sales_data['units_sold'].median()
mode_sales     = sales_data['units_sold'].mode()[0]
variance_sales = sales_data['units_sold'].var()
std_deviation_sales = sales_data['units_sold'].std()


category_stats = sales_data.groupby('category')['units_sold'].agg(['sum','mean','std']).reset_index()


# display results

print('\n Statistical Analysis:')
print(f"Mean Units Sold : {mean_sales}")
print(f'Median Units Sold : {median_sales}')
print(f'Mode Units Sold : {mode_sales}')
print(f'Variance of Units Sold : {variance_sales}')
print(f'Standard Deviation of Units Sold : {std_deviation_sales}')
print('\nCategory Statistics')
print(category_stats)



# inferential stats

Confidence_level = 0.95    #95%                                             
degrees_freedom = len(sales_data['units_sold']) - 1

sample_mean = mean_sales

sample_standard_error = std_deviation_sales / np.sqrt(len(sales_data['units_sold']))


# t-score                                                               # in this code entire , i need to find out the range of unit sold at 95% confidence level


t_score = stats.t.ppf((1 + Confidence_level)/2 , degrees_freedom)
margin_of_error = t_score * sample_standard_error

confidence_interval = (sample_mean - margin_of_error , sample_mean + margin_of_error)
print("\n Confidence Interval for Mean of Units sold")
print(confidence_interval)




t_statistic, p_value = stats.ttest_1samp(sales_data['units_sold'], 20)

print('\n Hypothesis Testing (t-test):')
print(f"T-statistics: {t_statistic}, p-value: {p_value}")

if p_value < 0.05:
    print('Reject the null hypothesisi: The mean units sold is different from 20')
else:
    print('fail to reject the null hypothesis: the mean units sold is not different from 20')
    
    
    
# visualization 

sns.set(style = 'whitegrid')

# plot distribution of units sold
plt.figure(figsize=(10,6))
sns.histplot(sales_data['units_sold'], bins=10, kde=True)
plt.title("Distribution of Units sold")
plt.xlabel('Unit Sold')
plt.ylabel("Frequency")
plt.axvline(mean_sales, color = 'red', linestyle='--', label='Mean')
plt.axvline(median_sales, color = 'green', linestyle='--', label='Median')
plt.legend()
plt.show()


# Boxplot for units sold by catogeory

plt.figure(figsize=(10,6))
sns.boxplot(x='category', y='units_sold', data=sales_data)
plt.title("Boxplot of Units Sold by Category")
plt.xlabel('Category')
plt.ylabel('Units Sold')
plt.show()




# BAR plot for total units  sold by catogory

plt.figure(figsize=(10,6))
category_stats = category_stats.groupby('category')['units_sold'].sum().reset_index()
plt.title("Total Units Sold by Category")
plt.xlabel('Category')
plt.ylabel('Total Units Sold')
plt.show()    
    
    
    
    
    
    
                          