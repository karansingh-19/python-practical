# Practical 13 : 

class InvalidNameError(Exception):
    """Raised when the name contains digits or special characters."""
    pass

def validate_name(name):
    """Raise an exception if the name has digits or special characters."""
    if name.strip() == "":
        raise InvalidNameError("Name cannot be empty.")

    for ch in name:
        if ch.isdigit():
            raise InvalidNameError("Name cannot contain digits.")
        if not (ch.isalpha() or ch == " "):
            raise InvalidNameError("Name cannot contain special characters.")

# Main program
try:
    name = input("Enter your name: ")
    validate_name(name)
    print("Hello,", name + "! Your name is valid.")
except InvalidNameError as e:
    print("Invalid name:", e)
finally:
    print("Program finished.")