def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        raise ValueError("invalid email address")
    
email = input("give me your email")

try:
    validate_email(email)

    print("logged in successfully")

except ValueError as e:
    print("Invalid email, try again")



