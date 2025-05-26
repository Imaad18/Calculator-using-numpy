import numpy as np

def display_menu():
    """Display the calculator menu options."""
    print("\nNumPy Array Calculator")
    print("1. Basic Arithmetic Operations")
    print("2. Matrix Multiplication")
    print("3. Element-wise Operations")
    print("4. Trigonometric Functions")
    print("5. Exit")

def get_array_input(prompt):
    """Get array input from user."""
    while True:
        try:
            arr_str = input(prompt)
            arr = np.array(eval(arr_str), dtype=float)
            return arr
        except:
            print("Invalid input. Please enter a valid array (e.g., [1, 2, 3] or [[1,2],[3,4]]).")

def basic_arithmetic():
    """Perform basic arithmetic operations on arrays."""
    print("\nBasic Arithmetic Operations")
    a = get_array_input("Enter first array: ")
    b = get_array_input("Enter second array: ")
    
    try:
        print("\nResults:")
        print(f"Addition: {a + b}")
        print(f"Subtraction: {a - b}")
        print(f"Multiplication: {a * b}")
        print(f"Division: {np.divide(a, b, where=b!=0)}")  # Avoid division by zero
    except ValueError as e:
        print(f"Error: {e}. Make sure arrays have compatible shapes.")
    except Exception as e:
        print(f"An error occurred: {e}")

def matrix_multiplication():
    """Perform matrix multiplication."""
    print("\nMatrix Multiplication")
    a = get_array_input("Enter first matrix: ")
    b = get_array_input("Enter second matrix: ")
    
    try:
        result = np.matmul(a, b)
        print("\nMatrix Multiplication Result:")
        print(result)
    except ValueError as e:
        print(f"Error: {e}. Inner dimensions must match for matrix multiplication.")
    except Exception as e:
        print(f"An error occurred: {e}")

def elementwise_operations():
    """Perform element-wise operations on an array."""
    print("\nElement-wise Operations")
    a = get_array_input("Enter an array: ")
    
    print("\nResults:")
    print(f"Element-wise addition with 5: {a + 5}")
    print(f"Element-wise multiplication with 2: {a * 2}")
    print(f"Element-wise square: {np.square(a)}")
    print(f"Element-wise square root: {np.sqrt(np.abs(a))}")  # Avoid sqrt of negative numbers

def trigonometric_functions():
    """Compute trigonometric functions for array values."""
    print("\nTrigonometric Functions (input in radians)")
    a = get_array_input("Enter an array: ")
    
    print("\nResults:")
    print(f"Sine: {np.sin(a)}")
    print(f"Cosine: {np.cos(a)}")
    print(f"Tangent: {np.tan(a)}")

def main():
    """Main calculator function."""
    print("Welcome to the NumPy Array Calculator!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            basic_arithmetic()
        elif choice == '2':
            matrix_multiplication()
        elif choice == '3':
            elementwise_operations()
        elif choice == '4':
            trigonometric_functions()
        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
