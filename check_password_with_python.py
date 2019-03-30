with open("password.txt","r") as f:
    password = f.read()
    print("enter the password")
    typedpassword = input()
    if typedpassword == password:
        print("access granted")
        if password == '12345':
            print("this is a stupid password")
    else:
        print("access denied")
