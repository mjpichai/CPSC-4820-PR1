# Allergery Menu PR1
# Mira, Mohan, Breanna

import csv
menu_file = "Panda Express Menu.csv"

menu_allergens = []
menu_item = []
user_allergens = []
good_items = []
bad_items = []

# Reading data from CSV File
# Storing data to arrays
with open(menu_file, 'r+t') as csvfile:
  read_data = csv.reader(csvfile)

  menu_allergens = next(read_data)

  for data in read_data:
    menu_item.append(data)

print('The following ingredients are potential allergens: ' + '\n'.join(allergen for allergen in menu_allergens))

num_allergens = int(input("Enter the number of allergens you have: "))

print("Please enter your allergens in all caps")
for i in range(0, num_allergens):
  print("Allergen ", i+1)

  allergy = str(input())

  user_allergens.append(allergy)

# Loop through user allergens
for i in user_allergens:
  # Loop through menu allergens
  for j in menu_allergens:
    # If the user allergen matches the menu allergen
    if i == j:
      # Cycle through the menu items
      for item in menu_item:
        if item[menu_allergens.index(j)] == '1':
          bad_items.append(item[0])
        else:
          good_items.append(item[0])

  # Prints the bad menu items for that allergen
  print(i + " Red:")
  print(bad_items)

  # Resets the list for the next allergen
  bad_items = []

  # Prints the good menu items for that allergen
  print(i + " Green")
  print(good_items)

  # Resets the list for the next allergen
  good_items = []
        



    
      
#   print('Red: ')

# 

# print(user_allergens)
  











### end ###