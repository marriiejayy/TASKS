# Transport fare calculator
Distance = float(input("Enter the distance in kilometer:"))
Fare = float(input("Enter the fare per kilometer:"))
Total_fare = Distance * Fare

# Calculate and display the total fare with two decimal places using f"{value:.2f}"
print(f" The total fare to get to Olomore is {Total_fare:.2f}")