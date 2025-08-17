# Task 4 Unique Members Registration
# Ask the user to enter three names separated by commas
Names = input("Enter three names separated by commas: ")

# Convert input string to a set to remove duplicates
Names_in_set = set(name for name in Names.split(","))

# Create a dictionary where each name is a key and its length is the value
name_length_dict = {name: len(name) for name in Names_in_set}

# Print the resulting dictionary
print("\n***** Unique Members and Name Lengths *****")
print(name_length_dict)
