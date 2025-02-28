#!/usr/bin/env python3

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

#Fn to update an expense using the id
def update_expense(expense_id, description = None, amount = None):
    conn=sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    #check if expense exists
    cursor.execute("SELECT * FROM expenses where id = ?", (expense_id,))
    expense = cursor.fetchone
    if not expense:
        print(f"❌ Expense with ID {expense_id} not found.")
        conn.close()
        return
    
    #prepare the update query
    updates = []
    values = []

    if description:
        updates.append("description = ?")
        values.append(description)
    
    if amount:
        updates.append("amount = ?")
        values.append("amount")

    if not updates:
        print("⚠ No changes provided.")
        conn.close()
        return
    
    values.append(expense_id)
    query = f"UPDATE expenses SET {', '.join(updates)} WHERE id = ?"

    # Execute the update query
    cursor.execute(query,values)
    conn.commit()
    conn.close()

    print(f"✅ Expense (ID: {expense_id}) updated successfully!")

#Fn to delete an expense
def delete_expense(expense_id):
    conn=sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    #Check if the expense exists
    cursor.execute("SELECT * FROM expenses where id = ?", (expense_id,))
    expense = cursor.fetchone
    if not expense:
        print(f"❌ Expense with ID {expense_id} not found.")
        conn.close()
        return
    
    # Delete the expense
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

    print(f"✅ Expense (ID: {expense_id}) deleted successfully!")

#Main function to handle CLI commands

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    # Add subparsers to the main parser
    subparsers = parser.add_subparsers(dest="command")

    #Add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description",required=True,help="Description of the expense")
    add_parser.add_argument("--amount",type=float,required=True,help="Amount of the expense")

    # Update Command
    update_parser = subparsers.add_parser("update",help="Update an existing expense")
    update_parser.add_argument("id",type=int,help="Expense ID to update")
    update_parser.add_argument("--description",help="New description")
    update_parser.add_argument("--amount",type=float,help="New amount")


    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description,args.amount)
    elif args.command == "update":
        update_expense(args.id,args.description,args.amount)

if __name__ == "__main__":
    main()