Customers_full_name = input("What is the your full name? : ")
Units_consumed_kWh = int(input("What is the amount of Units you consumed? : "))
Cost_per_unit = float(input("What is the Cost per unit of the amount you consumed? :₦ "))
Total_bill = Units_consumed_kWh * Cost_per_unit
print(f"Customers_full_name: {Customers_full_name}\nUnits consumed: {Units_consumed_kWh} \nCost per unit: ₦{Cost_per_unit} \ntotal bill ₦{Total_bill}")