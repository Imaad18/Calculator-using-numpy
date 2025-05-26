import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        self.current_operation = None
        
    def setup_window(self):
        self.root.title("Modern NumPy Calculator")
        self.root.geometry("1000x700")
        self.root.configure(bg='#0f0f23')
        self.root.resizable(True, True)
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1000 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"1000x700+{x}+{y}")
    
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure modern button style
        style.configure('Modern.TButton',
                       background='#4a69bd',
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat',
                       font=('Segoe UI', 11, 'bold'))
        
        style.map('Modern.TButton',
                 background=[('active', '#5a7bd6'),
                           ('pressed', '#3a59ad')])
        
        # Configure operation button style
        style.configure('Operation.TButton',
                       background='#e74c3c',
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat',
                       font=('Segoe UI', 11, 'bold'))
        
        style.map('Operation.TButton',
                 background=[('active', '#f75d4e'),
                           ('pressed', '#d73c2c')])
        
        # Configure special button style
        style.configure('Special.TButton',
                       background='#2ecc71',
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat',
                       font=('Segoe UI', 11, 'bold'))
        
        style.map('Special.TButton',
                 background=[('active', '#3ed882'),
                           ('pressed', '#27ae60')])
        
        # Configure sidebar button style
        style.configure('Sidebar.TButton',
                       background='#6c5ce7',
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat',
                       font=('Segoe UI', 10, 'bold'))
        
        style.map('Sidebar.TButton',
                 background=[('active', '#a29bfe'),
                           ('pressed', '#5b4bd7')])
    
    def create_widgets(self):
        # Create main container with sidebar
        container = tk.Frame(self.root, bg='#0f0f23')
        container.pack(fill='both', expand=True)
        
        # Create sidebar
        self.create_sidebar(container)
        
        # Main content frame
        main_frame = tk.Frame(container, bg='#1a1a2e')
        main_frame.pack(side='right', fill='both', expand=True, padx=(0, 20), pady=20)
        
        # Title
        title_label = tk.Label(main_frame, 
                              text="🔢 Modern NumPy Calculator",
                              font=('Segoe UI', 24, 'bold'),
                              fg='#74b9ff',
                              bg='#1a1a2e')
        title_label.pack(pady=(0, 20))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#1a1a2e')
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Array input fields
        self.create_input_section(input_frame)
        
        # Operation buttons frame
        operations_frame = tk.Frame(main_frame, bg='#1a1a2e')
        operations_frame.pack(fill='x', pady=(0, 20))
        
        self.create_operation_buttons(operations_frame)
        
        # Result display
        result_frame = tk.Frame(main_frame, bg='#1a1a2e')
        result_frame.pack(fill='both', expand=True)
        
        self.create_result_display(result_frame)
    
    def create_sidebar(self, parent):
        # Sidebar with modern gradient-like coloring
        sidebar = tk.Frame(parent, bg='#2d3436', width=250)
        sidebar.pack(side='left', fill='y', padx=(20, 20), pady=20)
        sidebar.pack_propagate(False)
        
        # Sidebar header with gradient effect
        header_frame = tk.Frame(sidebar, bg='#6c5ce7', height=80)
        header_frame.pack(fill='x', padx=10, pady=(10, 20))
        header_frame.pack_propagate(False)
        
        # Header gradient simulation with multiple frames
        gradient_colors = ['#6c5ce7', '#74b9ff', '#0984e3']
        for i, color in enumerate(gradient_colors):
            grad_frame = tk.Frame(header_frame, bg=color, height=26)
            grad_frame.pack(fill='x', pady=(i*2, 0))
        
        tk.Label(header_frame, text="⚡ CALCULATOR", 
                font=('Segoe UI', 14, 'bold'), fg='white', bg='#6c5ce7').place(relx=0.5, rely=0.5, anchor='center')
        
        # Navigation section
        nav_label = tk.Label(sidebar, text="🧭 NAVIGATION", 
                            font=('Segoe UI', 12, 'bold'), fg='#a29bfe', bg='#2d3436')
        nav_label.pack(pady=(0, 10), padx=20, anchor='w')
        
        # Navigation buttons with cool colors
        nav_buttons = [
            ("🏠 Dashboard", self.show_dashboard, '#fd79a8'),
            ("📊 Operations", self.show_operations, '#fdcb6e'),
            ("🔧 Settings", self.show_settings, '#6c5ce7'),
            ("📈 History", self.show_history, '#00b894')
        ]
        
        for text, command, color in nav_buttons:
            btn_frame = tk.Frame(sidebar, bg='#2d3436')
            btn_frame.pack(fill='x', padx=15, pady=2)
            
            btn = tk.Button(btn_frame, text=text, command=command,
                           bg=color, fg='white', relief='flat', bd=0,
                           font=('Segoe UI', 10, 'bold'), cursor='hand2',
                           activebackground=self.lighten_color(color))
            btn.pack(fill='x', ipady=8)
        
        # Quick actions section
        tk.Label(sidebar, text="⚡ QUICK ACTIONS", 
                font=('Segoe UI', 12, 'bold'), fg='#a29bfe', bg='#2d3436').pack(pady=(30, 10), padx=20, anchor='w')
        
        quick_actions = [
            ("🎯 Example Arrays", self.load_examples, '#e17055'),
            ("🧹 Clear All", self.clear_all, '#d63031'),
            ("💾 Save Result", self.save_result, '#00b894'),
            ("📋 Copy Result", self.copy_result, '#0984e3')
        ]
        
        for text, command, color in quick_actions:
            btn_frame = tk.Frame(sidebar, bg='#2d3436')
            btn_frame.pack(fill='x', padx=15, pady=2)
            
            btn = tk.Button(btn_frame, text=text, command=command,
                           bg=color, fg='white', relief='flat', bd=0,
                           font=('Segoe UI', 9, 'bold'), cursor='hand2',
                           activebackground=self.lighten_color(color))
            btn.pack(fill='x', ipady=6)
        
        # Status section at bottom
        status_frame = tk.Frame(sidebar, bg='#636e72', height=60)
        status_frame.pack(side='bottom', fill='x', padx=10, pady=10)
        status_frame.pack_propagate(False)
        
        tk.Label(status_frame, text="🟢 Ready", 
                font=('Segoe UI', 10, 'bold'), fg='#00b894', bg='#636e72').pack(pady=5)
        tk.Label(status_frame, text="NumPy Calculator v2.0", 
                font=('Segoe UI', 8), fg='#ddd', bg='#636e72').pack()
    
    def lighten_color(self, color):
        """Lighten a hex color for hover effects"""
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        lightened = tuple(min(255, int(c * 1.2)) for c in rgb)
        return f"#{lightened[0]:02x}{lightened[1]:02x}{lightened[2]:02x}"
    
    # Sidebar button functions
    def show_dashboard(self):
        self.display_info("🏠 Dashboard", "Welcome to NumPy Calculator Dashboard!\nAll operations are available in the main area.")
    
    def show_operations(self):
        self.display_info("📊 Operations", "Available Operations:\n• Basic: +, -, ×, ÷\n• Matrix Operations\n• Element-wise Operations\n• Trigonometric Functions")
    
    def show_settings(self):
        self.display_info("🔧 Settings", "Settings:\n• Theme: Dark Mode\n• Precision: Auto\n• Arrays: Dynamic Size\n• Format: NumPy Arrays")
    
    def show_history(self):
        self.display_info("📈 History", "Calculation History:\nAll your calculations are displayed in the results area.\nUse scroll to view previous calculations.")
    
    def load_examples(self):
        self.array_a_entry.delete('1.0', 'end')
        self.array_b_entry.delete('1.0', 'end')
        self.array_a_entry.insert('1.0', '[[1, 2, 3], [4, 5, 6]]')
        self.array_b_entry.insert('1.0', '[[7, 8, 9], [10, 11, 12]]')
        self.display_info("🎯 Examples Loaded", "Matrix examples loaded!\nTry Matrix Multiplication or other operations.")
    
    def save_result(self):
        self.display_info("💾 Save Result", "Feature: Save results to file\n(Implementation would save to .txt or .csv)")
    
    def copy_result(self):
        try:
            result_text = self.result_display.get('1.0', 'end-1c')
            self.root.clipboard_clear()
            self.root.clipboard_append(result_text)
            self.display_info("📋 Copied", "Results copied to clipboard!")
        except:
            self.display_info("📋 Copy Failed", "Could not copy to clipboard.")
    
    def display_info(self, title, message):
        self.result_display.insert('end', f"\n{'='*40}\n")
        self.result_display.insert('end', f"ℹ️ {title}\n")
        self.result_display.insert('end', f"{message}\n")
        self.result_display.see('end')
    
    def create_input_section(self, parent):
        # Input section with modern styling
        input_container = tk.Frame(parent, bg='#16213e', relief='flat', bd=2)
        input_container.pack(fill='x', pady=10)
        
        # Array A input
        tk.Label(input_container, text="Array A:", 
                font=('Segoe UI', 12, 'bold'), fg='#ddd6fe', bg='#16213e').pack(anchor='w', padx=15, pady=(15, 5))
        
        self.array_a_entry = tk.Text(input_container, height=3, font=('Consolas', 10),
                                    bg='#2d3748', fg='#e2e8f0', insertbackground='white',
                                    relief='flat', bd=0)
        self.array_a_entry.pack(fill='x', padx=15, pady=(0, 10))
        self.array_a_entry.insert('1.0', '[1, 2, 3]')
        
        # Array B input
        tk.Label(input_container, text="Array B:", 
                font=('Segoe UI', 12, 'bold'), fg='#ddd6fe', bg='#16213e').pack(anchor='w', padx=15, pady=(5, 5))
        
        self.array_b_entry = tk.Text(input_container, height=3, font=('Consolas', 10),
                                    bg='#2d3748', fg='#e2e8f0', insertbackground='white',
                                    relief='flat', bd=0)
        self.array_b_entry.pack(fill='x', padx=15, pady=(0, 15))
        self.array_b_entry.insert('1.0', '[4, 5, 6]')
    
    def create_operation_buttons(self, parent):
        # Create a grid of modern operation buttons
        button_frame = tk.Frame(parent, bg='#1a1a2e')
        button_frame.pack()
        
        # Basic operations
        basic_ops = [
            ("➕ Add", self.add_arrays, 'Operation.TButton'),
            ("➖ Subtract", self.subtract_arrays, 'Operation.TButton'),
            ("✖️ Multiply", self.multiply_arrays, 'Operation.TButton'),
            ("➗ Divide", self.divide_arrays, 'Operation.TButton')
        ]
        
        for i, (text, command, style) in enumerate(basic_ops):
            btn = ttk.Button(button_frame, text=text, command=command, style=style, width=15)
            btn.grid(row=0, column=i, padx=5, pady=5, sticky='ew')
        
        # Advanced operations
        advanced_ops = [
            ("🔢 Matrix Multiply", self.matrix_multiply, 'Modern.TButton'),
            ("📊 Element-wise Ops", self.show_elementwise_menu, 'Modern.TButton'),
            ("📐 Trigonometric", self.show_trig_menu, 'Modern.TButton'),
            ("🧹 Clear All", self.clear_all, 'Special.TButton')
        ]
        
        for i, (text, command, style) in enumerate(advanced_ops):
            btn = ttk.Button(button_frame, text=text, command=command, style=style, width=15)
            btn.grid(row=1, column=i, padx=5, pady=5, sticky='ew')
        
        # Configure grid weights
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def create_result_display(self, parent):
        # Result display with modern styling
        result_container = tk.Frame(parent, bg='#16213e', relief='flat', bd=2)
        result_container.pack(fill='both', expand=True, pady=10)
        
        tk.Label(result_container, text="📋 Results:", 
                font=('Segoe UI', 14, 'bold'), fg='#10b981', bg='#16213e').pack(anchor='w', padx=15, pady=(15, 10))
        
        self.result_display = scrolledtext.ScrolledText(
            result_container,
            font=('Consolas', 11),
            bg='#0f172a',
            fg='#64748b',
            insertbackground='white',
            relief='flat',
            bd=0,
            height=15
        )
        self.result_display.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        # Add welcome message
        welcome_msg = """🚀 Welcome to Modern NumPy Calculator!

📝 Instructions:
• Enter arrays in Python list format: [1, 2, 3] or [[1, 2], [3, 4]]
• Use buttons to perform operations
• Results will appear here with beautiful formatting

✨ Try some examples:
Array A: [1, 2, 3]    Array B: [4, 5, 6]
Array A: [[1, 2], [3, 4]]    Array B: [[5, 6], [7, 8]]

Ready to calculate! 🎯
"""
        self.result_display.insert('1.0', welcome_msg)
    
    def get_arrays(self):
        try:
            a_text = self.array_a_entry.get('1.0', 'end-1c').strip()
            b_text = self.array_b_entry.get('1.0', 'end-1c').strip()
            
            a = np.array(eval(a_text))
            b = np.array(eval(b_text))
            
            return a, b
        except Exception as e:
            messagebox.showerror("Input Error", f"Invalid array format:\n{str(e)}")
            return None, None
    
    def get_single_array(self):
        try:
            a_text = self.array_a_entry.get('1.0', 'end-1c').strip()
            a = np.array(eval(a_text))
            return a
        except Exception as e:
            messagebox.showerror("Input Error", f"Invalid array format:\n{str(e)}")
            return None
    
    def display_result(self, operation, result, arrays=None):
        self.result_display.insert('end', f"\n{'='*50}\n")
        self.result_display.insert('end', f"🔸 Operation: {operation}\n")
        
        if arrays:
            self.result_display.insert('end', f"📥 Input Arrays:\n")
            for i, arr in enumerate(arrays, 1):
                self.result_display.insert('end', f"   Array {chr(64+i)}: {arr}\n")
        
        self.result_display.insert('end', f"📤 Result:\n{result}\n")
        self.result_display.see('end')
    
    def add_arrays(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = np.add(a, b)
                self.display_result("Addition ➕", result, [a, b])
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
    
    def subtract_arrays(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = np.subtract(a, b)
                self.display_result("Subtraction ➖", result, [a, b])
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
    
    def multiply_arrays(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = np.multiply(a, b)
                self.display_result("Element-wise Multiplication ✖️", result, [a, b])
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
    
    def divide_arrays(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = np.divide(a, b)
                self.display_result("Division ➗", result, [a, b])
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
    
    def matrix_multiply(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = np.matmul(a, b)
                self.display_result("Matrix Multiplication 🔢", result, [a, b])
            except Exception as e:
                messagebox.showerror("Matrix Error", f"Matrix multiplication error:\n{str(e)}")
    
    def show_elementwise_menu(self):
        # Create a popup window for element-wise operations
        popup = tk.Toplevel(self.root)
        popup.title("Element-wise Operations")
        popup.geometry("400x300")
        popup.configure(bg='#1a1a2e')
        popup.transient(self.root)
        popup.grab_set()
        
        # Center the popup
        popup.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 200
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 150
        popup.geometry(f"400x300+{x}+{y}")
        
        tk.Label(popup, text="📊 Element-wise Operations", 
                font=('Segoe UI', 16, 'bold'), fg='#74b9ff', bg='#1a1a2e').pack(pady=20)
        
        # Constant input
        const_frame = tk.Frame(popup, bg='#1a1a2e')
        const_frame.pack(pady=10)
        
        tk.Label(const_frame, text="Constant:", font=('Segoe UI', 12), fg='white', bg='#1a1a2e').pack(side='left')
        const_entry = tk.Entry(const_frame, font=('Segoe UI', 12), bg='#2d3748', fg='white', insertbackground='white')
        const_entry.pack(side='left', padx=10)
        const_entry.insert(0, "2")
        
        # Operation buttons
        ops = [
            ("➕ Add Constant", lambda: self.elementwise_add_const(float(const_entry.get()), popup)),
            ("✖️ Multiply by Constant", lambda: self.elementwise_mult_const(float(const_entry.get()), popup)),
            ("🔲 Square Elements", lambda: self.elementwise_square(popup))
        ]
        
        for text, command in ops:
            ttk.Button(popup, text=text, command=command, style='Modern.TButton').pack(pady=5)
    
    def elementwise_add_const(self, const, popup):
        a = self.get_single_array()
        if a is not None:
            try:
                result = a + const
                self.display_result(f"Add Constant ({const}) ➕", result, [a])
                popup.destroy()
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
    
    def elementwise_mult_const(self, const, popup):
        a = self.get_single_array()
        if a is not None:
            try:
                result = a * const
                self.display_result(f"Multiply by Constant ({const}) ✖️", result, [a])
                popup.destroy()
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
    
    def elementwise_square(self, popup):
        a = self.get_single_array()
        if a is not None:
            try:
                result = np.square(a)
                self.display_result("Square Elements 🔲", result, [a])
                popup.destroy()
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
    
    def show_trig_menu(self):
        # Create a popup window for trigonometric operations
        popup = tk.Toplevel(self.root)
        popup.title("Trigonometric Functions")
        popup.geometry("400x300")
        popup.configure(bg='#1a1a2e')
        popup.transient(self.root)
        popup.grab_set()
        
        # Center the popup
        popup.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 200
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 150
        popup.geometry(f"400x300+{x}+{y}")
        
        tk.Label(popup, text="📐 Trigonometric Functions", 
                font=('Segoe UI', 16, 'bold'), fg='#74b9ff', bg='#1a1a2e').pack(pady=20)
        
        tk.Label(popup, text="⚠️ Input should be in radians", 
                font=('Segoe UI', 10), fg='#ffa502', bg='#1a1a2e').pack(pady=5)
        
        # Operation buttons
        ops = [
            ("📈 Sine", lambda: self.trig_function(np.sin, "Sine", popup)),
            ("📊 Cosine", lambda: self.trig_function(np.cos, "Cosine", popup)),
            ("📉 Tangent", lambda: self.trig_function(np.tan, "Tangent", popup))
        ]
        
        for text, command in ops:
            ttk.Button(popup, text=text, command=command, style='Modern.TButton').pack(pady=10)
    
    def trig_function(self, func, name, popup):
        a = self.get_single_array()
        if a is not None:
            try:
                result = func(a)
                self.display_result(f"{name} Function 📐", result, [a])
                popup.destroy()
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
    
    def clear_all(self):
        self.array_a_entry.delete('1.0', 'end')
        self.array_b_entry.delete('1.0', 'end')
        self.result_display.delete('1.0', 'end')
        
        # Add welcome message back
        welcome_msg = """🚀 Calculator cleared! Ready for new calculations.

✨ Enter your arrays and choose an operation.
"""
        self.result_display.insert('1.0', welcome_msg)

def main():
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
