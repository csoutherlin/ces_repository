import string

def is_strong_password(password):
    # Criteria
    has_special = any(char in string.punctuation for char in password)
    has_number = any(char.isdigit() for char in password)
    length_valid = len(password) >= 7
    
    # Check criteria
    if has_special and has_number and length_valid:
        return True
    else:
        feedback = []
        if not has_special:
            feedback.append("missing special character")
        if not has_number:
            feedback.append("missing number")
        if not length_valid:
            feedback.append("too short (minimum 7 characters)")
        
        print("Password is weak. Reasons:")
        for reason in feedback:
            print("-", reason)
        
        return False

def main():
    attempts = 3
    while attempts > 0:
        password = input("Enter your password: ")
        if is_strong_password(password):
            print("Congratulations! Your password is strong.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Please try again. {attempts} attempts remaining.")
            else:
                print("You have exceeded the maximum number of attempts. Please try again later.")

if __name__ == "__main__":
    print("Welcome to the Strong Password Checker.")
    print("A strong password must meet the following criteria:")
    print("- It must include at least 1 special character")
    print("- It must be at least 7 characters long")
    print("- It must include at least 1 number")
    main()
