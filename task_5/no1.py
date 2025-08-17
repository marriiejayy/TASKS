# Task 1
# Ask the user to enter three favorite Nih=gerian dishes

dish_1 = input("enter  your first favorite dish") #Ask the user to enter three favorite Nigerian dishes (one at a time)
dish_2 = input("enter your second favorite dish")
dish_3 = input("enter your third favorite dish")

# Store them in a tuple dishes
dishes = (dish_1, dish_2, dish_3) 
print(dishes)

#Print using n escpe sequence
print(f"{dish_1}\n{dish_2}\n{dish_3}") 
print(type(dishes))
  