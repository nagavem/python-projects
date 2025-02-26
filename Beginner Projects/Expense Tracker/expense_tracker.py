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