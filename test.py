import numpy as np
import streamlit as st

def main():
    st.title("NumPy Scientific Calculator")
    st.write("A powerful calculator using NumPy operations")
    
    # Sidebar menu
    st.sidebar.title("Menu")
    operation = st.sidebar.selectbox(
        "Select Operation",
        [
            "Basic Arithmetic",
            "Matrix Multiplication",
            "Element-wise Operations",
            "Trigonometric Functions",
            "Exponential/Logarithmic",
            "Statistical Operations"
        ]
    )
    
    # Initialize session state for arrays if not exists
    if 'array_a' not in st.session_state:
        st.session_state.array_a = np.array([1, 2, 3])
    if 'array_b' not in st.session_state:
        st.session_state.array_b = np.array([4, 5, 6])
    
    # Input section
    st.header("Input Arrays")
    col1, col2 = st.columns(2)
    
    with col1:
        array_a_input = st.text_area("Array A (Python list format)", value=str(st.session_state.array_a.tolist()))
        try:
            st.session_state.array_a = np.array(eval(array_a_input))
        except:
            st.error("Invalid input for Array A. Using default.")
    
    with col2:
        array_b_input = st.text_area("Array B (Python list format)", value=str(st.session_state.array_b.tolist()))
        try:
            st.session_state.array_b = np.array(eval(array_b_input))
        except:
            st.error("Invalid input for Array B. Using default.")
    
    # Display arrays
    st.subheader("Current Arrays")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Array A:")
        st.write(st.session_state.array_a)
    with col2:
        st.write("Array B:")
        st.write(st.session_state.array_b)
    
    # Operations
    st.header("Operations")
    
    if operation == "Basic Arithmetic":
        basic_arithmetic()
    elif operation == "Matrix Multiplication":
        matrix_multiplication()
    elif operation == "Element-wise Operations":
        elementwise_operations()
    elif operation == "Trigonometric Functions":
        trigonometric_functions()
    elif operation == "Exponential/Logarithmic":
        exponential_logarithmic()
    elif operation == "Statistical Operations":
        statistical_operations()

def basic_arithmetic():
    st.subheader("Basic Arithmetic Operations")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Add"):
            try:
                result = np.add(st.session_state.array_a, st.session_state.array_b)
                st.success(f"Result: {result}")
            except Exception as e:
                st.error(f"Error: {e}")
    
    with col2:
        if st.button("Subtract"):
            try:
                result = np.subtract(st.session_state.array_a, st.session_state.array_b)
                st.success(f"Result: {result}")
            except Exception as e:
                st.error(f"Error: {e}")
    
    with col3:
        if st.button("Multiply"):
            try:
                result = np.multiply(st.session_state.array_a, st.session_state.array_b)
                st.success(f"Result: {result}")
            except Exception as e:
                st.error(f"Error: {e}")
    
    with col4:
        if st.button("Divide"):
            try:
                result = np.divide(st.session_state.array_a, st.session_state.array_b)
                st.success(f"Result: {result}")
            except Exception as e:
                st.error(f"Error: {e}")

def matrix_multiplication():
    st.subheader("Matrix Multiplication")
    
    if st.button("Perform Matrix Multiplication"):
        try:
            result = np.matmul(st.session_state.array_a, st.session_state.array_b)
            st.success(f"Result:\n{result}")
        except ValueError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")

def elementwise_operations():
    st.subheader("Element-wise Operations")
    
    option = st.selectbox(
        "Select Operation",
        ["Add Constant", "Multiply by Constant", "Square Elements", "Square Root"]
    )
    
    if option in ["Add Constant", "Multiply by Constant"]:
        constant = st.number_input("Enter constant value", value=1.0)
    
    if st.button("Perform Operation"):
        try:
            if option == "Add Constant":
                result = st.session_state.array_a + constant
            elif option == "Multiply by Constant":
                result = st.session_state.array_a * constant
            elif option == "Square Elements":
                result = np.square(st.session_state.array_a)
            elif option == "Square Root":
                result = np.sqrt(st.session_state.array_a)
            
            st.success(f"Result:\n{result}")
        except Exception as e:
            st.error(f"Error: {e}")

def trigonometric_functions():
    st.subheader("Trigonometric Functions")
    
    option = st.selectbox(
        "Select Function",
        ["Sine", "Cosine", "Tangent", "Arc Sine", "Arc Cosine", "Arc Tangent"]
    )
    
    if st.button("Calculate"):
        try:
            if option == "Sine":
                result = np.sin(st.session_state.array_a)
            elif option == "Cosine":
                result = np.cos(st.session_state.array_a)
            elif option == "Tangent":
                result = np.tan(st.session_state.array_a)
            elif option == "Arc Sine":
                result = np.arcsin(st.session_state.array_a)
            elif option == "Arc Cosine":
                result = np.arccos(st.session_state.array_a)
            elif option == "Arc Tangent":
                result = np.arctan(st.session_state.array_a)
            
            st.success(f"Result:\n{result}")
        except Exception as e:
            st.error(f"Error: {e}")

def exponential_logarithmic():
    st.subheader("Exponential & Logarithmic Functions")
    
    option = st.selectbox(
        "Select Function",
        ["Exponential (e^x)", "Natural Log (ln)", "Log Base 10", "Log Base 2"]
    )
    
    if st.button("Calculate"):
        try:
            if option == "Exponential (e^x)":
                result = np.exp(st.session_state.array_a)
            elif option == "Natural Log (ln)":
                result = np.log(st.session_state.array_a)
            elif option == "Log Base 10":
                result = np.log10(st.session_state.array_a)
            elif option == "Log Base 2":
                result = np.log2(st.session_state.array_a)
            
            st.success(f"Result:\n{result}")
        except Exception as e:
            st.error(f"Error: {e}")

def statistical_operations():
    st.subheader("Statistical Operations")
    
    option = st.selectbox(
        "Select Operation",
        ["Mean", "Median", "Standard Deviation", "Variance", "Min", "Max", "Sum"]
    )
    
    if st.button("Calculate"):
        try:
            if option == "Mean":
                result = np.mean(st.session_state.array_a)
            elif option == "Median":
                result = np.median(st.session_state.array_a)
            elif option == "Standard Deviation":
                result = np.std(st.session_state.array_a)
            elif option == "Variance":
                result = np.var(st.session_state.array_a)
            elif option == "Min":
                result = np.min(st.session_state.array_a)
            elif option == "Max":
                result = np.max(st.session_state.array_a)
            elif option == "Sum":
                result = np.sum(st.session_state.array_a)
            
            st.success(f"Result:\n{result}")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
