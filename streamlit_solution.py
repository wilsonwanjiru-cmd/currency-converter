import requests

from_currency = str(input("Enter the currency you'd like to convert from: ").upper())
to_currency = str(input("Enter the currency you'd like to convert to: ").upper())
amount = float(input("Enter the amount of money: "))

response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

if response.status_code == 200:
    exchange_rate = response.json()['rates'][to_currency]
    converted_amount = amount * exchange_rate
    print(f"{amount} {from_currency} is {converted_amount} {to_currency}")
else:
    print("Error fetching data from the API.")
