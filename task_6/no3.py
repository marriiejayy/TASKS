# Task3 Simulate a football match ticket system
# - Store all seat numbers (1 to 50) in a set.
Seat_numbers = set(range(1, 51))

# - Ask users to "book" a seat by entering the number.
seat = int(input("Enter your seat number: "))
print(Seat_numbers)
# - Remove booked seats from the set
if seat in Seat_numbers:
    Seat_numbers.remove(seat)  
    print("Seat", seat, "successfully booked!")
else:
    print(" Seat not available.")


# - Show remaining seats after each booking
print("Remaining seat number:",Seat_numbers)