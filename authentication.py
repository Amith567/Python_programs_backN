def validate_email(email):

    name,domain=email.split('@',1)
    if not name or not domain:
        return False,"your name or domain is null."
    if '@' not in email:
        return False,"your email doesn't contain '@'."
    if '.' not in email:
        return False,"your email doesn't contain '.'."
    
    return True,"valid email."
    

def validate_password(password):
    if len(password)<8:
        return False,"your password length is less than 8."
    if not any(let.isalpha() for let in password):
        return False,"your password doesn't contain a alphabet."
    if not any(digi.isdigit() for digi in password):
        return False,"your password doesn't contain a digit."

    
    return True,"valid password."
    

email="amith@12.3"
# input("Enter email : ")
password=input("Enter password : ")

maill,mail_msg=validate_email(email)
passw,pass_msg=validate_password(password)

if maill==True and passw==True:
    print(f"you logined successfully !.")
elif maill==True and passw==False:
    print(f"your password is in incorrect format !.{pass_msg}")
elif maill==False and passw==True:
    print(f"your email is in incorrect format !.{mail_msg}")
else:
    print(f"your email and password is in incorrect format !.{mail_msg,pass_msg}")
    