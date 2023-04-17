#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# REFERENCE file_path = 'C:\\Users\\Sourabh\\Desktop\\com728\\Airbnb_UK_2022.csv'
def get_top_amenities(df):
    amenities_count = {}
    for index, row in df.iterrows():
        amenities = row['amenities'].replace('{', '').replace('}', '').replace('"', '').split(',')
        for amenity in amenities:
            if amenity not in amenities_count:
                amenities_count[amenity] = 1
            else:
                amenities_count[amenity] += 1
    top_amenities = sorted(amenities_count.items(), key=lambda x: x[1], reverse=True)[:10]
    top_amenities_dict = {amenity: count for amenity, count in top_amenities}
    return top_amenities_dict

def get_avg_price_by_location(df):
    avg_price_by_location = df.groupby('host_location')['price'].mean()
    return avg_price_by_location

def get_avg_review_score_by_location(df):
    avg_review_score_by_location = df.groupby('host_location')['review_scores_rating'].mean()
    return avg_review_score_by_location

def get_avg_review_scores_cleanliness_by_location(df):
    avg_review_scores_cleanliness_by_location = df.groupby('host_location')['review_scores_cleanliness'].mean()
    return avg_review_scores_cleanliness_by_location

# # When i created the file i wanted to test it so i Called it and print and hence now its commented 

# top_amenities_dict = get_top_amenities(df)
# print("Top 10 most popular amenities or features:")
# for amenity, count in top_amenities_dict.items():
#     print(f"{amenity}: {count}")

# avg_price_by_location = get_avg_price_by_location(df)
# print("\nAverage price of stay in each location:")
# print(avg_price_by_location)

# avg_review_score_by_location = get_avg_review_score_by_location(df)
# print("\nAverage review scores rating for each location:")
# print(avg_review_score_by_location)

# avg_review_scores_cleanliness_by_location = get_avg_review_scores_cleanliness_by_location(df)
# print("\nAverage review cleanliness score for each location:")
# print(avg_review_scores_cleanliness_by_location)


# In[ ]:





# In[ ]:




