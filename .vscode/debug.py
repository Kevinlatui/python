
import datetime
from re import I 

current_day = datetime.datetime.now().day
current_month = datetime.datetime.now().month
current_year = datetime.datetime.now().year 





d = ""
p = ""

a = input("Welcome to Search.org.vn! Have you signed up yet?")
if a == "no":
    print("Well then, sign up!")
    d = input("What's your desirable username?")
    p = input("What's your password?")
    print(f"{current_day} - {current_month} - {current_year}")
    d_con = input("Please recheck your username:")
    p_con = input("Please recheck your pasword:")
    if d == d_con and p == p_con:
        print("Account successfully checked.")
        print("Now login!")
    else:
        print("Please try again")
    while I == True:
        login = input("type your username:")
        login_password = input("type your password:")
        if login != d or login_password != p or login != d and login_password != p and len(login) == 0 and len(login_password) == 0:
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
    
    else: 
        print("There is an error. We can't find that account. Please try again.")

print("Please continue to create a blog that you want.")
blog = input("please set up your blog:")
if (len(blog) == 0):
    print("Blog unsuccessful")
else:
    print("Processing...")
    print()
    print("Blog successful")
