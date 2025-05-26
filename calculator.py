import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.inject_css()  # Inject modern CSS-style coloring
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
    
    def inject_css(self):
        """Inject modern CSS-style coloring throughout the application"""
        # Main color palette
        self.css_colors = {
            'primary': '#6c5ce7',
            'secondary': '#a29bfe',
            'accent': '#fd79a8',
            'background': '#0f0f23',
            'card': '#1a1a2e',
            'text': '#f8f9fa',
            'success': '#00b894',
            'warning': '#fdcb6e',
            'danger': '#d63031',
            'info': '#0984e3',
            'dark': '#2d3436',
            'light': '#dfe6e9'
        }
        
        # Gradient definitions
        self.css_gradients = {
            'primary_gradient': ['#6c5ce7', '#a29bfe', '#74b9ff'],
            'danger_gradient': ['#d63031', '#ff7675', '#fd79a8'],
            'success_gradient': ['#00b894', '#55efc4', '#81ecec']
        }
        
        # Text styles
        self.css_text = {
            'h1': {'font': ('Segoe UI', 24, 'bold'), 'fg': '#74b9ff'},
            'h2': {'font': ('Segoe UI', 18, 'bold'), 'fg': '#a29bfe'},
            'h3': {'font': ('Segoe UI', 14, 'bold'), 'fg': '#dfe6e9'},
            'p': {'font': ('Segoe UI', 11), 'fg': '#b2bec3'},
            'code': {'font': ('Consolas', 10), 'fg': '#e2e8f0'}
        }
    
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure modern button style using CSS colors
        style.configure('Modern.TButton',
                       background=self.css_colors['primary'],
                       foreground=self.css_colors['text'],
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat',
                       font=('Segoe UI', 11, 'bold'))
        
        style.map('Modern.TButton',
                 background=[('active', self.lighten_color(self.css_colors['primary'], 20)),
                           ('pressed', self.darken_color(self.css_colors['primary'], 20))])
        
        # Configure operation button style
        style.configure('Operation.TButton',
                       background=self.css_colors['accent'],
                       foreground=self.css_colors['text'],
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat',
                       font=('Segoe UI', 11, 'bold'))
        
        style.map('Operation.TButton',
                 background=[('active', self.lighten_color(self.css_colors['accent'], 20)),
                           ('pressed', self.darken_color(self.css_colors['accent'], 20))])
        
        # Configure special button style
        style.configure('Special.TButton',
                       background=self.css_colors['success'],
                       foreground=self.css_colors['text'],
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat',
                       font=('Segoe UI', 11, 'bold'))
        
        style.map('Special.TButton',
                 background=[('active', self.lighten_color(self.css_colors['success'], 20)),
                           ('pressed', self.darken_color(self.css_colors['success'], 20))])
        
        # Configure sidebar button style
        style.configure('Sidebar.TButton',
                       background=self.css_colors['dark'],
                       foreground=self.css_colors['text'],
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat',
                       font=('Segoe UI', 10, 'bold'))
        
        style.map('Sidebar.TButton',
                 background=[('active', self.lighten_color(self.css_colors['dark'], 20)),
                           ('pressed', self.darken_color(self.css_colors['dark'], 20))])
    
    def create_widgets(self):
        # Create main container with sidebar
        container = tk.Frame(self.root, bg=self.css_colors['background'])
        container.pack(fill='both', expand=True)
        
        # Create sidebar
        self.create_sidebar(container)
        
        # Main content frame
        main_frame = tk.Frame(container, bg=self.css_colors['card'])
        main_frame.pack(side='right', fill='both', expand=True, padx=(0, 20), pady=20)
        
        # Title with CSS h1 style
        title_label = tk.Label(main_frame, 
                              text="🔢 Modern NumPy Calculator",
                              **self.css_text['h1'],
                              bg=self.css_colors['card'])
        title_label.pack(pady=(0, 20))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg=self.css_colors['card'])
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Array input fields
        self.create_input_section(input_frame)
        
        # Operation buttons frame
        operations_frame = tk.Frame(main_frame, bg=self.css_colors['card'])
        operations_frame.pack(fill='x', pady=(0, 20))
        
        self.create_operation_buttons(operations_frame)
        
        # Result display
        result_frame = tk.Frame(main_frame, bg=self.css_colors['card'])
        result_frame.pack(fill='both', expand=True)
        
        self.create_result_display(result_frame)
    
    def create_sidebar(self, parent):
        # Sidebar with modern gradient-like coloring
        sidebar = tk.Frame(parent, bg=self.css_colors['dark'], width=250)
        sidebar.pack(side='left', fill='y', padx=(20, 20), pady=20)
        sidebar.pack_propagate(False)
        
        # Sidebar header with gradient effect
        header_frame = tk.Frame(sidebar, bg=self.css_colors['primary'], height=80)
        header_frame.pack(fill='x', padx=10, pady=(10, 20))
        header_frame.pack_propagate(False)
        
        # Header gradient simulation with multiple frames
        for i, color in enumerate(self.css_gradients['primary_gradient']):
            grad_frame = tk.Frame(header_frame, bg=color, height=26)
            grad_frame.pack(fill='x', pady=(i*2, 0))
        
        tk.Label(header_frame, text="⚡ CALCULATOR", 
                font=('Segoe UI', 14, 'bold'), fg='white', bg=self.css_colors['primary']).place(relx=0.5, rely=0.5, anchor='center')
        
        # Navigation section
        nav_label = tk.Label(sidebar, text="🧭 NAVIGATION", 
                            **self.css_text['h3'],
                            bg=self.css_colors['dark'])
        nav_label.pack(pady=(0, 10), padx=20, anchor='w')
        
        # Navigation buttons with cool colors
        nav_buttons = [
            ("🏠 Dashboard", self.show_dashboard, self.css_colors['accent']),
            ("📊 Operations", self.show_operations, self.css_colors['warning']),
            ("🔧 Settings", self.show_settings, self.css_colors['primary']),
            ("📈 History", self.show_history, self.css_colors['success'])
        ]
        
        for text, command, color in nav_buttons:
            btn_frame = tk.Frame(sidebar, bg=self.css_colors['dark'])
            btn_frame.pack(fill='x', padx=15, pady=2)
            
            btn = tk.Button(btn_frame, text=text, command=command,
                           bg=color, fg=self.css_colors['text'], relief='flat', bd=0,
                           font=('Segoe UI', 10, 'bold'), cursor='hand2',
                           activebackground=self.lighten_color(color, 20))
            btn.pack(fill='x', ipady=8)
        
        # Quick actions section
        tk.Label(sidebar, text="⚡ QUICK ACTIONS", 
                **self.css_text['h3'],
                bg=self.css_colors['dark']).pack(pady=(30, 10), padx=20, anchor='w')
        
        quick_actions = [
            ("🎯 Example Arrays", self.load_examples, self.css_colors['warning']),
            ("🧹 Clear All", self.clear_all, self.css_colors['danger']),
            ("💾 Save Result", self.save_result, self.css_colors['success']),
            ("📋 Copy Result", self.copy_result, self.css_colors['info'])
        ]
        
        for text, command, color in quick_actions:
            btn_frame = tk.Frame(sidebar, bg=self.css_colors['dark'])
            btn_frame.pack(fill='x', padx=15, pady=2)
            
            btn = tk.Button(btn_frame, text=text, command=command,
                           bg=color, fg=self.css_colors['text'], relief='flat', bd=0,
                           font=('Segoe UI', 9, 'bold'), cursor='hand2',
                           activebackground=self.lighten_color(color, 20))
            btn.pack(fill='x', ipady=6)
        
        # Status section at bottom
        status_frame = tk.Frame(sidebar, bg=self.css_colors['dark'], height=60)
        status_frame.pack(side='bottom', fill='x', padx=10, pady=10)
        status_frame.pack_propagate(False)
        
        tk.Label(status_frame, text="🟢 Ready", 
                font=('Segoe UI', 10, 'bold'), fg=self.css_colors['success'], bg=self.css_colors['dark']).pack(pady=5)
        tk.Label(status_frame, text="NumPy Calculator v2.0", 
                font=('Segoe UI', 8), fg=self.css_colors['light'], bg=self.css_colors['dark']).pack()
    
    def lighten_color(self, color, percent=20):
        """Lighten a hex color by a given percentage"""
        if isinstance(color, str) and color.startswith('#'):
            color = color.lstrip('#')
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            lightened = tuple(min(255, int(c + (255 - c) * percent / 100)) for c in rgb)
            return f"#{lightened[0]:02x}{lightened[1]:02x}{lightened[2]:02x}"
        return color
    
    def darken_color(self, color, percent=20):
        """Darken a hex color by a given percentage"""
        if isinstance(color, str) and color.startswith('#'):
            color = color.lstrip('#')
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            darkened = tuple(max(0, int(c * (100 - percent) / 100)) for c in rgb)
            return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"
        return color

    # [Rest of the code remains exactly the same...]
    # All the existing methods (show_dashboard, create_input_section, etc.)
    # remain unchanged to preserve functionality
    
    def create_input_section(self, parent):
        # Input section with modern styling using CSS colors
        input_container = tk.Frame(parent, bg=self.css_colors['dark'], relief='flat', bd=2)
        input_container.pack(fill='x', pady=10)
        
        # Array A input
        tk.Label(input_container, text="Array A:", 
                **self.css_text['h3'],
                bg=self.css_colors['dark']).pack(anchor='w', padx=15, pady=(15, 5))
        
        self.array_a_entry = tk.Text(input_container, height=3, 
                                    **self.css_text['code'],
                                    bg=self.css_colors['dark'],
                                    insertbackground='white',
                                    relief='flat', bd=0)
        self.array_a_entry.pack(fill='x', padx=15, pady=(0, 10))
        self.array_a_entry.insert('1.0', '[1, 2, 3]')
        
        # Array B input
        tk.Label(input_container, text="Array B:", 
                **self.css_text['h3'],
                bg=self.css_colors['dark']).pack(anchor='w', padx=15, pady=(5, 5))
        
        self.array_b_entry = tk.Text(input_container, height=3, 
                                    **self.css_text['code'],
                                    bg=self.css_colors['dark'],
                                    insertbackground='white',
                                    relief='flat', bd=0)
        self.array_b_entry.pack(fill='x', padx=15, pady=(0, 15))
        self.array_b_entry.insert('1.0', '[4, 5, 6]')
    
    def create_result_display(self, parent):
        # Result display with modern styling using CSS colors
        result_container = tk.Frame(parent, bg=self.css_colors['dark'], relief='flat', bd=2)
        result_container.pack(fill='both', expand=True, pady=10)
        
        tk.Label(result_container, text="📋 Results:", 
                **self.css_text['h2'],
                bg=self.css_colors['dark']).pack(anchor='w', padx=15, pady=(15, 10))
        
        self.result_display = scrolledtext.ScrolledText(
            result_container,
            **self.css_text['code'],
            bg=self.css_colors['dark'],
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

    # [All other existing methods remain exactly the same...]

def main():
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
