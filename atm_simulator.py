
# ==========================================
#          SIMPLE ATM SIMULATOR
# ==========================================

# Account Details
correct_pin = "1234"
balance = 5000.0


# 1. LOGIN FUNCTION
def login():
    print("\n================================")
    print("       WELCOME TO ATM")
    print("================================")

    attempts = 3

    while attempts > 0:
        pin = input("\nEnter your ATM PIN: ")

        if pin == correct_pin:
            print("\nLogin Successful!")
            return True
        else:
            attempts -= 1
            print("Incorrect PIN!")

            if attempts > 0:
                print("Remaining Attempts:", attempts)

    print("\nToo many incorrect attempts!")
    return False


# 2. CHECK BALANCE FUNCTION
def check_balance():
    print("\n---------- CHECK BALANCE ----------")
    print("Your Current Balance: Rs.", balance)


# 3. DEPOSIT FUNCTION
def deposit():
    global balance

    print("\n---------- DEPOSIT MONEY ----------")

    try:
        amount = float(input("Enter Amount: Rs. "))

        if amount > 0:
            balance += amount
            print("\nDeposit Successful!")
            print("Deposited Amount: Rs.", amount)
            print("Updated Balance: Rs.", balance)
        else:
            print("Enter a valid positive amount!")

    except ValueError:
        print("Invalid Input! Please enter numbers only.")


# 4. WITHDRAW FUNCTION
def withdraw():
    global balance

    print("\n---------- WITHDRAW MONEY ----------")

    try:
        amount = float(input("Enter Amount: Rs. "))

        if amount <= 0:
            print("Enter a valid positive amount!")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance -= amount
            print("\nWithdrawal Successful!")
            print("Withdrawn Amount: Rs.", amount)
            print("Remaining Balance: Rs.", balance)

    except ValueError:
        print("Invalid Input! Please enter numbers only.")


# 5. ATM MENU FUNCTION
def atm_menu():

    while True:
        print("\n================================")
        print("          ATM MAIN MENU")
        print("================================")

        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("\nEnter Your Choice (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank You For Using Our ATM!")
            print("Have a Nice Day!")
            break

        else:
            print("\nInvalid Choice! Please Select 1-4.")


# 6. MAIN PROGRAM
def main():

    if login():
        atm_menu()

    else:
        print("\nAccess Denied!")
        print("Please Contact Your Bank.")


# ==========================================
#          PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":
    main()

# ==========================================
#          END OF ATM PROJECT
# ==========================================
