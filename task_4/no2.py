# Task 2: Shopping List Manager
empty_list = []  # Create an empty list
list_1 = input("Enter your first shopping item: ") # Ask the user to enter 3 shopping items 
list_2 = input("Enter your second shopping item: ")
list_3 = input("Enter your third shopping item: ")
empty_list.append(list_1) #Add them to the list
empty_list.append(list_2)
empty_list.append(list_3)
print(",".join(empty_list)) # Display the list as a single string, separated by commas
