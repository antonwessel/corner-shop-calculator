print("Earned amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")

income = 202 + 118 + 2250 + 1680 + 1075 + 80
print(f"Income: ${income}")

print("Staff expenses:")
staff_expenses = int(input())
print("Other expenses:")
other_expenses = int(input())
print(f"Net income: ${income - staff_expenses - other_expenses}")