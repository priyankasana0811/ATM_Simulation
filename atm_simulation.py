pin = 1234
attempts = 3

login_success = False

while attempts > 0:
    entered_pin = int(input("Enter ATM PIN: ").strip())

    if entered_pin == pin:
        print("Login Successful!")
        login_success = True
        break
    else:
        attempts -= 1
        print("Incorrect PIN!")
        print("Attempts Left:", attempts)

        if attempts == 0:
            print("ATM Blocked! Too many wrong attempts.")

if login_success:
    print("-----ATM SIMULATION-----")
    balance = 1000

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance: ₹", balance)

        elif choice == 2:
            amount = float(input("Enter amount to deposit: ₹"))
            balance += amount
            print("Amount Deposited Successfully!")
            print("Updated Balance: ₹", balance)

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= balance:
                balance -= amount
                print("Withdraw Successful!")
                print("Remaining Balance: ₹", balance)
            else:
                print("Insufficient balance!")

        elif choice == 4:
            print("Thank you for using ATM Simulation!")
            break

        else:
            print("Invalid Choice! Please enter 1, 2, 3, or 4.")
