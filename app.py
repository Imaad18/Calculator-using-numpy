import numpy as np
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(
    page_title="Advanced NumPy Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
# Modernized CSS with fresh color combos
st.markdown("""
<style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background: linear-gradient(to right, #667eea, #764ba2);
        background-attachment: fixed;
        background-size: cover;
        color: #ffffff;
    }
    .css-1aumxhk, .stExpander > div > div {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        color: #ffffff;
    }
    .stButton>button {
        background: #00cec9;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        padding: 0.6rem 1.2rem;
        border: none;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background: #00b894;
        transform: scale(1.05);
        box-shadow: 0 0 10px #00cec9;
    }
    .stSelectbox, .stTextArea, .stRadio, .stNumberInput, .stTextInput {
        background-color: white;
        border-radius: 8px;
    }
    .block-container {
        padding: 2rem 3rem;
    }
</style>
""", unsafe_allow_html=True)
def main():
    # Header with logo
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://numpy.org/images/logo.svg", width=80)
    with col2:
        st.title("Advanced NumPy Calculator")
        st.caption("Perform scientific computations with ease")

    # Initialize session state
    if 'array_a' not in st.session_state:
        st.session_state.array_a = np.array([1, 2, 3])
    if 'array_b' not in st.session_state:
        st.session_state.array_b = np.array([3, 2, 1])
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Sidebar menu
    with st.sidebar:
        st.header("🔧 Menu")
        operation = st.selectbox(
            "Select Operation Category",
            [
                "Basic Arithmetic",
                "Matrix Operations",
                "Element-wise Operations",
                "Trigonometric Functions",
                "Exponential/Logarithmic",
                "Statistical Operations",
                "Linear Algebra",
                "Array Visualization"
            ]
        )

        st.markdown("---")
        st.header("📊 Array Configuration")
        array_type = st.radio(
            "Array Type",
            ["1D Array", "2D Matrix"],
            index=0
        )

        if array_type == "1D Array":
            default_a = "[1, 2, 3]"
            default_b = "[3, 2, 1]"
        else:
            default_a = "[[1, 2], [3, 4]]"
            default_b = "[[5, 6], [7, 8]]"

        array_a_input = st.text_area(
            "Array A (Python list format)",
            value=default_a,
            height=60 if array_type == "1D Array" else 80
        )

        array_b_input = st.text_area(
            "Array B (Python list format)",
            value=default_b,
            height=60 if array_type == "1D Array" else 80
        )

        if st.button("Update Arrays"):
            try:
                st.session_state.array_a = np.array(eval(array_a_input))
                st.session_state.array_b = np.array(eval(array_b_input))
                st.success("Arrays updated successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")

        st.markdown("---")
        st.header("ℹ️ About")
        st.info("""
        This calculator uses NumPy for advanced scientific computations.
        Enter arrays in Python list format and select operations from the menu.
        """)

    # Main content area
    st.header("🔢 Current Arrays")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("View Array A", expanded=True):
            st.write(st.session_state.array_a)
            st.caption(f"Shape: {st.session_state.array_a.shape}")
            st.caption(f"Data type: {st.session_state.array_a.dtype}")
    with col2:
        with st.expander("View Array B", expanded=True):
            st.write(st.session_state.array_b)
            st.caption(f"Shape: {st.session_state.array_b.shape}")
            st.caption(f"Data type: {st.session_state.array_b.dtype}")

    st.markdown("---")
    st.header(f"📌 {operation} Operations")

    # Operation sections
    if operation == "Basic Arithmetic":
        basic_arithmetic()
    elif operation == "Matrix Operations":
        matrix_operations()
    elif operation == "Element-wise Operations":
        elementwise_operations()
    elif operation == "Trigonometric Functions":
        trigonometric_functions()
    elif operation == "Exponential/Logarithmic":
        exponential_logarithmic()
    elif operation == "Statistical Operations":
        statistical_operations()
    elif operation == "Linear Algebra":
        linear_algebra()
    elif operation == "Array Visualization":
        array_visualization()

    # History section
    if st.session_state.history:
        st.markdown("---")
        st.header("📜 Operation History")
        for i, (op, result) in enumerate(reversed(st.session_state.history[-5:])):
            with st.expander(f"{i+1}. {op}"):
                st.code(f"Result:\n{result}")

def add_to_history(operation, result):
    st.session_state.history.append((operation, result))
    if len(st.session_state.history) > 10:
        st.session_state.history.pop(0)

def basic_arithmetic():
    cols = st.columns(4)
    operations = [
        ("➕ Add", "np.add(a, b)"),
        ("➖ Subtract", "np.subtract(a, b)"),
        ("✖️ Multiply", "np.multiply(a, b)"),
        ("➗ Divide", "np.divide(a, b)")
    ]

    for i, (label, func) in enumerate(operations):
        with cols[i]:
            if st.button(label):
                try:
                    a, b = st.session_state.array_a, st.session_state.array_b
                    result = eval(func)
                    st.success(f"Result:\n```\n{result}\n```")
                    add_to_history(label, result)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

def matrix_operations():
    cols = st.columns(3)
    operations = [
        ("🧮 Matrix Multiply", "np.matmul(a, b)"),
        ("🔀 Dot Product", "np.dot(a, b)"),
        ("📐 Cross Product", "np.cross(a, b)")
    ]

    for i, (label, func) in enumerate(operations):
        with cols[i]:
            if st.button(label):
                try:
                    a, b = st.session_state.array_a, st.session_state.array_b
                    result = eval(func)
                    st.success(f"Result:\n```\n{result}\n```")
                    add_to_history(label, result)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

def elementwise_operations():
    option = st.selectbox(
        "Select Operation",
        [
            "Add Constant",
            "Multiply by Constant",
            "Square Elements",
            "Square Root",
            "Absolute Value",
            "Exponentiation"
        ]
    )

    if option in ["Add Constant", "Multiply by Constant"]:
        constant = st.number_input("Enter constant value", value=1.0)

    if option == "Exponentiation":
        power = st.number_input("Enter exponent value", value=2.0)

    if st.button("Perform Operation"):
        try:
            a = st.session_state.array_a
            if option == "Add Constant":
                result = a + constant
                op_name = f"Add {constant} to array"
            elif option == "Multiply by Constant":
                result = a * constant
                op_name = f"Multiply array by {constant}"
            elif option == "Square Elements":
                result = np.square(a)
                op_name = "Square elements"
            elif option == "Square Root":
                result = np.sqrt(a)
                op_name = "Square root"
            elif option == "Absolute Value":
                result = np.abs(a)
                op_name = "Absolute value"
            elif option == "Exponentiation":
                result = np.power(a, power)
                op_name = f"Raise to power {power}"

            st.success(f"Result:\n```\n{result}\n```")
            add_to_history(op_name, result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

def trigonometric_functions():
    option = st.selectbox(
        "Select Function",
        [
            "Sine", "Cosine", "Tangent",
            "Arc Sine", "Arc Cosine", "Arc Tangent",
            "Hyperbolic Sine", "Hyperbolic Cosine", "Hyperbolic Tangent"
        ]
    )

    if st.button("Calculate"):
        try:
            a = st.session_state.array_a
            if option == "Sine":
                result = np.sin(a)
            elif option == "Cosine":
                result = np.cos(a)
            elif option == "Tangent":
                result = np.tan(a)
            elif option == "Arc Sine":
                result = np.arcsin(a)
            elif option == "Arc Cosine":
                result = np.arccos(a)
            elif option == "Arc Tangent":
                result = np.arctan(a)
            elif option == "Hyperbolic Sine":
                result = np.sinh(a)
            elif option == "Hyperbolic Cosine":
                result = np.cosh(a)
            elif option == "Hyperbolic Tangent":
                result = np.tanh(a)

            st.success(f"Result:\n```\n{result}\n```")
            add_to_history(f"{option} function", result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

def exponential_logarithmic():
    option = st.selectbox(
        "Select Function",
        [
            "Exponential (e^x)",
            "Natural Log (ln)",
            "Log Base 10",
            "Log Base 2",
            "Logarithm (Custom Base)"
        ]
    )

    if option == "Logarithm (Custom Base)":
        base = st.number_input("Enter logarithm base", min_value=0.1, value=2.0)

    if st.button("Calculate"):
        try:
            a = st.session_state.array_a
            if option == "Exponential (e^x)":
                result = np.exp(a)
            elif option == "Natural Log (ln)":
                result = np.log(a)
            elif option == "Log Base 10":
                result = np.log10(a)
            elif option == "Log Base 2":
                result = np.log2(a)
            elif option == "Logarithm (Custom Base)":
                result = np.log(a) / np.log(base)

            st.success(f"Result:\n```\n{result}\n```")
            add_to_history(option, result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

def statistical_operations():
    option = st.selectbox(
        "Select Operation",
        [
            "Mean", "Median", "Standard Deviation",
            "Variance", "Min", "Max", "Sum",
            "Product", "Cumulative Sum", "Cumulative Product"
        ]
    )

    if st.button("Calculate"):
        try:
            a = st.session_state.array_a
            if option == "Mean":
                result = np.mean(a)
            elif option == "Median":
                result = np.median(a)
            elif option == "Standard Deviation":
                result = np.std(a)
            elif option == "Variance":
                result = np.var(a)
            elif option == "Min":
                result = np.min(a)
            elif option == "Max":
                result = np.max(a)
            elif option == "Sum":
                result = np.sum(a)
            elif option == "Product":
                result = np.prod(a)
            elif option == "Cumulative Sum":
                result = np.cumsum(a)
            elif option == "Cumulative Product":
                result = np.cumprod(a)

            st.success(f"Result:\n```\n{result}\n```")
            add_to_history(option, result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

def linear_algebra():
    option = st.selectbox(
        "Select Operation",
        [
            "Matrix Determinant",
            "Matrix Inverse",
            "Matrix Trace",
            "Matrix Rank",
            "Eigenvalues",
            "Matrix Norm"
        ]
    )

    if st.button("Calculate"):
        try:
            a = st.session_state.array_a
            if option == "Matrix Determinant":
                result = np.linalg.det(a)
            elif option == "Matrix Inverse":
                result = np.linalg.inv(a)
            elif option == "Matrix Trace":
                result = np.trace(a)
            elif option == "Matrix Rank":
                result = np.linalg.matrix_rank(a)
            elif option == "Eigenvalues":
                result = np.linalg.eigvals(a)
            elif option == "Matrix Norm":
                result = np.linalg.norm(a)

            st.success(f"Result:\n```\n{result}\n```")
            add_to_history(option, result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

def array_visualization():
    st.subheader("Array Visualization")

    option = st.selectbox(
        "Select Visualization Type",
        ["Line Plot", "Bar Chart", "Scatter Plot", "Histogram"]
    )

    if option in ["Line Plot", "Bar Chart", "Scatter Plot"]:
        show_both = st.checkbox("Show both arrays", value=True)

    if st.button("Generate Plot"):
        try:
            a = st.session_state.array_a
            b = st.session_state.array_b

            fig, ax = plt.subplots(figsize=(8, 4))

            if option == "Line Plot":
                ax.plot(a, label="Array A")
                if show_both:
                    ax.plot(b, label="Array B")
                ax.set_title("Line Plot")
            elif option == "Bar Chart":
                if len(a.shape) == 1:
                    x = range(len(a))
                    ax.bar(x, a, width=0.4, label="Array A")
                    if show_both and len(b.shape) == 1 and len(b) == len(a):
                        ax.bar([p + 0.4 for p in x], b, width=0.4, label="Array B")
                    elif show_both:
                        st.warning("Bar chart requires 1D arrays of the same length to show both.")
                else:
                    st.warning("Bar chart requires 1D arrays.")
                ax.set_title("Bar Chart")
                ax.set_xlabel("Index")
                ax.set_ylabel("Value")
            elif option == "Scatter Plot":
                if len(a.shape) == 1 and len(b.shape) == 1 and len(a) == len(b):
                    ax.scatter(a, b)
                    ax.set_title("Scatter Plot (Array A vs Array B)")
                    ax.set_xlabel("Array A")
                    ax.set_ylabel("Array B")
                else:
                    st.warning("Scatter plot requires two 1D arrays of the same length.")
            elif option == "Histogram":
                ax.hist(a.flatten(), bins=20, alpha=0.7, label="Array A")
                if show_both:
                    ax.hist(b.flatten(), bins=20, alpha=0.7, label="Array B")
                ax.set_title("Histogram")
                ax.set_xlabel("Value")
                ax.set_ylabel("Frequency")

            ax.legend()
            ax.grid(True)
            st.pyplot(fig)
            add_to_history(f"{option} Visualization", "Plot generated")
        except Exception as e:
            st.error(f"Error generating plot: {str(e)}")



if __name__ == "__main__":
    main()
