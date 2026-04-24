import os

class FileManager:

    def create_file(self):
        filename = input("Enter file name (e.g. data.txt, data.csv, data.pdf): ")

        try:
            with open(filename, "w") as file:
                file.write("")  # empty file create
            print(f"File created: {filename}")
        except Exception as e:
            print("Error:", e)

    def write_file(self):
        filename = input("Enter file name: ")
        data = input("Enter data to write: ")

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(data)
            print("Data written successfully")
        except Exception as e:
            print("Error:", e)

    def append_file(self):
        filename = input("Enter file name: ")
        data = input("Enter data to append: ")

        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write("\n" + data)
            print("Data appended successfully")
        except Exception as e:
            print("Error:", e)

    def read_file(self):
        filename = input("Enter file name: ")

        try:
            with open(filename, "r", encoding="utf-8") as file:
                print("\n===== FILE CONTENT =====")
                print(file.read())
        except Exception as e:
            print("Error:", e)

    def delete_file(self):
        filename = input("Enter file name to delete: ")

        try:
            if os.path.exists(filename):
                os.remove(filename)
                print("File deleted successfully")
            else:
                print("File not found")
        except Exception as e:
            print("Error:", e)

    def menu(self):
        while True:
            print("\n===== FILE MANAGEMENT SYSTEM =====")
            print("1. Create File")
            print("2. Write File")
            print("3. Append File")
            print("4. Read File")
            print("5. Delete File")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.create_file()
            elif choice == "2":
                self.write_file()
            elif choice == "3":
                self.append_file()
            elif choice == "4":
                self.read_file()
            elif choice == "5":
                self.delete_file()
            elif choice == "6":
                print("Bye ")
                break
            else:
                print("Invalid choice")

fm = FileManager()
fm.menu()





# ============================ xx ANIKET xx =========================================


import os

def create_file():
    filename = input("Enter file name (with extension): ")
    file = open(filename, "w")
    file.close()
    print("File created successfully")

def write_file():
    filename = input("Enter file name to write: ")
    data = input("Enter data: ")
    file = open(filename, "w")
    file.write(data)
    file.close()
    print("Data written successfully")

def append_file():
    filename = input("Enter file name to append: ")
    data = input("Enter data to add: ")
    file = open(filename, "a")
    file.write("\n" + data)
    file.close()
    print("Data appended successfully")

def read_file():
    filename = input("Enter file name to read: ")
    file = open(filename, "r")
    content = file.read()
    print("File Content:\n", content)
    file.close()

def delete_file():
    filename = input("Enter file name to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully")
    else:
        print("File does not exist")

# Menu system
while True:
    print("--- File Management System ---")
    print("1. Create File")
    print("2. Write File")
    print("3. Append File")
    print("4. Read File")
    print("5. Delete File")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_file()
    elif choice == "2":
        write_file()
    elif choice == "3":
        append_file()
    elif choice == "4":
        read_file()
    elif choice == "5":
        delete_file()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")