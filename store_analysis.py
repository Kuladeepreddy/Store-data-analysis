import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("QVI_data.csv")
data.head()
print(" ")
#Data information
print("1.Basic Data Information")
print(data.info())
print(" ")

#Checking for missing values
print("2.Missing values")
print(data.isnull().sum())
print(" ")

#Calculating for basic stastitics
print("3.Basic stats")
print(data.describe())
print(" ")

#FOR STORE 77
#To get the sum of sales 
start_index = data[data['STORE_NBR'] == 77].index.min()
end_index = data[data['STORE_NBR'] == 77].index.max()
sum_of_sales_77 = data.loc[start_index:end_index,'TOT_SALES'].sum()
print("SUM OF SALES FOR STORE 77 IS:",sum_of_sales_77)

#TO GET NUMBER OF CUSTOMERS
store_77_rows = data.loc[start_index:end_index]
total_customers_store_77 = store_77_rows['LYLTY_CARD_NBR'].nunique()
print("TOTAL NUMBER OF CUSTOMERS FOR STORE 77 IS:", total_customers_store_77)

#TO GET AVERAGE TRANSACTIONS
total_transactions = data['TXN_ID'].nunique()
total_customers = data['LYLTY_CARD_NBR'].nunique()
average_transactions_per_customer_77 = total_transactions / total_customers
print("AVERAGE NUMBER OF TRANSACTIONS FOR STORE 77 ARE:",average_transactions_per_customer_77)
print(" ")


#FOR STORE 86
#To get the sum of sales 
start_index = data[data['STORE_NBR'] == 86].index.min()
end_index = data[data['STORE_NBR'] == 86].index.max()
sum_of_sales_86 = data.loc[start_index:end_index,'TOT_SALES'].sum()
print("SUM OF SALES FOR STORE 86 IS:",sum_of_sales_86)

#TO GET NUMBER OF CUSTOMERS
store_86_rows = data.loc[start_index:end_index]
total_customers_store_86 = store_86_rows['LYLTY_CARD_NBR'].nunique()
print("TOTAL NUMBER OF CUSTOMERS FOR STORE 86 IS:", total_customers_store_86)

#TO GET AVERAGE TRANSACTIONS
total_transactions = data['TXN_ID'].nunique()
total_customers = data['LYLTY_CARD_NBR'].nunique()
average_transactions_per_customer_86 = total_transactions / total_customers
print("AVERAGE NUMBER OF TRANSACTIONS FOR STORE 86 ARE:",average_transactions_per_customer_86)
print("  ")


#FOR STORE 89
#To get the sum of sales 
start_index = data[data['STORE_NBR'] == 89].index.min()
end_index = data[data['STORE_NBR'] == 89].index.max()
sum_of_sales_89 = data.loc[start_index:end_index,'TOT_SALES'].sum()
print("SUM OF SALES FOR STORE 89 IS:",sum_of_sales_89)

#TO GET NUMBER OF CUSTOMERS
store_89_rows = data.loc[start_index:end_index]
total_customers_store_89 = store_77_rows['LYLTY_CARD_NBR'].nunique()
print("TOTAL NUMBER OF CUSTOMERS FOR STORE 89 IS:", total_customers_store_89)

#TO GET AVERAGE TRANSACTIONS
total_transactions = data['TXN_ID'].nunique()
total_customers = data['LYLTY_CARD_NBR'].nunique()
average_transactions_per_customer_89 = total_transactions / total_customers
print("AVERAGE NUMBER OF TRANSACTIONS FOR STORE 89 ARE:",average_transactions_per_customer_89)

#TO DRAW A BAR GRAPH BETWEEN TOTAL SALES
store_numbers = [77, 86, 89]
sum_of_sales_list = [sum_of_sales_77, sum_of_sales_86, sum_of_sales_89]

plt.bar(store_numbers, sum_of_sales_list)
plt.yscale('log')
plt.xlabel('Store Number')
plt.ylabel('Sum of Sales')
plt.title('Comparision of Sales between stores 77, 86, and 89')
plt.show()

#TO PLOT COMPARISION OF CUTOMERS 
plt.plot(store_numbers, [total_customers_store_77, total_customers_store_86, total_customers_store_89], marker='o',linestyle='--',color='g')
plt.xlabel('Store Number')
plt.ylabel('Total Customers')
plt.title('Comparision of Customers from Stores 77, 86, and 89')
plt.tight_layout()
plt.show()

kong = [average_transactions_per_customer_77,average_transactions_per_customer_86,average_transactions_per_customer_89]
plt.bar(store_numbers,kong)
#plt.yscale('log')
plt.ylim(3.5)
plt.xlabel('Store Number')
plt.ylabel('Avg transactions')
plt.title('Comparision of Sales between stores 77, 86, and 89')
plt.show()