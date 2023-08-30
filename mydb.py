import mysql.connector

try:
    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vedant",
        database="crm",
        auth_plugin='vedant'
    )

    # Now you have a connection object that you can use to interact with the database
    cursorObject = connection.cursor()
    
    cursorObject.execute("SHOW DATABASES")
    
    # Don't forget to close the connection when you're done
    connection.close()

except mysql.connector.Error as err:
    print("Error:", err)
