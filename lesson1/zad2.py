login = input()
if login == "guest":
    print("Welcome")
elif login == "user":
    name = input("What is your name? ")
    print("We are glad that you have returned, " + name)
elif login == "manager":
    password = input("Please enter your password: ")
    if password == "manager123":
        print("Hi, boss")
    else:
        print("Incorrect password")
else:
    print("No such login :(")
