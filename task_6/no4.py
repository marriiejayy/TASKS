# Task4 Create a Unique Voters Registration System
#  Ask for voter names and store in a set
Voters_name = set()
Name1 = input("Enter voters name: ")
Name2 = input("Enter voters name: ")

#  If a voter tries to register twice, display a warning.
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
# After registration, display the total number of unique voters
print("Total number of unique voters:", Voters_name)