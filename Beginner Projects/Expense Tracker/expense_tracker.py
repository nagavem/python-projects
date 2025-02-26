import sqlite3
import argparse
import datetime

#Fn to add an expense
def add_expense(description,amount):
    #connect to sqllite db
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    #get today's date
    date = datetime.date.today().strftime("%Y-%m-%d")
    category = "Misc" # Default category

    #Insert data
    cursor.execute(
        "INSERT into expenses(date,category,amount,description) VALUES (?,?,?,?)",
                   (date,category,amount,description)
            )                  

    # Get the id of the last inserted row
    expense_id = cursor.lastrowid

    #Commit and close connection
    conn.commit()
    conn.close()

    print(f"✅ Expense added successfully (ID: {expense_id})")

#Main function to handle CLI commands

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    #Add command
    parser.add_argument("add", help="Add a new expense", nargs='?',default=None)
    parser.add_argument("--description",required=True,help="Description of the expense")
    parser.add_argument("--amount",type=float,required=True,help="Amount of the expense")

    args = parser.parse_args()

    if args.add == "add":
        add_expense(args.description,args.amount)

if __name__ == "__main__":
    main()