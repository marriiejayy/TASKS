# Task4 Create a Unique Voters Registration System
#  Ask for voter names 
Voters_name = set()
Name1 = input("Enter voters name: ")
Name2 = input("Enter voters name: ")

if Name1 in Voters_name:
    print(" Warning! Name already registered:", Name1)
else:
    Voters_name.add(Name1)
    print(" Registration successful for:", Name1)

if Name2 in Voters_name:
  print(" Warning! Name already registered:", Name2)
else:
    Voters_name.add(Name2)
    print(" Registration successful for:", Name2)

print("Total number of unique voters:", Voters_name)