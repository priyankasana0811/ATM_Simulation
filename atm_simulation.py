print("-----ATM SIMULATION-----")
balance = 1000 
while True:
    print("\n1. Check Balance")
    print("2. Depodit Money")
    print("3. withdraw Money")
    print("4. Exit") 
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Current Balance: ₹",balance)
    
    elif choice == 2:
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount 
        print("Amount Deposited Successfully!")
        print("Updated Balance: ₹",balance)
    
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹"))
        
        if amount <= balance:
            balance -= amount 
            print("Withdraw Successfull!")
            print("Remaining Balance: ₹",balance)
        
    elif choice == 4:
        print("Thank you for using ATM Simulation!")
        break 
    else:
        print("Invalid Choice! Please enter 1, 2, 3, or 4.")
            
        