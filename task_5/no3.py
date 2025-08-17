# Task 3 
# Create a tuple of 5 Nigerian state entered by the user
Nigerian_states = input("Hello user, kindly enter 5 Nigerian states\nNote: ensure you put space")
split_states = Nigerian_states.split(",")
tupple = tuple(split_states)

 # Print first and last state
print(tupple[::3])

# Check if Lagos is in tuple
print("Lagos" in tupple) 

# print No. of state entered
print(len(tupple))
