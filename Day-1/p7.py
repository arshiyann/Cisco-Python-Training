digit = input("Enter Digit: ")

if (digit.isdigit()):
    value = int(digit) + 100
    print(f"Incremented Value Is: {value}")
else:
    print("Number is not an Integer")