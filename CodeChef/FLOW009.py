def totalExpenses(quantity, price):
    expenses = 0
    if quantity < 1000:
        expenses = quantity * price
    else:
        expenses = quantity * price
        discount = expenses * 0.1
        expenses = expenses - discount
    return expenses

for t in range(int(input())):
    quantity, price = map(int, input().split())
    print(totalExpenses(quantity, price))