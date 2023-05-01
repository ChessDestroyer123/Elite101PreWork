import mysql.connector

connection = mysql.connector.connect(
    user = "bank_account",
    database = "accounts",
    password = "Rajni123",
    autocommit = True
)

cursor = connection.cursor()
cursor.execute("create database if not exists bank_account")
cursor.execute("use bank_account")

cursor.execute(
    "create table if not exists bank_account(account_number int primary key auto_increment, name varchar(45), city varchar(45), balance int, phone varchar(45))"
)

cursor.execute(   
     "create table if not exists transaction(account_number int, amount int, transaction_option varchar(1), foreign key (account_number) references bank_account(account_number))"
)




print("Hello! Welcome to Gringotts Bank!")

while True:
    print("1. Create account")
    print("2. Withdraw Money")
    print("3. Deposit")
    print("4. See Account")
    print("5. Leave")

    choice = int(input("Please enter your choice:"))
    if choice == 1:
        name = input("Please Enter your name:")
        city = input("Please enter the name of the current city you live in:")
        phone = input("Please provide your phone number (no dashes or spaces please):")
        balance = 0
        sql_input = "INSERT into bank_account(name, city, phone_number, balance) values (%s,%s,%s,%s)"
        val = (name, city, phone, balance)
        cursor.execute(sql_input, val)
        cursor.execute("SELECT * FROM bank_account where name = '"+name+"'")
        print("Thank you for creating your account at Gringotts! You have become a Wizard of the World!")

        for i in cursor:
            print(i)
    
    if choice == 2:
        account_num = input("Please enter your account_number:")
        deposit_money = int(input("Please enter the amount of money you want to deposit:"))
        transaction_option = "d"
        cursor.execute("INSERT into transaction VALUES('"+account_num+"','"+str(deposit_money)+"','"+transaction_option+"')")
        cursor.execute("UPDATE bank_account set balance = balance+'" + str(deposit_money)+"' WHERE account_number = '"+ account_num + "'")
        print("You have deposited",deposit_money,"Gringotts into account:",account_num)
    if choice == 3:
      account_num = input("Please enter your account_number:")
      withdraw_money = int(input("Please enter the amount of money you want to withdraw:"))  
      select_Query = "SELECT balance from bank_account WHERE account_number = '" + account_num+"'" 
      cursor.execute(select_Query)
      balance_now = cursor.fetchone()[0]
      if withdraw_money < balance_now:
          transaction_option = "y"
          cursor.execute("INSERT into transaction VALUES('" + account_num +"','"+str(withdraw_money)+"','"+transaction_option+"'"")")
          cursor.execute("UPDATE bank_account set balance = balance+'" + str(withdraw_money)+"' WHERE account_number = '"+ account_num + "'")
          print("You have deposited",withdraw_money,"Gringotts into account:",account_num)
      else:
          print("Sorry, you cannot withdraw that many Gringotts.")

    if choice == 4:
        account_num = input("Please enter your account_number:")
        cursor.execute("SELECT * FROM bank_account WHERE account_number = '" + account_num + "'")
        for i in cursor:
            print(i)
    else:
        break

connection.close()
