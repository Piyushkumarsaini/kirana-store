# # khali lise banate hai
# data = {}

import sqlite3


conn = sqlite3.connect("item.db")
cursor = conn.cursor()

# Create a table to store item data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items
    (
        "Customer" TEXT,
        "Item name" TEXT,
        "item Purchase" INTEGER,
        "item Prices" INTEGER,
        "Total" INTEGER
    )
''')

conn.commit()


def add_data(Customer, Item_name, item_Purchase, item_Prices):
    Total = item_Prices * item_Purchase
    cursor.execute("INSERT INTO items ('Customer', 'Item name', 'item Purchase', 'item Prices', 'Total') VALUES (?, ?, ?, ?, ?)", (Customer, Item_name, item_Purchase, item_Prices, Total))
    conn.commit()

def main():
    Customer = input("enter the Customer name :")
    while True:
        item_name = input("enter the item name : ")
        item_purchased = int(input("enter the purchased quantity: "))
        item_prices = int(input("enter the price : "))

        add_data(Customer, item_name, item_purchased, item_prices)

        choice = input("Add another item? : (yes/no)")

        if choice == "no":
            break   

    print("---item---")
    cursor.execute("SELECT Customer, sum(Total) FROM items WHERE Customer =? GROUP BY Customer", (Customer,))   
    items = cursor.fetchall()
    for item in items:
        print(item)

conn.commit()

main()

