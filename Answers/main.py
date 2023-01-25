#Question 1
def priceCheck(products: [], productPrices: [], productSold: [], soldPrice: []) -> int:
  Dec = {}
  ErrorCounter = 0
  for product, price in zip(products, productPrices):  # this loop give you by value ->for each
    Dec[product] = price
  for proSold, PriceSold in zip(productSold, soldPrice):
    if Dec[proSold] != PriceSold:  # Dec[prosold] return the value for me    PriceSold have the value of the product
      ErrorCounter += 1
  return ErrorCounter
#-----------------------------------------------------------------------------------------------------------------------
#Question 2
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="name",
  password="password",
  database="database"
)
mycursor1 = mydb.cursor() #For Creating DATABASE
mycursor1.execute("CREATE DATABASE mydatabase")
mycursor = mydb.cursor() #For Createing Tables
mycursor2 = mydb.cursor() #For the Query
mycursor.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), salary(int),dept_id(int))")
mycursor.execute("CREATE TABLE Department (id INT AUTO_INCREMENT PRIMARY KEY,dep_name VARCHAR(255),location VARCHAR(255))")
sql = "INSERT INTO Employee (name,salary,dept_id) VALUES (%s, %s,%s)"
val = [
  ('Candice', 4685,1),
  ('Julia', 2559,2),
  ('Bob', 4405,4),
  ('Scarlet', 2350,1),
  ('Llena', 1151,4)
]
sql1 = "INSERT INTO Department (dep_name,location) VALUES (%s, %s)"
val1 = [
  (1,"Executive","Sydne"),
  (2,"Production","Sydne"),
  (3,"Rescources","Cape Down"),
  (4, "Technical", "Texax"),
  (5,"Management","Paris"),
]
mycursor.execute(sql, val)
mycursor.execute(sql1, val1)
mydb.commit()
mycursor2.execute("SELECT dept_id,COUNT(*) FROM Employee GROUP BY dep_name ORDER BY count DESC")
myresult = mycursor2.fetchall()
for x in myresult:
  print(x)
#-----------------------------------------------------------------------------------------------------------------------
#Question 3
  def Recursive_Digit(Number: int) -> int:
    if Number == 0:
      return 0
    return Recursive_Digit(Number // 10) + Number % 10