# 1. Create a function to calculate finances
def calculate_finances(monthly_income: float, tax_rate: float, expenses: float, currency: str) -> None:
    # 2. Do the math for each field
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax
    money_saved_monthly: float = monthly_net_income - expenses
    money_saved_yearly: float = yearly_net_income - (expenses * 12)

    # 3. Format the information nicely for the user
    print('--------------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Monthly money left: {currency}{money_saved_monthly:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print(f'Yearly money left: {currency}{money_saved_yearly:,.2f}')
    if(money_saved_yearly < 0):
        print("Man, you truly live in debt")
    print('--------------------------------')


def get_float(prompt: str) ->float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, only digits please")


# 4. Create a main entry point for the program
def main() -> None:
    # 5. Gather user input
    
    monthly_income: float = get_float('Enter your monthly income: ')
    tax_rate: float = get_float('Enter your tax rate (%): ')
    expenses: float = get_float("How many you expend monthly in your living? (rent, food, etc): ")

    # 6. Call the function
    calculate_finances(monthly_income, tax_rate, expenses, currency='CLP')


# 7. Run the script
if __name__ == "__main__":
    main()

