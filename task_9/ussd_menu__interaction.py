# Simulated USSD Menu Interaction
Balance = 2500

print("Welcome to Airtel mobile service!")
user = input("Dial *312#: ") # Ask the user to "dial" a USSD code

if user != "*312#":
    print("Invalid code!")
else:
    while True: #Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data")
        print("\nPick an option")
        print("1. Check balance.")
        print("2. Buy Airtime.")
        print("3. Buy Data.")
        print("4. Exit")

        choice = input("Enter your choice: ")
        # 1. Check balance
        if choice == "1":
            print(f"Your airtime balance is: ₦{Balance}")
            break
        # 2. Buy airtime
        if choice == "2":
            Airtime_amount = int(input("Enter amount: ₦"))
            if Airtime_amount <= Balance:
                Balance -= Airtime_amount
                print(f"You have successfully purchased ₦{Airtime_amount} airtime.")
                print(f"New Balance: ₦{Balance}")
            else:
                print("Insufficient funds!")
        # 3. Buy data
        elif choice == "3":
            while True:  
                print("\nSelect a Data plan")
                print("1. Daily Plans")
                print("2. Weekly Plans")
                print("3. Monthly Plans")
                print("4. Back")
                data_choice = input("Enter your choice: ")
                # Daily plans
                if data_choice == "1":
                    print("\nDaily Plans:")
                    print("1. ₦300/300MB")
                    print("2. ₦200/230MB")
                    print("3. ₦100/110MB")
                    print("4. ₦75/75MB")
                    plan = input("Select plan: ")

                    if plan == "1" and Balance >= 300:
                        Balance -= 300
                        print("You purchased 300MB data.Kindly check your SMS for more information")
                    elif plan == "2" and Balance >= 200:
                        Balance -= 200
                        print("You purchased 230MB data.Kindly check your SMS for more information")
                    elif plan == "3" and Balance >= 100:
                        Balance -= 100
                        print("You purchased 110MB data.Kindly check your SMS for more information")
                    elif plan == "4" and Balance >= 75:
                        Balance -= 75
                        print("You purchased 75MB data.Kindly check your SMS for more information")
                    else:
                        print("Insufficient funds.")
                    print(f"Remaining Balance: ₦{Balance}")
                # Weekly plans
                elif data_choice == "2":
                    print("\nWeekly Plans:")
                    print("1. ₦500/1.5GB (7 days)")
                    print("2. ₦1000/3GB (7 days)")
                    print("3. ₦1500/7GB (7 days)")
                    plan = input("Select plan: ")
                    if plan == "1" and Balance >= 500:
                        Balance -= 500
                        print("You purchased 1.5GB data.Kindly check your SMS for more information")
                    elif plan == "2" and Balance >= 1000:
                        Balance -= 1000
                        print("You purchased 3GB data.Kindly check your SMS for more information")
                    elif plan == "3" and Balance >= 1500:
                        Balance -= 1500
                        print("You purchased 7GB data.Kindly check your SMS for more information")
                    else:
                        print("Insufficient funds.")
                    print(f"Remaining Balance: ₦{Balance}")
                # Monthly plans
                elif data_choice == "3":
                    print("\nMonthly Plans:")
                    print("1. ₦1000/2GB (30 days)")
                    print("2. ₦2000/4.5GB (30 days)")
                    print("3. ₦3000/10GB (30 days)")
                    plan = input("Select plan: ")

                    if plan == "1" and Balance >= 1000:
                        Balance -= 1000
                        print("You purchased 2GB data.Kindly check your SMS for more information")
                    elif plan == "2" and Balance >= 2000:
                        Balance -= 2000
                        print("You purchased 4.5GB data.Kindly check your SMS for more information")
                    elif plan == "3" and Balance >= 3000:
                        Balance -= 3000
                        print("You purchased 10GB data.Kindly check your SMS for more information")
                    else:
                        print("Insufficient funds.")
                    print(f"Remaining Balance: ₦{Balance}")
                 # Back to main menu
                elif data_choice == "4": 
                    break  
        # Exit
        elif choice == "4":
            print(" Thank you for using Airtel service!")
            break

