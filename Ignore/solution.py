import requests

# * convert the input into string and all upper case letters
from_currency = str(input("Enter currency: ")).upper()

to_currency = str(input("Enter currency 2: ")).upper()

amount = float(input("enter amount of money: "))

response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

# print(response)

print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")