print("Select an operation to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input()

try:
    if operation == "1":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The sum is", int(num1) + int(num2))
    elif operation == "2":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The difference is", str(int(num1) - int(num2)))
    elif operation == "3":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The product is", str(int(num1) * int(num2)))
    elif operation == "4":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is", str(int(num1) / int(num2)))
    else:
        print("Invalid Entry")
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")    