import numpy as np

def display_menu():
    print("\n--- Basic Calculator ---")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Matrix Multiplication")
    print("6.Element Wise Operations")
    print("7.Trigonometric Functions")
    print("8.Exit")

# Creating a Function taking Two user inputs
def get_two_inputs():
    a = np.array(eval(input("Enter First Array:")))
    b = np.array(eval(input("Enter second Array:")))

    return a, b

# Calculator Function
def calculator():
    while True:
        display_menu()
        choice = input("Enter your choice:")

        if choice == "1":
            a, b = get_two_inputs()
            print("Result: ", np.add(a,b))

        elif choice == "2":
            a, b = get_two_inputs()
            print("Result: ", np.subtract(a,b))

        elif choice == "3":
            a, b = get_two_inputs()
            print("Result: ", np.multiply(a,b))

        elif choice == "4":
            a, b = get_two_inputs()
            try:
                print("Result: ", np.divide(a,b))
            except ZeroDivisionError:
                print("Error: Divison by Zero")

        elif choice == "5":    # Matrix Multiplication
            a = np.array(eval(input("enter the first matrix:")))
            b = np.array(eval(input("Enter the second matrix:")))

            try:
                print("result is :\n", np.matmul(a,b))
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "6":
            print("1.Add a constant\n  2.Multiply by a constant\n  3. Square elements")
            sub_choice = input("chosse an element wise operations:")
            a = np.array(eval(input("Enter the array:")))


            if sub_choice == "1":
                const = float(input("Enter the constant to add:"))
                print("Result:", a + const)
            elif sub_choice == "2":
                const = float(input("Enter the constant to multiply:"))
                print("Result:", np.square(a))
            else:
                print("Invalid choice")

        elif choice == "7":
            print("1. Sine\n   2. Cosine\n   3. Tangent")
            sub_choice = input("Choose a trigonometric function")
            a = np.array(eval(input("Enter the array in radians")))

            if sub_choice == "1":
                print("Result is: ", np.sin(a))
            elif sub_choice == "2":
                print("Result is ", np.cos(a))
            elif sub_choice == "3":
                print("Result is :", np.tan(a))
            else:
                print("Invalid Choice")

        elif choice == "8":
            print("Exiting the Calculator.Goodbye!")
            break
        else:
            print("Invalid option")

calculator()







