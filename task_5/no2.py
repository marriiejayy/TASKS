# Task 2 

# Asking the user for 5 best friend"s name 
Bf_names = input("Dear user, kindly enter your best friends name:/nNote: ensure you put space")
Split_Bf_names = Bf_names.split(",")

# Store them in a tuple friends
Friends = tuple(Split_Bf_names)

# Print tuple in reversed order
print(Friends[::1])
