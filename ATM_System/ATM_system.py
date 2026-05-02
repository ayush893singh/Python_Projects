from datetime import datetime

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        print("\n===== CREATE ACCOUNT =====")
        name = input("Enter your name: ")
        acc_no = input("Enter account number: ")
        ifsc = input("Enter IFSC code: ")
        bank = input("Enter Bank Name: ")
        dob = input("Enter Date of Birth (DD-MM-YYYY): ")
        pin = input("Set your PIN: ")

        if acc_no in self.accounts:
            print("Account already exists!")
            return

        self.accounts[acc_no] = {
            "name": name,
            "ifsc": ifsc,
            "bank": bank,
            "dob": dob,
            "pin": pin,
            "balance": 0,
            "history": []
        }

        print(" Account created successfully!")

    def login(self):
        print("\n===== LOGIN =====")
        acc_no = input("Enter account number: ")
        pin = input("Enter PIN: ")

        if acc_no in self.accounts and self.accounts[acc_no]["pin"] == pin:
            print(f"\nWelcome, {self.accounts[acc_no]['name']}!")
            self.menu(acc_no)
        else:
            print(" Invalid account number or PIN")

    def menu(self, acc_no):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Mini Statement (Last 3)")
            print("6. Account Details")
            print("7. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.check_balance(acc_no)
            elif choice == '2':
                self.deposit(acc_no)
            elif choice == '3':
                self.withdraw(acc_no)
            elif choice == '4':
                self.show_history(acc_no)
            elif choice == '5':
                self.mini_statement(acc_no)
            elif choice == '6':
                self.show_details(acc_no)
            elif choice == '7':
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice.")

    def get_time(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

  
    def save_to_file(self, acc_no, text):
        try:
            filename = f"{acc_no}_transactions.txt"
            with open(filename, "a", encoding="utf-8") as file:
                file.write(text + "\n")
        except Exception as e:
            print(" File saving error:", e)

    def check_balance(self, acc_no):
        bal = self.accounts[acc_no]["balance"]
        time = self.get_time()
        msg = f"{time} - Checked Balance: Rs {bal}"
        print(msg)

        self.accounts[acc_no]["history"].append(msg)
        self.save_to_file(acc_no, msg)

    def deposit(self, acc_no):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.accounts[acc_no]["balance"] += amount
                time = self.get_time()
                msg = f"{time} - Deposited: Rs {amount}"
                print(" Deposit successful")

                self.accounts[acc_no]["history"].append(msg)
                self.save_to_file(acc_no, msg)
            else:
                print("Invalid amount")
        except:
            print(" Please enter a valid number")

    def withdraw(self, acc_no):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > self.accounts[acc_no]["balance"]:
                print(" Insufficient balance")
            elif amount <= 0:
                print("Invalid amount")
            else:
                self.accounts[acc_no]["balance"] -= amount
                time = self.get_time()
                msg = f"{time} - Withdrawn: Rs {amount}"
                print(" Withdrawal successful")

                self.accounts[acc_no]["history"].append(msg)
                self.save_to_file(acc_no, msg)
        except:
            print(" Please enter a valid number")

    def show_history(self, acc_no):
        print("\n===== TRANSACTION HISTORY =====")
        history = self.accounts[acc_no]["history"]

        if not history:
            print("No transactions yet")
        else:
            for i, h in enumerate(history, 1):
                print(f"{i}. {h}")

    def mini_statement(self, acc_no):
        print("\n===== MINI STATEMENT (LAST 3) =====")
        history = self.accounts[acc_no]["history"]

        filtered = [h for h in history if "Deposited" in h or "Withdrawn" in h]

        if not filtered:
            print("No transactions yet")
        else:
            for h in filtered[-3:]:
                print(h)

    def show_details(self, acc_no):
        acc = self.accounts[acc_no]
        print("\n===== ACCOUNT DETAILS =====")
        print(f"Name: {acc['name']}")
        print(f"Account No: {acc_no}")
        print(f"IFSC: {acc['ifsc']}")
        print(f"Bank Name: {acc['bank']}")
        print(f"DOB: {acc['dob']}")


atm = ATM()

while True:
    print("\n===== MAIN MENU =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        atm.create_account()
    elif choice == '2':
        atm.login()
    elif choice == '3':
        print("Thank you for using ATM system.")
        break
    else:
        print("Invalid choice.")
