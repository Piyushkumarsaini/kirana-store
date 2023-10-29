import sqlite3

# Connect to the SQLite database named "item.db" or create it if it doesn't exist
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

# Commit the changes to the database
conn.commit()

# Function to add data to the "items" table
def add_data(Customer, Item_name, item_Purchase, item_Prices):
    Total = item_Prices * item_Purchase

    # Insert data into the table using parameterized query to avoid SQL injection
    cursor.execute("INSERT INTO items ('Customer', 'Item name', 'item Purchase', 'item Prices', 'Total') VALUES (?, ?, ?, ?, ?)", (Customer, Item_name, item_Purchase, item_Prices, Total))
    conn.commit()

# Main function to interact with the user and manage data
def main():
    Customer = input("enter the Customer name :")
    while True:
  
        item_name = input("enter the item name : ")
        try:
            item_purchased = int(input("enter the purchased quantity: "))
        except:
             print("Please enter a valid number for purchased quantity.")
             continue
        try:
            item_prices = int(input("enter the price : "))
        except:
            print("Please enter a valid number for price.")
            continue

        add_data(Customer, item_name, item_purchased, item_prices)

        choice = input("Add another item? : (yes/no)")

        if choice == "no":
          break  


    print("---item---")
    # Select and display the total cost of items for the given customer
    cursor.execute("SELECT Customer, sum(Total) FROM items WHERE Customer =? GROUP BY Customer", (Customer,))   
    items = cursor.fetchall()
    for item in items:
        print(item)



# Call the main function to start the program
main()
conn.close()

