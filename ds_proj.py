#init db
database = {}

#add user
def add_user():
    name = input("enter user's name: ").lower()
    if name in database:
        print("user name already exists. Exitiing...")
    else:
        age = int(input("enter age: "))
        email = input("enter email: ").lower()
        hobby = list(set(input("enter hobbies with space in btw: ").lower().split()))

        database[name] = {
            'age' : age,
            'email' : email,
            'hobbies' : hobby
        }

#search user
def search_user():
    name = input("enter the name you want to search: ").lower()
    if name in database:
        print(f"user found. {name} details are as follows: ")
        print(database[name])
    else:
        print("user not found")

#delete user
def delete_user():
    name = input("enter the name of the user you want to delete: ").lower()
    if name in database:
        del database[name]
        print("user deleted from the db")
    else:
        print("user not found in the db")

#edit user
def edit_user():
    name = input("enter the name of the user you want to make edits on: ").lower()
    if name not in database:
        print("user not found in the db")
    else:
        print("the following details are needed:")
        age = int(input("enter the updated age: "))
        email = input("enter the updated email address: ").lower()
        hobby = list(set(input("enter the updated hobbies: ").lower().split()))

        database[name] = {
            'age' : age,
            'email' : email,
            'hobbies' : hobby
        }

#display main actions
def display_options():
    print("this is a database")
    print("the options are: 1 - add user 2 - search user 3 - delete user 4 - edit user 5 - exit")

#loop
while True:
    display_options()
    choice = input("enter your choice: ")
    if choice == '1':
        add_user()
    elif choice == '2':
        search_user()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        edit_user()
    elif choice == '5':
        break
    else:
        print("invalid choice, pls enter the right option")
    
print("exiting...")