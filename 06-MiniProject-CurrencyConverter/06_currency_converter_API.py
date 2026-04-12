# 1. Import necessary functionality
import json
import sys
import requests
import random

# 2. Get the file path regarless of the script is run
def fetch_live_rates() -> dict[str, dict]:
    url = "https://www.floatrates.com/daily/eur.json"

    try:
        print("Fetching live market data...")
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Network Error: Could not connect to API. {e}")
        sys.exit(1)


# 3. Create the function
def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    # 4. Make sure the user input is lowered
    base = base.lower()
    to = to.lower()

    # 5. Get the dictionaries and define EUR as the reference rate (1.0) if it's not in the dictionary
    from_rate_data = rates.get(base, {'rate': 1.0}) if base != 'eur' else {'rate': 1.0}
    to_rate_data = rates.get(to, {'rate': 1.0}) if to != 'eur' else {'to': 1.0}


    # 6. Math: Result = Amount * (ToRate / FromRate)
    return amount * (to_rate_data['rate'] / from_rate_data['rate'])

# 7. User's input in amount variable
def get_float(prompt: str) ->float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, only digits please")

# 8. Validates user's input in currencies' variables
def get_currency(prompt: str, rates: dict[str, dict]) -> str:
    while True:
        user_input = input(prompt).strip().lower()

        if user_input == 'eur' or user_input in rates:
            return user_input
        
        print(f"'{user_input}' is not valid currency, Please try again: ")
        options = random.choices(list(rates), k=10)
        print(f"Available options: {options} ... and more.")
        print("-"*30)


# 10. Create a main entry point
def main() -> None:
    rates_data = fetch_live_rates()
    try:
        amount: float = get_float('Enter the total amount to convert: ')
        base_currency = get_currency('From: (e.g., USD, EUR): ', rates_data)
        target_currency = get_currency('From: (e.g., USD, EUR): ', rates_data)

        result = convert(amount, base_currency, target_currency, rates_data)

        print(f"Result: {amount:,.2f} {base_currency.upper()} = {result:,.2f} {target_currency.upper()}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
        

# 11. Run the script
if __name__ == '__main__':
    main()

