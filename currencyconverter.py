from pprint import PrettyPrinter
import requests

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_fO7tpIZ9H6AlQaoyxjbUr7sHppN5yMBFNDd7rsiW"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"v1/currencies?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = requests.get(url).json()['data']
    data = list(data.items())
    data.sort()
    return data


def print_currencies(currencies):
    for key, value in currencies:
        name = value['name']
        code = value['code']
        symbol = value['symbol']
        print(f"{code} - {name} - {symbol}")


def exchange_rate(currency_one, currency_two):
    endpoint = f"v1/latest?apikey={API_KEY}&currencies={currency_two}&base_currency={currency_one}"
    url = BASE_URL + endpoint
    response = requests.get(url)
    data = response.json()['data']
    rate = list(data.values())[0]
    print(f"{currency_one} -> {currency_two} = {rate}")
    return rate


def convert(currency_one, currency_two, amount):
    rate = exchange_rate(currency_one, currency_two)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency_one} is equal to {converted_amount} {currency_two}")
    return currency_two


def main():
    currencies = get_currencies()
    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of the two currencies")
    while True:
        command = input("Enter a command (q to quit): ").lower()
        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency_one = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency_one}: ")
            currency_two = input("Enter a currency to convert to: ").upper()
            convert(currency_one, currency_two, amount)
        elif command == "rate":
            currency_one = input("Enter a base currency: ").upper()
            currency_two = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency_one, currency_two)
        else:
            print("Unrecognized command!")


main()
