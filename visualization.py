#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# REFERENCE file_path = 'C:\\Users\\Sourabh\\Desktop\\com728\\Airbnb_UK_2022.csv'

def bedrooms_piechart(df):
    sorted_bedrooms_group_piechart = df.groupby('bedrooms').size().sort_values()
    piechart_bedrooms_list = sorted_bedrooms_group_piechart.index.tolist()
    number_bedrooms_list = sorted_bedrooms_group_piechart.tolist()

    fig = plt.figure(figsize=(10,99))
    plt.pie(number_bedrooms_list, labels=piechart_bedrooms_list, autopct='%1.1f%%')
    plt.title("PROPORTION OF NO.OF BEEDROOMS")
    plt.legend(loc="best", bbox_to_anchor=(2, 1.5))
    plt.show()
    return

def room_type_counts(df):
    # group the DataFrame by room type and count the number of listings 
    room_type_counts = df.groupby('room_type').count()['host_id']
    # create a bar chart of the counts
    room_type_counts.plot(kind='bar')
    plt.xlabel('Room Type')
    plt.ylabel('Number of Listings')
    plt.title('Number of Listings by Room Type')
    plt.show()
    return

def accommodates_vs_price_scatterplot(df):
    plt.scatter(df['accommodates'], df['price'], s=50)
    plt.title('Accommodates vs. Price')
    plt.xlabel('Accommodates')
    plt.ylabel('Price')
    plt.show()
    return

def airbnb_price(df):
    df['host_since'] = pd.to_datetime(df['host_since'])

    # Split data by year
    year_2019 = df[df['host_since'].dt.year == 2019]
    year_2020 = df[df['host_since'].dt.year == 2020]
    year_2021 = df[df['host_since'].dt.year == 2021]
    year_2022 = df[df['host_since'].dt.year == 2022]


    # Compute price per month for each year
    price_2019 = year_2019.groupby(year_2019['host_since'].dt.month)['price'].sum()
    price_2020 = year_2020.groupby(year_2020['host_since'].dt.month)['price'].sum()
    price_2021 = year_2021.groupby(year_2021['host_since'].dt.month)['price'].sum()
    price_2022 = year_2022.groupby(year_2022['host_since'].dt.month)['price'].sum()

    fig, axs = plt.subplots(2,2,figsize=(15,11))

    # Plot data for 2019
    axs[0,0].plot(price_2019.index, price_2019)
    axs[0,0].set_title('Airbnb Price in 2019')
    axs[0,0].set_xlabel('Month')
    axs[0,0].set_ylabel('Price')

    axs[0,1].plot(price_2020.index, price_2020)
    axs[0,1].set_title('Airbnb Price in 2020')
    axs[0,1].set_xlabel('Month')
    axs[0,1].set_ylabel('Price')

    axs[1,0].plot(price_2021.index, price_2021)
    axs[1,0].set_title('Airbnb Price in 2021')
    axs[1,0].set_xlabel('Month')
    axs[1,0].set_ylabel('Price')

    # Plot data for 2022
    axs[1,1].plot(price_2022.index, price_2022)
    axs[1,1].set_title('Airbnb Price in 2022')
    axs[1,1].set_xlabel('Month')
    axs[1,1].set_ylabel('Price')

    # Adjust spacing between subplots
    plt.tight_layout()

    # Display the plots
    plt.show()
    return

def beds_pie_chart(df):
    sorted_beds_group_piechart = df.groupby('beds').size().sort_values()
    piechart_beds_list = sorted_beds_group_piechart.index.tolist()
    number_beds_list = sorted_beds_group_piechart.tolist()

    fig = plt.figure(figsize=(10, 8))

    plt.pie(number_beds_list, labels=piechart_beds_list, autopct='%1.1f%%')
    plt.title("Proportion of Number of Beds")

    plt.legend(loc="best", bbox_to_anchor=(1.5, 1))

    plt.show()    
    return


# In[ ]:





# In[ ]:




