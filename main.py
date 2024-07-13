import pyodbc
import datetime

# Connection to database from Management Studio to VSC
connect_db = ("DRIVER={ODBC DRIVER 17 FOR SQL Server};"
              "Server=DESKTOP-TIV4J1P\\SQLEXPRESS;"
              "Database=KnightHardwareDB;"
              "UID=sa;"
              "PWD=Xeronate123*"
              )
 
def get_db_connection():
    connection = pyodbc.connect(connect_db)
    return connection

def main_menu():
    print("""
        Database Menu:
        1. Customers
        2. Parts
        3. Orders
        0. Quit
    """)

def sub_menu():
    print("""
        CRUD Options:
        1. Select
        2. Insert
        3. Update
        4. Delete
        0. Return to Main Menu
    """)

#======================================================================================
# Customer's CRUD methods

def select_customers():
    print("--------------------------------------")
    print("Display Customer")
    print("--------------------------------------")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        db_cursor.execute("SELECT * FROM Customers")
        for i in db_cursor:
            print(i)
        
        connection.close()
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)


def insert_customers():
    print("--------------------------------------")
    print("Insert Customer")
    print("--------------------------------------")
    customer_name = input("Enter Customer Name to Insert: ")
    city = input("Enter City to Insert: ")
    state = input("Enter State to Insert: ")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        sql = "INSERT INTO Customers (CustomerName, City, State) VALUES (?, ?, ?);"
        parameters = (customer_name, city, state)
        db_cursor.execute(sql, parameters)
        connection.commit()
        connection.close()
        print("Customer data inserted successfully!")
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)


def update_customers():
    print("--------------------------------------")
    print("Update Customer")
    print("--------------------------------------")
    select_customers()
    print("--------------------------------------")
    customer_id = input("Enter Customer ID to Update: ")
    customer_name = input("Enter Customer Name to Update: ")
    city = input("Enter City to Update: ")
    state = input("Enter State to Update: ")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        sql = "UPDATE Customers SET CustomerName = ?, City = ?, State = ? WHERE CustomerID = ?;"
        parameters = (customer_name, city, state, int(customer_id))
        db_cursor.execute(sql, parameters)
        connection.commit()
        connection.close()
        print("Customer data updated successfully!")
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)


def delete_customers():
    print("--------------------------------------")
    print("Delete Customer")
    print("--------------------------------------")
    select_customers()
    print("--------------------------------------")
    customer_id = input("Enter Customer ID to Delete: ")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        sql = "DELETE FROM Customers WHERE CustomerID = ?;"
        parameters = (int(customer_id))
        db_cursor.execute(sql, parameters)
        connection.commit()
        connection.close()
        print("Customer data deleted successfully!")
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)

#====================================================================================
# Parts CRUD methods

def select_parts():
    print("--------------------------------------")
    print("Display Parts")
    print("--------------------------------------")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        db_cursor.execute("SELECT * FROM Parts")
        for i in db_cursor:
            print(i)
        
        connection.close()
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)


def insert_parts():
    print("--------------------------------------")
    print("Insert Parts")
    print("--------------------------------------")
    part_code = input("Enter Part Code to Insert: ")
    part_name = input("Enter Part Name to Insert: ")
    inventory = input("Enter How Many Parts to Insert: ")
    price = input("Enter Price for Part: ")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        sql = "INSERT INTO Parts (PartCode, PartDescription, InventoryOnHand, Price) VALUES (?, ?, ?, ?);"
        parameters = (part_code, part_name,inventory,float(price))
        db_cursor.execute(sql, parameters)
        connection.commit()
        connection.close()
        print("Part data inserted successfully!")
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)


def update_parts():
    print("--------------------------------------")
    print("Update Parts")
    print("--------------------------------------")
    select_parts()
    print("--------------------------------------")
    part_id = input("Enter Part ID to Update: ")
    part_code = input("Enter Part Code to Update: ")
    part_name = input("Enter Part Name to Update: ")
    inventory = input("Enter How Many Parts to Update: ")
    price = input("Enter Price for Update: ")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        sql = "UPDATE Parts SET PartCode = ?, PartDescription = ?, InventoryOnHand = ?, Price = ? WHERE PartID = ?;"
        parameters = (part_code, part_name,inventory,float(price),part_id)
        db_cursor.execute(sql, parameters)
        connection.commit()
        connection.close()
        print("Part data updated successfully!")
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)


def delete_parts():
    print("--------------------------------------")
    print("Delete Part")
    print("--------------------------------------")
    select_parts()
    print("--------------------------------------")
    part_id = input("Enter Part ID to Delete: ")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        sql = "DELETE FROM Parts WHERE PartID = ?;"
        parameters = (int(part_id))
        db_cursor.execute(sql, parameters)
        connection.commit()
        connection.close()
        print("Part data deleted successfully!")
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)

#========================================================================================
# Order CRUD methods

def select_orders():
    print("--------------------------------------")
    print("Display Orders")
    print("--------------------------------------")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        sql = '''SELECT o.OrderID, c.CustomerName, p.PartCode, od.NumberOrdered
                 FROM Orders AS o
                    JOIN Customers AS c On o.CustomerID = c.CustomerID
                    JOIN OrderDetails AS od ON o.OrderID = od.OrderID
                    JOIN Parts AS p ON od.PartID = p.PartID;
                '''
        db_cursor.execute(sql)
        for i in db_cursor:
            print(i)
        
        connection.close()
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)


def insert_orders():
    print("--------------------------------------")
    print("Insert Orders")
    print("--------------------------------------")
    select_customers()
    print("--------------------------------------")
    customer_id = input("Enter Customer ID for Order: ")
    select_parts()
    print("--------------------------------------")
    part_id = input("Enter Part ID for Order: ")
    inventory = input("Enter Number Ordered for Order: ")

    connection = get_db_connection()
    db_cursor = connection.cursor()


    try:
        sql = """
            SET NOCOUNT ON;
            INSERT INTO Orders (CustomerID, OrderDate) VALUES (?, ?);
            SELECT @@IDENTITY AS OrderID;
        """
        parameters = (int(customer_id), datetime.datetime.now())
        db_cursor.execute(sql, parameters)
        order_id = db_cursor.fetchone()[0]

        sql2 = 'INSERT INTO OrderDetails (OrderID, PartID, NumberOrdered) VALUES (?, ?, ?);'
        parameters2 = [order_id, int(part_id), int(inventory)]
        db_cursor.execute(sql2, parameters2)

        connection.commit()
        connection.close()
        print("Order data inserted successfully!")
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)
        db_cursor.rollback()


def update_orders():
    print("--------------------------------------")
    print("Update Orders")
    print("--------------------------------------")
    select_orders()
    print("--------------------------------------")
    order_id = input("Enter Order ID to Update: ")
    customer_id = input("Enter Customer ID to Update: ")
    order_date = input("Enter Date Ordered (Date Time: yyyy-mm-dd hh:mm:ss) to Update: ")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        sql = "UPDATE Orders SET CustomerID = ?, OrderDate = ? WHERE OrderID = ?;"
        parameters = (customer_id, order_date, int(order_id))
        db_cursor.execute(sql, parameters)
        connection.commit()
        connection.close()
        print("Order data updated successfully!")
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)


def delete_orders():
    print("--------------------------------------")
    print("Delete Order")
    print("--------------------------------------")
    select_orders()
    print("--------------------------------------")
    order_id = input("Enter Part ID to Delete: ")

    try:
        connection = get_db_connection()
        db_cursor = connection.cursor()
        sql = "DELETE FROM Orders WHERE OrderID = ?;"
        parameters = (int(order_id))
        db_cursor.execute(sql, parameters)
        connection.commit()
        connection.close()
        print("Order data deleted successfully!")
        print("--------------------------------------")

    except pyodbc.Error as e:
        print(e)

#========================================================================================
# Main
def main():
    main_menu()
    main_input = int(input(": "))
    while main_input != 0:
        sub_menu()
        sub_input = int(input(": "))
        while sub_input != 0:
            #Customers Conditions
            if (main_input == 1 and sub_input == 1):
                select_customers()
            if (main_input == 1 and sub_input == 2):
                insert_customers()
            if (main_input == 1 and sub_input == 3):
                update_customers()
            if (main_input == 1 and sub_input == 4):
                delete_customers()

            #======================================#
            #Parts Conditions
            if (main_input == 2 and sub_input == 1):
                select_parts()
            if (main_input == 2 and sub_input == 2):
                insert_parts()
            if (main_input == 2 and sub_input == 3):
                update_parts()
            if (main_input == 2 and sub_input == 4):
                delete_parts()

            #======================================#
            #Orders Conditions
            if (main_input == 3 and sub_input == 1):
                select_orders()
            if (main_input == 3 and sub_input == 2):
                insert_orders()
            if (main_input == 3 and sub_input == 3):
                update_orders()
            if (main_input == 3 and sub_input == 4):
                delete_orders()

            sub_menu()
            sub_input = int(input(": "))

        main_menu()
        main_input = int(input(": "))

if __name__ == "__main__":
    main()           