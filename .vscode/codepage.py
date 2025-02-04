a = input("Welcome to Search.org.vn! Have you signed up yet?")
if a == "no":
    print("Well then, sign up!")
    d = input("What's your desirable username?")
    p = input("What's your password?")
    print("Now login!")
    while True:
        login = input("type your username:")
        login_password = input("type your password:")
        if login != d or login_password != p:
            print("oops! try again")
            continue
        
        print("Welcome back!")
        break