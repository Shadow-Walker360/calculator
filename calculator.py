
def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

    if operation in ["add", "+"]:
        result = num1 + num2
    elif operation in ["subtract", "-"]:
        result = num1 - num2
    elif operation in ["multiply", "*"]:
        result = num1 * num2
    elif operation in ["divide", "/"]:
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
        return

    print("Result:", result)


if __name__ == "__main__":
    main()
