School_name = input("Enter the School name:")
Tuition_fee = float(input("Enter the tution fee:"))
Hostel_fee = float(input("Enter the Hostel fee:"))
Feeding_fee =float(input("Enter the feeding fee:"))

# Total fee
Total = Tuition_fee + Hostel_fee + Feeding_fee

# Print receipt format
print(f"School name: {School_name}\nTuition fee: {Tuition_fee}\nHostel fee: {Hostel_fee}\nFeeding fee: {Feeding_fee}\nTotal: {Total}")


