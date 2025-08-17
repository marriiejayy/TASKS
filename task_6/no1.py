# Task 1 
# Fruit collector 
# Ask the user to enter 5 favorite fruits
Favorite_fruits = set()
Favorite_fruit =input("Dear user, kindly enter your 5 favorite fruits:( Note -ensure you put space):")
split_favorite_fruit = Favorite_fruit.split(",")

# Store them in a set
Favorite_fruits =set(split_favorite_fruit)

# Display the set 
print(Favorite_fruits)
print(type(Favorite_fruits))