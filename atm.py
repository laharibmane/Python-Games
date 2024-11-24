class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
Hello! How would you like to proceed?
1. Create PIN
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
Enter your choice: """)
            
            if user_input == "1":
                self.create_pin()
            elif user_input =="2":
                self.deposit()
            elif user_input =="3":
                self.withdraw()
            elif user_input =="4":
                self.check_balance()
            elif user_input =="5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

    def create_pin(self):
        self.pin = input("Set your PIN: ")
        print("PIN created successfully!")

    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"Deposit successful! Your new balance is {self.balance}.")
        else:
            print("Invalid PIN.")

    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful! Your new balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid PIN.")

    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print(f"Your current balance is {self.balance}.")
        else:
            print("Invalid PIN.")


# Create an instance of the ATM class to start the program
atm = ATM()

    
