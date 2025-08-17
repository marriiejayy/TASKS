# Task 2 Supermarket Price List

# Items
Item_1 = "Padlock"
Item_2 = "Tooth paste"
Item_3 = "Tissue paper"
Item_4 = "Pad"
Item_5 = "Perfume"

# Input prices
Padlock_price = int(input(f"Enter the price of {Item_1}: ₦"))
Tooth_paste_price = int(input(f"Enter the price of {Item_2}: ₦"))
Tissue_paper_price = int(input(f"Enter the price of {Item_3}: ₦"))
Pad_price = int(input(f"Enter the price of {Item_4}: ₦"))
Perfume_price = int(input(f"Enter the price of {Item_5}: ₦"))

# Create dictionary
Price = {
    Item_1: Padlock_price,
    Item_2: Tooth_paste_price,
    Item_3: Tissue_paper_price,
    Item_4: Pad_price,
    Item_5: Perfume_price
}

# Print price list
print("\n*****Items and their prices*****")
for item, price in Price.items():
    print(f"{item}: ₦{price}")

Updated_price = int(input(f"\nEnter the new price of {Item_1}: ₦"))
Price[Item_1] = Updated_price

print(f"\nThe new price of {Item_1} is: ₦{Updated_price}")

# Print updated price list
print("\n*****Updated price list*****")
for item, price in Price.items():
    print(f"{item}: ₦{price}")
