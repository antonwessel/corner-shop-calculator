def read_expense(prompt):
    while True:
        print(prompt)
        expense_text = input().strip()

        try:
            expense = float(expense_text)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if expense < 0:
            print("Expense cannot be negative.")
            continue

        return expense


earnings = [
    ("Bubblegum", 202),
    ("Toffee", 118),
    ("Ice cream", 2250),
    ("Milk chocolate", 1680),
    ("Doughnut", 1075),
    ("Pancake", 80),
]

print("Earned amount:")
income = 0

for product, amount in earnings:
    print(f"{product}: ${amount}")
    income += amount

print(f"Income: ${income}")

staff_expenses = read_expense("Staff expenses:")
other_expenses = read_expense("Other expenses:")
net_income = income - staff_expenses - other_expenses
print(f"Net income: ${net_income:.2f}")