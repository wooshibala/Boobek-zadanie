def password_check(password):
    has_digit = any(c.isdigit() for c in password)
    has_special_char = any(c in "№#%!$@&*" for c in password)
    has_uppercase = any(c.isupper() for c in password)
    length_check = 8 <= len(password) < 15
    if not has_digit:
        print("Your password must contain at least one digit.")
    if not has_special_char:
        print("Your password must contain at least one special character.")
    if not has_uppercase:
        print("Your password must contain at least one uppercase letter.")
    if not length_check:
        print("Your password must be between 8 and 15 characters.")
    return has_digit and has_special_char and has_uppercase and length_check

while True:
    password = input("Enter a password: ")
    if password_check(password):
        print("Welcome new user!")
        break
    else:
        print("Please improve your password.")
