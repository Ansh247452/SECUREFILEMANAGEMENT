from modules.expense import add_expense, view_expenses, delete_expense, update_expense
from modules.search import search_by_date
from modules.reports import category_report
from modules.budget import set_budget, check_budget
from modules.subscription import add_subscription, upcoming_subscriptions

from db import engine, Base
import models

Base.metadata.create_all(bind=engine)

def menu():
    while True:
        print("\n" + "="*35)
        print("        FINTRACK PRO")
        print("="*35)
        print("1  Add Expense")
        print("2  View Expenses")
        print("3  Update Expense")
        print("4  Delete Expense")
        print("5  Search by Date")
        print("6  Category Report")
        print("7  Set Budget")
        print("8  Check Budget")
        print("9  Add Subscription")
        print("10 View Subscriptions")
        print("0  Exit")
        print("="*35)

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            search_by_date()
        elif choice == "6":
            category_report()
        elif choice == "7":
            set_budget()
        elif choice == "8":
            check_budget()
        elif choice == "9":
            add_subscription()
        elif choice == "10":
            upcoming_subscriptions()
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")

menu()
