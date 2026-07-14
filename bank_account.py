users ={
"ahmed":{
        "password":"854140#",
         "balance":7500,
         
         },
"omar":{"password":"ereh854#",
         "balance":10500
        },
"kamal":{"password":"se4140#",
         "balance":2500
        }

}


def register():
    balance=0
    last_transaction= f"NO transaction yet"
    while True:    
        username=input("enter the user u want: ").strip()
        if not username:
            print("invalid username !")
            continue
        if  username  in users:
            print("username already exists! ")
            continue
        password=input("enter your password")
        if not password:
            print("enter your pass:")
            continue
        if len(password)<6:
            print("Not long enough ")
            continue 
        else:
            users[username]={"password":password,
                         "balance":balance,
                         "last transaction":last_transaction  # BONUS 3
                        }
        print("Account created successfully!")
        return
        
def Login():
    attempts = 0

    while True:
        username = input("username: ")
        password = input("password: ")

        if username in users and users[username]["password"] == password:
            return bank_menu(username)

        else:
            print("Invalid username or password!")
            attempts += 1
            if attempts<3:
                print(f"you got {3-attempts}left")
            elif attempts>=3:
                print("Too many failed attempts!")
                print("TRY AGAIN LATER!")
                return

            continue
        

def bank_menu(username):
    print(f"Welcome sir {username},your balance is:{users[username]['balance']}")
    
    while True:
        
        print("="*10 + " Bank Menu "+ "="*10)
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw ")
        print("4. Transfer ")
        print("5. Change Password")
        print("6. Logout")
        try:
            choice=int(input("plz enter your request:"))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
#CHECKING BALANCE
        if choice==1:
                print(f"your current balance is:{users[username]['balance']}")
                print(f"your last transaction was:{users[username]['last transaction']}")
                print("")
# DEPOSIT 
        elif choice==2:
            while True:
                try:
                    amount=float(input("Amount:"))
                    if amount==0:
                        print("operation has been canceled ")
                        break
                    elif amount<0:
                        print("invalid amount")
                        continue
                    else:
                        users[username]['balance']+=amount
                        print(f"your final balance is {users[username]['balance']}")
                        users[username]['last transaction']=f"deposite of {amount}"
                        print("-"*50)
                        print_receipt(username)
                        print("")

                        break
                except ValueError:
                    print("plz enter correct  amount")
                    continue 
# WITHDRAW
        elif choice==3: 
            while True:
                try:
                    withdraw=int(input("Enter the amount to withdraw: "))
                    if withdraw==0:
                        print("operation has been canceled ")
                        break
                    
                    elif withdraw > users[username]['balance'] or withdraw < 0:
                        print("invalid number .")
                        continue
                    
                    else:
                        users[username]['balance']-=withdraw
                        print(f"you have withdrawn {withdraw}")
                        print(f"your new balance is {users[username]['balance']}")
                        print(f"operation successful. Thank you for banking with us.")
                        users[username]['last transaction']=f"withdraw of {withdraw}"
                        print_receipt(username)
                        print("")
                        break
                except ValueError:
                    print("please enter a number < balance > 0!")
                    continue

#TRANSFER 
        elif choice==4:
            while True:
                try:        
                    recipient_username =input("The recipient's Username:")
                    if recipient_username not in users.keys():
                        print("invalid username, plz try again.")
                        continue
                    elif recipient_username == username :
                        print("can't transfer money to yourself ")
                        continue

                    amount=float(input("The Amount:"))
                    if amount==0:
                        print("operation has been canceled ")
                        break
                    
                    elif amount > users[username]['balance'] or amount <0:
                        print("error:The balance must be sufficient")
                        continue
                    else:
                        users[username]['balance']-=amount
                        users[recipient_username]['balance']+=amount
                        print("The amount is deducted from the sender and added to the recipient")
                        print(f"your current balance is:{users[username]['balance']}")
                        users[username]['last transaction']=f"transfer of {amount}"
                        users[recipient_username]['last transaction']=f"recive of {amount}"
                        print_receipt(username)
                        print("")
                        print_receipt(recipient_username)
                        print("")
                        break
                except ValueError:
                    print("error")
                    continue                        

#CHANGING PASSWORD                
        elif choice==5:
            while True:    
                current_password=input("Enter your current password:")
                new_password=input("Enter your new password:")
                if current_password=="0" or new_password=="0":
                    print("operation has been canceled ")
                    break

                elif current_password!=users[username]['password']:
                    print("the password isn't matched!")
                    continue
                elif len(new_password) <6:
                    print("the new password isn't long enough!")
                    continue
                else:
                    users[username]['password']=new_password 
                    print("the operation is successful ")
                    print("")
                    break
#LOGOUT
        elif choice==6:
                print(f"THANK FOR BANKING WITH US!")
                return 
        else:
            print("choose num from 1-6")
            continue

#BONUS 4
def print_receipt(username):
    print("")
    print("-"*50)
    print("RECEIPT")
    print("-"*50)
    print("")
    print(f"username:{username}")
    print(f"balance:{users[username]['balance']}")
    print(f"transaction:{users[username]['last transaction']}")




def main():
    while True:
        print("========== Welcome To Python Bank ==========")
        print("")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("")
        print(f"the members using the app are: {len(users.keys())}")
        print("")


        try:
            choice=int(input("choose your request:"))
        except ValueError:
            print("p;z enter a number! from(1-3)")
            continue
        if choice==1:
            register()
        elif choice==2:
            Login()
        elif choice==3:
            return
        else:
            continue



if __name__ == "__main__" :
    main()

                



        

     
     
    
    
    
    



        


    

