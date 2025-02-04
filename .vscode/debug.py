from re import I

d = ""
p = ""

a = input("Welcome to Search.org.vn! Have you signed up yet?")
if a == "no":
    print("Well then, sign up!")
    d = input("What's your desirable username?")
    p = input("What's your password?")
    print("Now login!")
    while I == True:
        login = input("type your username:")
        login_password = input("type your password:")
        if login != d or login_password != p or login != d and login_password != p:
            print("oops! try again")
            continue
        a = input("Welcome to Search.org.vn! Have you signed up yet?")
        if a == "yes":
            loginrep = input("pls enter your username")
            loginpass = input("pls enter your pass:")
        if loginrep == d and loginpass == p:
            print("Welcome back!")
        else:
            print("Try again. We can't find this page....")
elif a == "yes":
    loginrep = input("pls enter your username")
    loginpass = input("pls enter your pass:")
    if loginrep == d and loginpass == p:
        print("Welcome back!")