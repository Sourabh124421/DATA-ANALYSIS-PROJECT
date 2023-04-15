#!/usr/bin/env python
# coding: utf-8

# In[97]:


from IPython.display import Markdown

def heading():
    display(Markdown("<h1><span style='font-size:48px'>Welcome to DATA PROJECT *-*</span></h1>"))


def welcome_message(): 
    print("                                \033[7mHOPE YOU'RE HAVING A GREAT DAY!\033[0m\n\n")
    print("*" * 100)
    print("*" * 100)  


def menu():
    print("\033[31m\nPlease Select One Option From The Menu:\n\033[0m")
    menu_selection=input(" 1.CSV Process \n\n 2.Pandas Process \n\n 3.Visualization \n\n 9.Abort\n\n")
    print(f"\033[32mYou have selected:\033[0m{menu_selection}")
    print("*" * 100) 
    try:
        return int(menu_selection)
    except:
        return 0
    


def csvprocess_menu():
    print("\033[31m\nPlease Select One Option From The CSV Processes Listed:\n\033[0m")
    csvmenu_selection=input(" 1.Get Information using HOST ID \n\n 2.Get Information related to LOCATION \n\n 3.Get Information about a specific PROPERTY TYPE \n\n 4.Get Information using HOST and LOCATION \n\n 5.Press 5 to Dislay the file path\n\n")
    print(f"\033[32mYou have selected:\033[0m{csvmenu_selection}")
    print("*" * 100) 
    try:
        return int(csvmenu_selection)
    except:
        return 0 

def pandasprocess_menu():
    print("\033[31m\nPlease Select One Option From The Pandas Processes Listed:\n\033[0m")
    pandasmenu_selection=input(" 1.Get Top 10 Amenities that hosts provide \n\n 2.Get Aerage price of stay in each location\n\n 3.Get Average review scores rating for each location \n\n 4.Get Average review cleanliness score for each location\n\n")
    print(f"\033[32mYou have selected:\033[0m{pandasmenu_selection}")
    print("*" * 100) 
    try:
        return int(pandasmenu_selection)
    except:
        return 0
    
def visualization_menu():
    print("\033[31m\nPlease Select One Option From The Visualization Processes Listed:\n\033[0m")
    visualization_selection=input(" 1.Get Pie Chart for Proportion of Number of Bedrooms \n\n 2.Get Bar Chart for Number of listings for Each Room Type \n\n 3.Get Scatter Plot for Relationship between Accommodates and Price \n\n 4.Get Subplots Line Chart for Airbnb prices from 2019 - 2022 \n\n 5.Get PieChart for Proportion of Number of Beds \n\n")
    print(f"\033[32mYou have selected:\033[0m{visualization_selection}")
    print("*" * 100) 
    try:
        return int(visualization_selection)
    except:
        return 0
    
def error():
    display (Markdown("I AM SORRY +_+ I GUESS THERE WAS AN ERROR. HOPE YOU DONT MIND RETRYING !"))
   


# In[ ]:




