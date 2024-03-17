def arithmetic_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        if operation == '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == '*':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operation!")

        choice = input("Do you want to perform another operation? (yes/no): ")
        if choice.lower() == 'yes':
            arithmetic_calculator()  # Recursively call itself for another calculation
        elif choice.lower() == 'no':
            print("Thank you for using the calculator!")
        else:
            print("Invalid choice! Exiting...")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        arithmetic_calculator()  # Recursively call itself on invalid input

arithmetic_calculator()
