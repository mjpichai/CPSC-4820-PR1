
# File: PR1_Code_v7
# Description: A simple menu that helps the user determine which foods contain their allergens
# Project members: Mira, Mohan, Breanna

import tkinter as tk
from functools import partial
import csv

# Set up window
window = tk.Tk()
window.title("Panda Express Allergen Aware Menu")
window.geometry('800x300')
window.config(bg='#84BF04')

menu_file = "Panda Express Menu.csv"

mainFrame = tk.Frame(window)
mainFrame.pack()
allergensFrame = tk.Frame(window)
allergensFrame.pack()
sidesFrame = tk.Frame(window)
sidesFrame.pack()


# Storage arrays
menu_allergens = []
menu_item = []
good_items = []
bad_items = []
food_label_dict = {}

# Read in menu and create list of allergens
with open(menu_file, 'r+t') as csvfile:
  read_data = csv.reader(csvfile)

  menu_allergens = next(read_data)

  for data in read_data:
    menu_item.append(data)


# Determines what food is safe for a given allergen
def determineSafeFood(userAllergen):
    if(userAllergen == "clear"):
        resetUI()
    else:
        # Loop through menu allergens
        for ingredient in menu_allergens:
            # If the user allergen matches the menu allergen
            if userAllergen == ingredient:
                # Cycle through the menu items
                # Check whether the item contains the user's allergen
                for item in menu_item:
                    if item[menu_allergens.index(ingredient)] == '1':
                        bad_items.append(item[0])
                    else:
                        good_items.append(item[0])

        # Highlight foods to avoid 
        for label in food_label_dict:
            for badFood in bad_items:
                if(label == badFood):
                    food_label_dict[label].configure(bg="red",fg="white")
                
def resetUI():

    # Resets the list for the next allergen
    bad_items.clear()

    # Resets the list for the next allergen
    good_items.clear()

    # Clear UI
    for label in food_label_dict:
        food_label_dict[label].configure(bg="white",fg="black")


    
# Set up user interface
with open(menu_file, 'r') as csvfile:
    datareader = csv.reader(csvfile)

    message = tk.Label(mainFrame, text = "Select which allergens you want to avoid. Dishes you should avoid will appear as red.")
    message.pack(side = tk.TOP)

    # Create allergen buttons
    for row in datareader:
        for cell in row:
            button = tk.Button(allergensFrame, text=cell, command=partial(determineSafeFood,cell))
            button.pack(side = tk.LEFT)
        break

    # Create food label dict (allows for looping through food labels)
    for row in datareader:
        # Create each food label
        food_label_dict[row[0]] = tk.Label(sidesFrame, text=row[0])
        food_label_dict[row[0]].pack(side = tk.TOP)
        

            

window.mainloop()