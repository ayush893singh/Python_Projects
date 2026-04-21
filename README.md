## ATM Management System (Python)

## Technology Used
Python 3
OOP (Object-Oriented Programming)
File Handling (for transaction storage)
Datetime module (for timestamps)

## How It Works
This is a simple console-based ATM system where users can:

🔹 1. Create Account
Enter details like:
Name
Account Number
IFSC Code
Bank Name
Date of Birth
PIN
Account gets stored in memory (dictionary)

🔹 2. Login
User logs in using:
Account Number
PIN
If correct → access ATM menu

🔹 3. ATM Features
After login, user can:
Check Balance
Deposit Money
Withdraw Money
View Full Transaction History
Mini Statement (Last 3 transactions)
View Account Details
Logout

🔹 4. Transaction Handling
Every transaction is:
Stored in memory (history)
Saved in a file → accountnumber_transactions.txt
Each entry includes:
Date & Time
Transaction type
Amount

## Features
Simple & beginner-friendly
File-based transaction storage
Mini statement support
Error handling for invalid inputs
Menu-driven interface


## Sample Output
```
===== MAIN MENU =====
1. Create Account
2. Login
3. Exit
Enter your choice: 1

===== CREATE ACCOUNT =====
Enter your name: Ayush
Enter account number: 12345
Enter IFSC code: SBI0001
Enter Bank Name: SBI
Enter Date of Birth (DD-MM-YYYY): 01-01-2000
Set your PIN: 1234
Account created successfully!

===== MAIN MENU =====
Enter your choice: 2

===== LOGIN =====
Enter account number: 12345
Enter PIN: 1234

Welcome, Ayush!

===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Mini Statement
6. Account Details
7. Logout

Enter your choice: 2
Enter amount to deposit: 500
Deposit successful

Enter your choice: 1
21-04-2026 14:30:22 - Checked Balance: Rs 500

Enter your choice: 3
Enter amount to withdraw: 200
Withdrawal successful

Enter your choice: 4
1. 21-04-2026 14:29:10 - Deposited: Rs 500
2. 21-04-2026 14:30:22 - Checked Balance: Rs 500
3. 21-04-2026 14:31:05 - Withdrawn: Rs 200
```

 ## Output Files
 ```
Example file:
12345_transactions.txt

Contains:

21-04-2026 14:29:10 - Deposited: Rs 500
21-04-2026 14:30:22 - Checked Balance: Rs 500
21-04-2026 14:31:05 - Withdrawn: Rs 200
```

## Author
Ayush Singh
GitHub: https://github.com/ayush893singh
