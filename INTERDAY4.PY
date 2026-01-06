# Smart Expense Analyzer with Alerts

n = int(input("Enter number of expenses: "))

expenses = []   # list to store all expense amounts

category_totals = {
    "Food": 0,
    "Travel": 0,
    "Shopping": 0,
    "Other": 0
}

for i in range(1, n + 1):
    amount = int(input(f"Expense {i} amount: "))
    category = input(f"Expense {i} category (Food/Travel/Shopping/Other): ")

    expenses.append(amount)

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals["Other"] += amount

    if amount > 500:
        print("High expense detected")

# calculations
total_expense = sum(expenses)
average_expense = total_expense / n

print("\nTotal Expense:", total_expense)
print("Average Expense:", average_expense)

print("\nCategory-wise Expenses:")
for cat, amt in category_totals.items():
    print(cat, ":", amt)

# highest spending category
highest_category = max(category_totals, key=category_totals.get)
print("\nHighest Spending Category:", highest_category)

# spending status
if average_expense <= 200:
    print("Spending Status: Controlled Spending")
elif average_expense <= 400:
    print("Spending Status: Moderate Spending")
else:
    print("Spending Status: High Spending")