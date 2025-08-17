# Task 4: Name Organizer
empty_list = [] # Ask the user to enter 5 names (separated by spaces)
name_1 = input("Enter first name: ").lower() #Convert all names to lowercase
name_2 = input("Enter second name: ").lower()
name_3 = input("Enter third name: ").lower()
name_4 = input("Enter fourth name: ").lower()
name_5 = input("Enter second name: ").lower()
empty_list.append(name_1) # Sort the list alphabetically
empty_list.append(name_2)
empty_list.append(name_3)
empty_list.append(name_4)
empty_list.append(name_5)
empty_list.sort()
print("\n".join(empty_list)) # Display them one name per line