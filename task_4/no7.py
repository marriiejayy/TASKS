# Task 7: List Manipulation
cities = ["Ibadan", "Ikeja", "Abeokuta","Dutse","Asaba"] #  Create a list of five cities
new_city = input("Enter a new city to replace the third one you typed: ") #Replace the third city with a new one 
cities[2] = new_city

removed_city = cities[:-1] # Remove the last city
print(removed_city)
new_city = removed_city.insert("Osogbo") # Add a new city to the beginning of the list
print(new_city) # Print the updated list.