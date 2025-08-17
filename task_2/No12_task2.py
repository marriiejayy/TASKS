# Simulated USSD Menu Interaction 
print("Welcome to Airtel Mobile Services!")
ussd_code = input("Kindly dial your USSD code (e.g., *123#): ")
print("\nMain Menu:")
print("1. Check Balance\n2. Buy Airtime\n3. Buy Data")

# Ask user to choose an option
choose_option = input("Enter your choice (1, 2, or 3): ")

#  Display confirmation message
print(f"\nYou selected option {choose_option}")

# Ask for amount 
amount = float(input("Enter amount in Naira: "))
print(f"\nTransaction complete! Option {choose_option} with ₦{amount:}")
