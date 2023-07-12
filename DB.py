import mysql.connector

myDB = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password',
    database='testdb'
)

# print(myDB)
mycursor = myDB.cursor() # from here we can execute 

# to create a table use:
# mycursor.execute("CREATE TABLE cocktail_bar (name VARCHAR(255), typeOfBar VARCHAR(255))")

# to show the tables that has been created use:

sqlFormula = "INSERT INTO cocktail_bar(name, typeOfBar) VALUES(%s, %s)"
# example:

cocktailbar1 = ("Punch Room", "Speakeasy bar")

mycursor.execute(sqlFormula, cocktailbar1)

# to save the changes:
myDB.commit()