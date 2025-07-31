def validate_email(email):
    if '@'not in email:
        return False,"it doesn't contain '@' "
    name,domain=email.split('@',1)
    if '.'not in domain:
        return False,"it doesn't contain '.' "
    if not name or not domain:
        return False,"name or domain is null "
    return True,"email is valid"
def validate_password(password):
    if len(password)<8:
        return False,"password length is less than 8 "
    if not any(digi.isdigit() for digi in password):
        return False,"your password doesn't contain a digit "
    if not any(let.isalpha() for let in password):
        return False,"your password doesn't contain a alphabet"

    return True,"password is valid"

# email=input("Enter email : ")
email="nived@gmail.com"
password=input("Enter password : ")

maill,mail_msg=validate_email(email)
passw,passw_msg=validate_password(password)

if maill==True and passw==True:
    print(f"you logined successfully !.")
elif  maill==True and passw==False:
    print(f"your password is in incorrect format !.{passw_msg}")
    
elif maill==False and passw==True:
    print(f"your email is in incorrect format !.{mail_msg}")
else:    
    print(f"your email and password is in incorrect format !.")
