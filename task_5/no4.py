# Task 4

# Ask for user profile
First_name = input("Dear user, kindly input your first name: ") 
Age = input("enter your age: ")
Favorite_color = input("enter your favorite color: ")
Home_town = input(" enter your hometown:")

# Store in a tuple 
User_profile = (First_name, Age, Favorite_color, Home_town) # store in a tuple
First_name, Age, Favorite_color, Home_town = User_profile  #unpack into variables 

# print and use escape sequence
print("\n USER PROFILE ")
print(f"First name:\t{First_name}")
print(f"Age:\t\t{Age}")
print(f"Favorite Color:\t{Favorite_color}")
print(f"Home Town:\t{Home_town}")