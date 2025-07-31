def validate_email(email):
    return True
    #in progress

def validate_password(password):
    return True
    #in progress

email=input("Enter email : ")
password=input("Enter password : ")

maill=validate_email(email)
passw=validate_password(password)

if maill==True and passw==True:
    print(f"you logined successfully !.")
elif maill==False and passw==False:
    print(f"your email and password is in incorrect format !.")
elif maill==False:
    print(f"your email is in incorrect format !.")
else:
    print(f"your email and password is in incorrect format !.")
    #hi