#Task 5
# Modify tuple indirectly 
User_items = input("Dear user, kindly enter three items for your shopping list/Note: ensure you put space")
split_user_items = User_items.split(",")
tupple_01 = tuple(split_user_items)
print(tupple_01)

#store in a tuple called shopping list
shopping_list = list(tupple_01) 
print(shopping_list) 

#Convert it to a list and ask for two more items to add
new_user_item_01 =input("enter new user item ") 
new_user_item_02 =input("enter new user item")

shopping_list.append(new_user_item_01)
shopping_list.append(new_user_item_02)

# Convert back to a tuple 
tupple_01 = tuple(shopping_list) 

# Print the updated list using join() to display items separated by " | "
print("My items: "," | ".join(shopping_list)) 