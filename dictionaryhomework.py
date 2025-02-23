usernames = {
    "Alex":"Itsme102",
    "Josh":"The_best0987",
    "Mary":"Let_me_in",
    "Martin":"open_up",
    "Harry":"Potter_2001",
    "Anna":"the_pretty123",
    "Noah":"6543210",
    "Alice":"in_the-wonderland",
    "Kevin":"21The_nerd",
    "Michael":"Jackson_2009"
}
username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username not in usernames:
    print("Invalid username. Please try another username.")
else:
    if usernames[username] == password:
        print("You are now logged into the system.")
    else:
        print("Incorrect password. Please try again.")