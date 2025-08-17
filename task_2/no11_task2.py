# Nigerian Currency Converter 

Amount_in_Naira = float(input("Enter the amount in Naira: "))
Exchange_rate_to_US_Dollars = float(input("Enter the exchange rate to US Dollars: "))
Exchange_rate_to_British_Pounds = float(input("Enter the exchange rate to British Pounds: "))
 
 # Conversion
usd = Amount_in_Naira / Exchange_rate_to_US_Dollars
gbp =  Amount_in_Naira/ Exchange_rate_to_British_Pounds

# print(f"{'Currency:'}{'Amount:'})
# print(f"{'Naira (₦)':}{Amount_in_Naira:'})
# print(f"{'US Dollars ($)'}{usd:')
# print(f"{'British Pounds (£)'}{gbp:}")