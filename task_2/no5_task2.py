# Daily market report 
market_name = input("Enter market name? : ")
number_of_traders = int(input("Enter the number of traders in the market? :"))
daily_revenue_in_naira = int(input("Enter the daily revenue? :"))

# Result using f_string format 
print("\nDaily Market Report")
print(f"Market Name: {market_name}")
print(f"Number of Traders: {number_of_traders:,}")
print(f"Daily Revenue (Naira): ₦{daily_revenue_in_naira:,}k")




