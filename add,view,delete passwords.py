master_pwd=input("Enter your master password: ")
mp= "1234"
sec_code="5678"


def view_passwords():
    with open("passwords.txt","r") as f:
    
        for line in f.readlines():
            print(line.rstrip())


def add_password():
    website=input("Enter the website name: ")
    username=input("Enter your username/email: ")
    password=input("Enter your password: ")
    with open("passwords.txt","a") as f:
        f.write(f"{website} | {username} | {password}\n")
    print("\nPassword added successfully!\n")




if master_pwd==mp:
    print("Access granted!")
   
    while True:
        mode=input("\nWould you like to add a new password or view existing ones or quit? (add/view/quit): ").lower()
        if mode=="quit":
            print("Exiting the program.")
            break

        if mode=="add":
            add_password()  
            ask=input("Do you want to add another password? (yes/no): ").lower()
            while ask=="yes":
                add_password()
                ask=input("Do you want to add another password? (yes/no): ").lower()
            else:
                print("Exiting the program.")
        elif mode=="view":
            if view_passwords() == None:
                print("No passwords found.")   
                continue
            else:
                view_passwords()
        else:
            print("Invalid option. Please choose 'add', 'view', or 'quit'.")    
            continue

elif master_pwd=='delete':
    print("Are you sure you want to delete all passwords? This action cannot be undone.")
    confirm=input("Type 'yes' to confirm or 'no' to cancel: ").lower()
    if confirm=='yes':
        if input("Enter the security code to confirm deletion: ") == sec_code:
            with open("passwords.txt","w") as f:
                f.write("")
            print("All passwords deleted successfully!")
        else:
            print("Incorrect security code. Deletion aborted. Dumbass")
            exit()
    else:
        print("Deletion cancelled.")
        exit()
else:
    print("Access denied!")
    exit()



