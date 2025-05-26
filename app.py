import streamlit as st
import numpy as np
from typing import Union

# Custom CSS styling
def inject_css():
    st.markdown("""
    <style>
        /* Main container styling */
        .main {
            background-color: #f8f9fa;
        }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #2c3e50;
            color: white;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: #3498db;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 8px 16px;
            font-weight: bold;
        }
        
        .stButton>button:hover {
            background-color: #2980b9;
            color: white;
        }
        
        /* Header styling */
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        
        /* Input fields */
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1px solid #dfe6e9;
        }
        
        /* Success messages */
        .success {
            color: #27ae60;
            font-weight: bold;
        }
        
        /* Error messages */
        .error {
            color: #e74c3c;
            font-weight: bold;
        }
        
        /* Array display */
        .array-display {
            background-color: #ecf0f1;
            border-radius: 8px;
            padding: 10px;
            margin: 10px 0;
        }
    </style>
    """, unsafe_allow_html=True)

def display_array(arr: Union[np.ndarray, list, float]):
    """Display array in a formatted way"""
    if isinstance(arr, (np.ndarray, list)):
        with st.expander("View Array", expanded=True):
            st.write(arr)
    else:
        st.write(f"Result: {arr}")

def get_array_input(dim: int = 1) -> np.ndarray:
    """Get array input from user based on dimension"""
    arr_input = st.text_area(
        f"Enter {dim}D array (Python list format):",
        value="[1, 2, 3]" if dim == 1 else "[[1, 2], [3, 4]]",
        height=100
    )
    
    try:
        arr = np.array(eval(arr_input), dtype=float)
        if dim == 2 and arr.ndim != 2:
            st.error("Please enter a valid 2D array")
            return None
        return arr
    except Exception as e:
        st.error(f"Invalid input: {str(e)}")
        return None

def basic_arithmetic():
    """Perform basic arithmetic operations on arrays"""
    st.subheader("Basic Arithmetic Operations")
    
    col1, col2 = st.columns(2)
    with col1:
        dim = st.radio("Array Dimension", [1, 2], key="basic_dim")
        array1 = get_array_input(dim)
    
    with col2:
        array2 = get_array_input(dim)
    
    if array1 is not None and array2 is not None:
        try:
            st.subheader("Results")
            cols = st.columns(4)
            
            with cols[0]:
                st.markdown("**Addition**")
                display_array(array1 + array2)
            
            with cols[1]:
                st.markdown("**Subtraction**")
                display_array(array1 - array2)
            
            with cols[2]:
                st.markdown("**Multiplication**")
                display_array(array1 * array2)
            
            with cols[3]:
                st.markdown("**Division**")
                if np.any(array2 == 0):
                    st.error("Division by zero detected!")
                else:
                    display_array(array1 / array2)
                    
        except Exception as e:
            st.error(f"Error in operation: {str(e)}")

def matrix_multiplication():
    """Perform matrix multiplication"""
    st.subheader("Matrix Multiplication")
    
    col1, col2 = st.columns(2)
    with col1:
        matrix1 = get_array_input(2)
    
    with col2:
        matrix2 = get_array_input(2)
    
    if matrix1 is not None and matrix2 is not None:
        try:
            result = np.matmul(matrix1, matrix2)
            st.success("Matrix multiplication successful!")
            display_array(result)
        except ValueError as e:
            st.error(f"Matrix dimension mismatch: {str(e)}")

def elementwise_operations():
    """Perform element-wise operations on an array"""
    st.subheader("Element-wise Operations")
    
    dim = st.radio("Array Dimension", [1, 2], key="element_dim")
    array = get_array_input(dim)
    
    if array is not None:
        st.subheader("Results")
        
        scalar = st.number_input("Enter a scalar value:", value=2.0)
        
        cols = st.columns(3)
        with cols[0]:
            st.markdown("**Add Scalar**")
            display_array(array + scalar)
        
        with cols[1]:
            st.markdown("**Multiply by Scalar**")
            display_array(array * scalar)
        
        with cols[2]:
            st.markdown("**Power of Scalar**")
            display_array(np.power(array, scalar))
        
        st.markdown("**Other Operations**")
        cols2 = st.columns(3)
        with cols2[0]:
            st.markdown("**Square**")
            display_array(np.square(array))
        
        with cols2[1]:
            st.markdown("**Square Root**")
            display_array(np.sqrt(np.abs(array)))
        
        with cols2[2]:
            st.markdown("**Exponential**")
            display_array(np.exp(array))

def trigonometric_functions():
    """Compute trigonometric functions for array values"""
    st.subheader("Trigonometric Functions")
    
    dim = st.radio("Array Dimension", [1, 2], key="trig_dim")
    array = get_array_input(dim)
    
    if array is not None:
        st.subheader("Results (in radians)")
        
        cols = st.columns(3)
        with cols[0]:
            st.markdown("**Sine**")
            display_array(np.sin(array))
        
        with cols[1]:
            st.markdown("**Cosine**")
            display_array(np.cos(array))
        
        with cols[2]:
            st.markdown("**Tangent**")
            display_array(np.tan(array))
        
        st.markdown("**Inverse Trigonometric Functions**")
        cols2 = st.columns(3)
        with cols2[0]:
            st.markdown("**Arcsine**")
            display_array(np.arcsin(np.clip(array, -1, 1)))
        
        with cols2[1]:
            st.markdown("**Arccosine**")
            display_array(np.arccos(np.clip(array, -1, 1)))
        
        with cols2[2]:
            st.markdown("**Arctangent**")
            display_array(np.arctan(array))

def main():
    """Main application function"""
    inject_css()
    
    st.title("🧮 NumPy Array Calculator")
    st.markdown("Perform various operations on 1D and 2D arrays using NumPy")
    
    # Sidebar menu
    with st.sidebar:
        st.header("Menu")
        operation = st.radio(
            "Select Operation",
            ["Basic Arithmetic", "Matrix Multiplication", 
             "Element-wise Operations", "Trigonometric Functions"]
        )
        
        st.markdown("---")
        st.markdown("### Array Configuration")
        st.markdown("Choose operation above and configure arrays below")
    
    # Main content area
    if operation == "Basic Arithmetic":
        basic_arithmetic()
    elif operation == "Matrix Multiplication":
        matrix_multiplication()
    elif operation == "Element-wise Operations":
        elementwise_operations()
    elif operation == "Trigonometric Functions":
        trigonometric_functions()

if __name__ == "__main__":
    main()
