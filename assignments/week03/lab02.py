# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "4":
            print("Thank you to use our ATM")
            break

        elif choice == "1":
            print("Now, You have : ",balance)

        elif choice == "2":
            withdraw = float(input("Withdraw amount : "))
            balance = balance - withdraw
            print("Now, You have : ",balance)

        elif choice == "3":
            deposit = float(input("Deposit amount : "))
            balance = balance + deposit
            print("Now, You have : ",balance)
        else:
            print("Invalid Choice, Please Re-enter.")
        
else:
    print("Invalid PIN")
