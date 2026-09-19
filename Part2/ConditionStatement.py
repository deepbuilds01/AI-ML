username = input("Enter your name :")
password = input("Enter password :")


if(username == "admin" and password == "pass"):
    print("Loggedin Successfully!")
elif(password != "pass"):
    print("Wrong Password!") 
else:
    print("Wrong username!")