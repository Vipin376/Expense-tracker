from expense import Expense
import datetime
import calendar


    
def main():
    print(f"🎯Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget=5000

    #get user input  for expense
    expense = get_user_expense()

    #Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    ##read file and summarize expenses
    summarize_expense(expense_file_path ,budget)

    pass
def get_user_expense():
    print(f"Getting User Expense!")
    expense_name = input("Enter Expense name: ")
    expense_amount = float(input("Enter Expense amount: "))
    expense_categories = [
        "food" ,
        "Home" ,
        "Work" ,
        "fun",
        "Misc" ,
    ]
    
   
    while True:
        print("Select a acategory: ")
        for i, category_name in enumerate(expense_categories):
           print(f"{i + 1} . {category_name}")

        value_range = f"[ 1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range (len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
            name=expense_name , category=selected_category , amount=expense_amount 
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense:Expense, expense_file_path):
    print(f"🎯Saving User Expense!: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")



def summarize_expense(expense_file_path , budget ):
    print(f"🎯Summerizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path , "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category=line.strip().split(",")
            print(expense_name, expense_amount, expense_category)
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount),
                category=expense_category
            )
            print(line_expense)
            expenses.append(line_expense)
    print(expenses)
    
    amount_by_category={}
    for expense in expenses:
        key= expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expenses By Category:")
    for key, amount in amount_by_category.items():  
        print(f" {key}: ₹{amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent: ₹{total_spent:.2f}")

    remaining_budget= budget - total_spent
    print(f"Budget remaining: ₹{remaining_budget:.2f}")

    today = datetime.date.today()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    remaining_days = days_in_month - today.day

    print("Remaining days in current month: ", remaining_days)
    
    daily_budget= remaining_budget/ remaining_days
    print(f'Budget Per Day: ₹{daily_budget:.2f}')




if __name__ == "__main__":
    main()