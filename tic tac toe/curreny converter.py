import requests

amount = float(input("Enter amount: "))
from_curr = input("From currency code (e.g. USD, EUR, INR): ").upper()
to_curr = input("To currency code (e.g. EUR, INR, USD): ").upper()

url = f"https://open.er-api.com/v6/latest/{from_curr}"
response = requests.get(url).json()

if response.get("result") == "success":
    rates = response["rates"]
    if to_curr in rates:
        converted = amount * rates[to_curr]
        print(f"\n💰 {amount} {from_curr} = {converted:.2f} {to_curr}")
    else:
        print("Invalid target currency code.")
else:
    print("Failed to fetch conversion data. Check base currency code.")
