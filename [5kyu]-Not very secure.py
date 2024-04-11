def alphanumeric(password: str):
    if not password:
        return False
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return False
    return True


print(alphanumeric("   "))
