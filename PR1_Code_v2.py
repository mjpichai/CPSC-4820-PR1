
# File: test_tk.py

import tkinter as tk
from functools import partial
import csv

menu_file = "Panda Express Menu.csv"

window = tk.Tk()
window.title("Panda Express Allergen Aware Menu")
window.geometry('400x300')
window.config(bg='#84BF04')
frame = tk.Frame(window)
frame.pack()

# Storage arrays
menu_allergens = []
menu_item = []
good_items = []
bad_items = []

def showSafeFood(userAllergen):

    # Resets the list for the next allergen
    bad_items = []

    # Resets the list for the next allergen
    good_items = []

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


    text_box = tk.Text(
        window,
        height = 12,
        width = 40
    )

    text_box.pack(expand = True)
    text_box.insert('end', userAllergen)
    text_box.config(state = 'disabled')



with open(menu_file, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for cell in row:
            button = tk.Button(frame, text=cell, command=partial(showSafeFood,cell))
            button.pack(side = tk.LEFT)
        break
    


window.mainloop()