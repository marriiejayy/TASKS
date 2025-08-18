#Create a list of items 
Items = ["Pillow","Sandal","Bag","Pot","Tissue paper"]
Prices = [2000, 5000, 15000, 24000, 1500]
#Start with an empty cart total
cart_total = 0


# Use assignment operators (+=) to add the price of some items into cart_total
cart_total += Prices[0] 
cart_total += Prices[1] 
cart_total += Prices[2]

# printing the list of items and the total price
print(f"Items: {Items}\nTotal Price: ₦{cart_total}")

