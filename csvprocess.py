#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
# REFERENCE file_path = 'C:\\Users\\Sourabh\\Desktop\\com728\\Airbnb_UK_2022.csv'
def read_csv_file():
    file_path = input("Enter FILE PATH:")
    try:
        with open(file_path, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
            return data, file_path
    except:
        print(f"Error: Could not read file: {file_path}")
    return [], file_path

def retrieve_host_data(file_path):
    if not file_path:
        print("Error: No data found.")
        return
    with open(file_path, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
    # To retrieve the data from the dataset we need to create a new dict
    data_dict = {}
    for row in data:
        host_id = row['host_id']
        data_dict[host_id] = row

    # Take input from user for hostID
    host_id = input("Enter the host ID to retrieve data for: ")

    # Data to be accessed for the respective hostID using if else condition 
    if host_id in data_dict:
        host_data = data_dict[host_id]
        name = host_data['name']
        host_name = host_data['host_name']
        description = host_data['description']
        host_location = host_data['host_location']
        created_date = host_data['host_since']
        # Print all the data about the host ID
        print(f"Name of listing: {name}\n Host name: {host_name}\n Description: {description}\nHost location: {host_location}\nCreated date: {created_date}")
        return "HOPE YOU'RE HAPPY WITH THE DATA"
    else:
        # Print message to be displayed if hostID is not found 
        print(f"Sorry! No Data found regarding HostID:{host_id}")
    return "NO DATA"

def filter_by_location(file_path):
    # Take input from user for location
    location = input("What location are you looking for?: ")
    # Open the CSV file
    with open(file_path, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        filtered_data = []
        for row in reader:
            if row['host_location'] == location:
                filtered_data.append({'host_name': row['host_name'] , 'property_type': row['property_type'], 'price': row['price'], 'minimum_nights': row['minimum_nights'], 'maximum_nights': row['maximum_nights']})
        if filtered_data:
            print("Here is the data you requested for -")
            for row in filtered_data:
                print(row)
                print("\n")
            return "HOPE YOU'RE HAPPY WITH THE DATA"
        else:
            print(f"Sorry I was unable to find anything related to '{location}'")
    return "NO DATA"

def filter_by_property_type(file_path):
    # Take input from user for property type
    property_type = input('What Kind Of Property Are You Looking For ? -\n -rental unit \n -guesthouse \n -houseboat \n -townhouse \n -home \n -condo \n -loft \n -cottage \n -guest suite \n -boat \n -cabin \n -serviced apartment \n -bed and breakfast \n -Yurt \n -villa \n -farm stay \n -penthouse \n -casa particular \n -apartment \n -studio \n -hut \n -bungalow \n -treehouse \n')
    # Open the CSV file
    with open(file_path, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        filtered_data = []
        for row in reader:
            if row['property_type'] == property_type:
                filtered_data.append({'room_type': row['room_type'], 'accommodates': row['accommodates'], 'bathrooms': row['bathrooms_text'], 'bedrooms': row['bedrooms'], 'beds': row['beds']})
        if filtered_data:
            print("Here is the data you requested for -")
            for row in filtered_data:
                print(row)
                print("\n")
            return "HOPE YOU'RE HAPPY WITH THE DATA"
        else:
            print(f"Sorry, there seems to be no data available related to '{property_type}'")
    return "NO DATA"
        
        
def filter_by_host_location(file_path):
    location = input('Please provide a location:')
    host_name = input('Please Input a Name:')
    with open(file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        filtered_data = []
        for row in rows:
            if row['host_location'] == location and row['host_name'] == host_name:
                filtered_data.append({'acceptance_rate': row['host_acceptance_rate'], 'amenities': row['amenities'], 'instant_bookable': row['instant_bookable']})
        if filtered_data:
            print("HERE IS THE DATA YOU REQUESTED FOR:")
            for row in filtered_data:
                print("-"*125)
                print(f"Acceptance rate: {row['acceptance_rate']}\n")
                print(f"Amenities: {row['amenities']}\n")
                print(f"Instant bookable: {row['instant_bookable']}")
                print("\n")
            return "HOPE YOU'RE HAPPY WITH THE DATA"
        else:
            print(f"Sorry !!! No information related to '{location}' and '{host_name}'")
    return "NO DATA"

        
# When i created it i wanted to test it and hence i called CSV file data and file path using read_csv_file() function and now im leaving it as commented
data, file_path = read_csv_file()

# retrieve_host_data() function
retrieve_host_data(file_path)

#filter data by location using filter_by_location() function
filter_by_location(file_path)

#filter data by property type using filter_by_property_type function
filter_by_property_type(file_path)

#filter by host location using filter_by_host_location function
filter_by_host_location(file_path)


# In[ ]:





# In[ ]:




