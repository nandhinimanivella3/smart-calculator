
def smart_calculator():

    print("Welcome to Smart Calculator")
    print("================================")
    print("       SMART CALCULATOR")

    while True:
        print("\nSelect an Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Percentage (%)")
        print("6. Exit")

        choice = input("\nEnter Your Choice (1-6): ")

        if choice == "6":
            print("Thank you for using Smart Calculator")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice! Please try again.")
            continue

        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            if choice == "1":
                result = num1 + num2
                print("Addition =", result)

            elif choice == "2":
                result = num1 - num2
                print("Subtraction =", result)

            elif choice == "3":
                result = num1 * num2
                print("Multiplication =", result)

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by Zero!")
                else:
                    print("Division =", num1 / num2)

            elif choice == "5":
                result = (num1 * num2) / 100
                print("Percentage =", result)

        except ValueError:
            print("Please enter valid numbers!")


smart_calculator()
