#Task5 Store Inventory Update
# Create a dictionary called store with items and their available quantities
Store = {"Book": 50, "Pencil": 50, "Eraser": 20}


# Ask the user to input the item and quantity they want to buy 
User_item= (input("Enter the item you want to buy: ")).title()
user_quantity = int(input("Enter the quantity you want to purchase: "))

# Use the assignment operator -= to update (reduce) the item quantity in the dictionary.

Store[User_item] -= user_quantity

# Print the dictionary before and after purchase
print(f"Before purchase: {Store}")
print(f"After purchase: {Store} ")

 

