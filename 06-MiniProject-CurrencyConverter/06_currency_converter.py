# 1. Import necessary functionality
import json
import os
import sys

# 1.5. Get the file path regarless of the script is run
def get_file_path(filename: str) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

# 2. Load the rates from a JSON file
def load_rates(json_file: str) -> dict[str, dict]:
    file_path = get_file_path(json_file)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: The file '{json_file}', was not found at {file_path}")
        sys.exit(1)
    
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{json_file}")
        sys.exit(1)

# 3. Create the function
def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    # 4. Make sure the user input is lowered
    base = base.lower()
    to = to.lower()

    # 5. Get the dictionaries and define EUR as the reference rate (1.0) if it's not in the dictionary
    from_rate_data = rates.get(base) if base != 'eur' else {'rate': 1.0}
    to_rate_data = rates.get(to) if to != 'eur' else {'to': 1.0}

    # 6. Checks if the currencies were found or defined
    if from_rate_data is None or to_rate_data is None:
        missing = base if from_rate_data is None else to
        raise ValueError(f"Currency '{missing}' not found in the database" )

    # 7. If base is EUR (1.0), it simplifies to: Amount * TargetRate
    return amount * (to_rate_data['rate'] / from_rate_data['rate'])

# 8. User's input in amount variable
def get_float(prompt: str) ->float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, only digits please")

# 9. Validates user's input in currencies' variables
def get_currency(prompt: str, rates: dict[str, dict]) -> str:
    while True:
        user_input = input(prompt).strip().lower()

        if user_input == 'eur' or user_input in rates:
            return user_input
        
        print(f"'{user_input}' is not valid currency, Please try again: ")


# 10. Create a main entry point
def main() -> None:
    rates_data = load_rates('rates.json')
    try:
        amount: float = get_float('Enter the total amount to convert: ')
        base_currency = get_currency('From: (e.g., USD, EUR): ', rates_data)
        target_currency = get_currency('From: (e.g., USD, EUR): ', rates_data)

        result = convert(amount, base_currency, target_currency, rates_data)

        print(f"Result: {amount:.2f} {base_currency.upper()} = {result:2f} {target_currency.upper()}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
        

# 11. Run the script
if __name__ == '__main__':
    main()

"""
Homework:
1. Right now it works fine if you insert a rate that exists, but make it so that if the user
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options.
2. Edit the script so that the "to" currency can also be specified as euro. 
3. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API. 
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script. 

"""