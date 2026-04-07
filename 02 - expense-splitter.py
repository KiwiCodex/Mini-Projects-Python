
# 1. Create the function
def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    # 2. Validate the amount of people
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than one.')

    # 3. Perform the calculation

    while True:
        choice = input("Do you want uneven split? (y/n): ").strip().lower()
        if choice in ("y", "n"):
            break
        print("Invalid input, write 'y' or 'n'")

    print(f'Total expense: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')


    if choice == "y":
        uneven_split(total_amount, number_of_people, currency)
    else:
        share_per_person: float = total_amount / number_of_people
        print(f'Each person should pay: {currency}{share_per_person:,.2f}')


def uneven_split(total_amount: float, number_of_people: int,  currency: str)-> None:

    percent_used = 0.0
    percents = []
    for i in range(1, number_of_people+1):
        while True:
            percent_choice: float = get_float(f'Enter the % for Person {i}: ')
        
            if percent_used + percent_choice > 100:
                print("You got over 100%, try again!")
            else:
                percents.append(percent_choice)
                percent_used += percent_choice
                print(f"Percent left: {100 - percent_used:.2f}%")
                break

    if abs(sum(percents) - 100) > 1e-6:
        print(f"\n Warning: Total percentage is {sum(percents)}%, not 100%. "f"The amounts will be proportional anyway.\n")

    for i, j in enumerate(percents, start=1):
        pay = total_amount * (j/100)
        print(f"Pay for Person {i}: {currency}{pay:,.2f}")


def get_float(prompt: str) ->float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, only digits please")

def get_int(prompt: str) ->int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, only integer numbers please")


# 5. Create a main entry point
def main() -> None:
    # 6. Try to get the user input and perform the calculation
    total_amount: float = get_float('Enter the total amount of the expense: ')
    number_of_people: int = get_int('Enter the number of people sharing the expense: ')

    # Call the function to calculate and display expenses
    calculate_split(total_amount, number_of_people, currency='$')


# 7. Run the script
if __name__ == '__main__':
    main()

