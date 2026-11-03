def check_password(password):

    if len(password) < 8:
        return "Invalid Password: Minimum 8 characters required"

    if not any(ch.isupper() for ch in password):
        return "Invalid Password: One uppercase letter required"

    if not any(ch.islower() for ch in password):
        return "Invalid Password: One lowercase letter required"

    if not any(ch.isdigit() for ch in password):
        return "Invalid Password: One digit required"

    if not any(not ch.isalnum() for ch in password):
        return "Invalid Password: One special character required"

    return "Valid Password"


print(check_password("Hello@123"))