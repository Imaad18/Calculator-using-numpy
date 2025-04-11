import streamlit as st
import numpy as np

st.set_page_config(page_title="Numpy Calculator", page_icon="🧮")

st.title("🧮 Basic Numpy Calculator")

menu = [
    "Add",
    "Subtract",
    "Multiply",
    "Divide",
    "Matrix Multiplication",
    "Element-wise Operations",
    "Trigonometric Functions"
]
choice = st.selectbox("Select an operation:", menu)

def get_array_input(label):
    user_input = st.text_input(label, value="[1, 2, 3]")
    try:
        arr = np.array(eval(user_input))
        return arr
    except:
        st.error("Please enter a valid Python list or array (e.g., [1, 2, 3])")
        return None

if choice in ["Add", "Subtract", "Multiply", "Divide"]:
    a = get_array_input("Enter the first array:")
    b = get_array_input("Enter the second array:")
    if a is not None and b is not None:
        if choice == "Add":
            result = np.add(a, b)
        elif choice == "Subtract":
            result = np.subtract(a, b)
        elif choice == "Multiply":
            result = np.multiply(a, b)
        elif choice == "Divide":
            try:
                result = np.divide(a, b)
            except ZeroDivisionError:
                st.error("Division by zero is not allowed.")
                result = None
        if result is not None:
            st.write("Result:", result)

elif choice == "Matrix Multiplication":
    a = get_array_input("Enter the first matrix:")
    b = get_array_input("Enter the second matrix:")
    if a is not None and b is not None:
        try:
            result = np.matmul(a, b)
            st.write("Result:", result)
        except ValueError as e:
            st.error(f"Error: {e}")

elif choice == "Element-wise Operations":
    operation = st.selectbox("Choose an element-wise operation:", ["Add a constant", "Multiply by a constant", "Square elements"])
    a = get_array_input("Enter the array:")
    if a is not None:
        if operation == "Add a constant":
            const = st.number_input("Enter the constant to add:", value=1.0)
            result = a + const
        elif operation == "Multiply by a constant":
            const = st.number_input("Enter the constant to multiply:", value=2.0)
            result = a * const
        elif operation == "Square elements":
            result = np.square(a)
        st.write("Result:", result)

elif choice == "Trigonometric Functions":
    func = st.selectbox("Choose a trigonometric function:", ["Sine", "Cosine", "Tangent"])
    a = get_array_input("Enter the array in radians:")
    if a is not None:
        if func == "Sine":
            result = np.sin(a)
        elif func == "Cosine":
            result = np.cos(a)
        elif func == "Tangent":
            result = np.tan(a)
        st.write("Result:", result)
