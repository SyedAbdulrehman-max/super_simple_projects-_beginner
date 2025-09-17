# Currency Converter	Convert using real-time rates	APIs, math

import requests
import json
# 1. API endpoint (USD is the base currency here)
url = "https://api.exchangerate-api.com/v4/latest/USD"

# 2. Get data from API
response = requests.get(url)
data = response.json()
with open('data.json','w') as  f :
    json.dump(data,f,indent= 4 )

# 3. User input
amount = float(input("Enter amount in USD: "))
currency = input("Enter target currency code (e.g., PKR, INR, EUR): ").upper()

# 4. Check if currency exists
if currency in data['rates']:
    rate = data["rates"][currency]
    converted_currency  = amount * rate 
    print(f"{amount} in {currency} is {converted_currency:.2f}")
else:
    print('Not found')