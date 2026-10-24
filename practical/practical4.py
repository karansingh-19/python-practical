# Practical 4 :

# Accept a character
ch = input("Enter a character: ")

# Validate that exactly one character is entered
if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    # a. Check type of character
    if ch.isalpha():
        print(ch, "is a letter.")

        # b. Uppercase or lowercase
        if ch.isupper():
            print("It is an uppercase letter.")
        else:
            print("It is a lowercase letter.")

    elif ch.isdigit():
        print(ch, "is a numeric digit.")

        # c. Print digit name in text
        names = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
                 "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        print("In words:", names[int(ch)])

    else:
        print(ch, "is a special character.")