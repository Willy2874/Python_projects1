from locale import currency
import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1 = 'INR'
currency_2 = 'USD'
amount = '1000'

querystring = {"from":currency_1,"to":currency_2,"amount":"1000"}

headers = {
	"X-RapidAPI-Key": "29b0ad3034msh4cd89019ad29d08p14fdc7jsn7f5975b40696",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data['result']['convertedAmount']
formatted = '{:,.2f}'.format(converted_amount)

print(converted_amount, formatted)