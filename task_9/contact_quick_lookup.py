# Task  Contact Quick Lookup

# Tuples of names and phone numbers
Names = ("Lola", "Sade", "Mariam")
phone_numbers = ("09080461840", "098765432", "08116044841")

# Create a dictionary 
contacts = dict(zip(Names, phone_numbers))

# Ask the user for a name
search_name = input("Enter a name in the contacts: ")

# Retrieve the phone number 
phone = contacts.get(search_name)

# Display result
if phone:
    print(f"{search_name}'s phone number is: {phone}")
else:
    print(f" Hello!, {search_name} cannot be found in the contact list.")
