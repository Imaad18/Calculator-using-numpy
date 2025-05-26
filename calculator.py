import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.inject_css()
        self.setup_styles()
        self.create_widgets()
        self.current_operation = None
        self.calculation_history = []
        
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
        """Setup ttk styles with modern CSS colors"""
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
    
    def lighten_color(self, color, percent=20):
        """Lighten a hex color by a given percentage"""
        if isinstance(color, str) and color.startswith('#'):
            color = color.lstrip('#')
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            lightened = tuple(min(255, int(c + (255 - c) * percent / 100)) for c in rgb)
            return f"#{lightened[0]:02x}{lightened[1]:02x}{lightened[2]:02x}"
        return color
    
    def create_gradient_background(self):
        """Create an animated gradient background with CSS-like effects"""
        # Create background canvas
        self.bg_canvas = tk.Canvas(self.root, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Gradient colors for animation
        self.gradient_colors = [
            ['#0f0f23', '#1a1a2e', '#16213e', '#0f3460'],
            ['#1a1a2e', '#16213e', '#0f3460', '#533483'],
            ['#16213e', '#0f3460', '#533483', '#6c5ce7'],
            ['#0f3460', '#533483', '#6c5ce7', '#a29bfe'],
            ['#533483', '#6c5ce7', '#a29bfe', '#74b9ff']
        ]
        self.current_gradient = 0
        
        # Create initial gradient
        self.draw_gradient_background()
        
        # Start animation
        self.animate_background()
    
    def draw_gradient_background(self):
        """Draw animated gradient background"""
        self.bg_canvas.delete("gradient")
        
        width = self.root.winfo_width() if self.root.winfo_width() > 1 else 1000
        height = self.root.winfo_height() if self.root.winfo_height() > 1 else 700
        
        colors = self.gradient_colors[self.current_gradient % len(self.gradient_colors)]
        
        # Create diagonal gradient effect
        steps = 100
        for i in range(steps):
            # Calculate color interpolation
            ratio = i / steps
            
            # Interpolate between multiple colors
            if ratio < 0.33:
                # First third: color[0] to color[1]
                local_ratio = ratio * 3
                color = self.interpolate_color(colors[0], colors[1], local_ratio)
            elif ratio < 0.66:
                # Second third: color[1] to color[2]
                local_ratio = (ratio - 0.33) * 3
                color = self.interpolate_color(colors[1], colors[2], local_ratio)
            else:
                # Final third: color[2] to color[3]
                local_ratio = (ratio - 0.66) * 3
                color = self.interpolate_color(colors[2], colors[3], local_ratio)
            
            # Create diagonal stripes
            x1 = int(i * width / steps)
            y1 = 0
            x2 = x1 + int(width / steps) + 2
            y2 = height
            
            self.bg_canvas.create_rectangle(x1, y1, x2, y2, 
                                          fill=color, outline=color, tags="gradient")
        
        # Add floating orbs/circles for extra effect
        self.add_floating_elements()
    
    def add_floating_elements(self):
        """Add floating CSS-like elements for visual appeal"""
        width = self.root.winfo_width() if self.root.winfo_width() > 1 else 1000
        height = self.root.winfo_height() if self.root.winfo_height() > 1 else 700
        
        # Add some floating circles with CSS-like blur effect simulation
        orb_colors = [self.css_colors['primary'], self.css_colors['accent'], 
                     self.css_colors['success'], self.css_colors['warning']]
        
        for i in range(8):
            x = (i * width // 8) + (i * 50)
            y = (height // 4) + (i % 3) * (height // 3)
            radius = 30 + (i % 3) * 20
            color = orb_colors[i % len(orb_colors)]
            
            # Create multiple circles with decreasing opacity effect
            for j in range(5):
                current_radius = radius - j * 5
                alpha_color = self.add_alpha_to_color(color, 0.1 - j * 0.02)
                if current_radius > 0:
                    self.bg_canvas.create_oval(x - current_radius, y - current_radius,
                                             x + current_radius, y + current_radius,
                                             fill=alpha_color, outline="", tags="gradient")
    
    def interpolate_color(self, color1, color2, ratio):
        """Interpolate between two hex colors"""
        # Convert hex to RGB
        c1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
        c2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))
        
        # Interpolate
        r = int(c1[0] + (c2[0] - c1[0]) * ratio)
        g = int(c1[1] + (c2[1] - c1[1]) * ratio)
        b = int(c1[2] + (c2[2] - c1[2]) * ratio)
        
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def add_alpha_to_color(self, color, alpha):
        """Simulate alpha by blending with background"""
        bg_color = self.css_colors['background']
        
        # Convert hex to RGB
        c = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
        bg = tuple(int(bg_color[i:i+2], 16) for i in (1, 3, 5))
        
        # Blend colors
        r = int(bg[0] + (c[0] - bg[0]) * alpha)
        g = int(bg[1] + (c[1] - bg[1]) * alpha)
        b = int(bg[2] + (c[2] - bg[2]) * alpha)
        
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def animate_background(self):
        """Animate the gradient background"""
        self.current_gradient = (self.current_gradient + 1) % len(self.gradient_colors)
        self.draw_gradient_background()
        
    def animate_header(self):
        """Animate the header with moving gradient"""
        if hasattr(self, 'header_canvas'):
            self.header_canvas.delete("header_bg")
            
            width = 230  # approximate header width
            height = 76  # approximate header height
            
            # Create moving gradient effect
            colors = ['#6c5ce7', '#a29bfe', '#74b9ff', '#fd79a8']
            offset = (self.current_gradient * 20) % 100
            
            for i in range(4):
                x1 = (i * width // 4) + offset - 50
                x2 = x1 + width // 2
                color = colors[i % len(colors)]
                
                self.header_canvas.create_rectangle(x1, 0, x2, height,
                                                  fill=color, outline="", tags="header_bg")
        
        # Schedule next header animation
        self.root.after(1000, self.animate_header)

    def darken_color(self, color, percent=20):
        """Darken a hex color by a given percentage"""
        if isinstance(color, str) and color.startswith('#'):
            color = color.lstrip('#')
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            darkened = tuple(max(0, int(c * (100 - percent) / 100)) for c in rgb)
            return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"
        return color

    def create_widgets(self):
        # Create animated gradient background canvas
        self.create_gradient_background()
        
        # Create main container with sidebar (transparent-like effect)
        container = tk.Frame(self.root, bg=self.css_colors['background'])
        container.pack(fill='both', expand=True)
        
        # Create sidebar (with semi-transparent effect)
        self.create_sidebar(container)
        
        # Main content frame (with glass-like effect)
        main_frame = tk.Frame(container, bg='', highlightthickness=2, 
                             highlightbackground=self.css_colors['primary'],
                             highlightcolor=self.css_colors['accent'])
        main_frame.pack(side='right', fill='both', expand=True, padx=(0, 20), pady=20)
        
        # Make main frame semi-transparent
        main_frame.configure(bg=self.add_alpha_to_color(self.css_colors['card'], 0.8))
        
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
        # Sidebar with glass-morphism effect
        sidebar = tk.Frame(parent, bg=self.add_alpha_to_color(self.css_colors['dark'], 0.7), 
                          width=250, highlightthickness=2,
                          highlightbackground=self.css_colors['primary'],
                          highlightcolor=self.css_colors['accent'])
        sidebar.pack(side='left', fill='y', padx=(20, 20), pady=20)
        sidebar.pack_propagate(False)
        
        # Sidebar header with animated gradient effect
        header_frame = tk.Frame(sidebar, height=80, highlightthickness=2,
                               highlightbackground=self.css_colors['accent'])
        header_frame.pack(fill='x', padx=10, pady=(10, 20))
        header_frame.pack_propagate(False)
        
        # Create animated header background
        self.header_canvas = tk.Canvas(header_frame, highlightthickness=0)
        self.header_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.animate_header()
        
        # Header label centered with glow effect
        header_label = tk.Label(header_frame, text="⚡ CALCULATOR", 
                               font=('Segoe UI', 14, 'bold'), 
                               fg='white', bg='')
        header_label.place(relx=0.5, rely=0.5, anchor='center')
        
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
                           activebackground=self.lighten_color(color, 20),
                           activeforeground=self.css_colors['text'],
                           highlightthickness=1, highlightcolor=self.css_colors['accent'])
            btn.pack(fill='x', ipady=8)
        
        # Quick actions section
        quick_label = tk.Label(sidebar, text="⚡ QUICK ACTIONS", 
                              **self.css_text['h3'],
                              bg=self.css_colors['dark'])
        quick_label.pack(pady=(30, 10), padx=20, anchor='w')
        
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
                           activebackground=self.lighten_color(color, 20),
                           activeforeground=self.css_colors['text'],
                           highlightthickness=1, highlightcolor=self.css_colors['accent'])
            btn.pack(fill='x', ipady=6)
        
        # Status section at bottom
        status_frame = tk.Frame(sidebar, bg=self.css_colors['dark'], height=60)
        status_frame.pack(side='bottom', fill='x', padx=10, pady=10)
        status_frame.pack_propagate(False)
        
        status_ready = tk.Label(status_frame, text="🟢 Ready", 
                               font=('Segoe UI', 10, 'bold'), 
                               fg=self.css_colors['success'], 
                               bg=self.css_colors['dark'])
        status_ready.pack(pady=5)
        
        version_label = tk.Label(status_frame, text="NumPy Calculator v2.0", 
                                font=('Segoe UI', 8), 
                                fg=self.css_colors['light'], 
                                bg=self.css_colors['dark'])
        version_label.pack()
    
    def create_input_section(self, parent):
        # Input section with modern styling using CSS colors
        input_container = tk.Frame(parent, bg=self.css_colors['dark'], relief='flat', bd=2)
        input_container.pack(fill='x', pady=10)
        
        # Array A input
        array_a_label = tk.Label(input_container, text="Array A:", 
                                **self.css_text['h3'],
                                bg=self.css_colors['dark'])
        array_a_label.pack(anchor='w', padx=15, pady=(15, 5))
        
        self.array_a_entry = tk.Text(input_container, height=3, 
                                    **self.css_text['code'],
                                    bg=self.lighten_color(self.css_colors['dark'], 10),
                                    insertbackground='white',
                                    relief='flat', bd=0,
                                    highlightthickness=1,
                                    highlightcolor=self.css_colors['primary'])
        self.array_a_entry.pack(fill='x', padx=15, pady=(0, 10))
        self.array_a_entry.insert('1.0', '[1, 2, 3]')
        
        # Array B input
        array_b_label = tk.Label(input_container, text="Array B:", 
                                **self.css_text['h3'],
                                bg=self.css_colors['dark'])
        array_b_label.pack(anchor='w', padx=15, pady=(5, 5))
        
        self.array_b_entry = tk.Text(input_container, height=3, 
                                    **self.css_text['code'],
                                    bg=self.lighten_color(self.css_colors['dark'], 10),
                                    insertbackground='white',
                                    relief='flat', bd=0,
                                    highlightthickness=1,
                                    highlightcolor=self.css_colors['primary'])
        self.array_b_entry.pack(fill='x', padx=15, pady=(0, 15))
        self.array_b_entry.insert('1.0', '[4, 5, 6]')
    
    def create_operation_buttons(self, parent):
        # Operations section with modern styling
        ops_container = tk.Frame(parent, bg=self.css_colors['dark'], relief='flat', bd=2)
        ops_container.pack(fill='x', pady=10)
        
        ops_label = tk.Label(ops_container, text="🔧 Operations:", 
                            **self.css_text['h2'],
                            bg=self.css_colors['dark'])
        ops_label.pack(anchor='w', padx=15, pady=(15, 10))
        
        # Create button grid
        button_frame = tk.Frame(ops_container, bg=self.css_colors['dark'])
        button_frame.pack(fill='x', padx=15, pady=(0, 15))
        
        # Basic operations
        basic_ops = [
            ("➕ Add", self.add_arrays, self.css_colors['success']),
            ("➖ Subtract", self.subtract_arrays, self.css_colors['warning']),
            ("✖️ Multiply", self.multiply_arrays, self.css_colors['accent']),
            ("➗ Divide", self.divide_arrays, self.css_colors['info'])
        ]
        
        # Advanced operations
        advanced_ops = [
            ("📊 Dot Product", self.dot_product, self.css_colors['primary']),
            ("🔄 Transpose A", self.transpose_a, self.css_colors['secondary']),
            ("📐 Shape Info", self.show_shapes, self.css_colors['dark']),
            ("📈 Statistics", self.show_statistics, self.css_colors['success'])
        ]
        
        # Create basic operations row
        basic_frame = tk.Frame(button_frame, bg=self.css_colors['dark'])
        basic_frame.pack(fill='x', pady=(0, 10))
        
        for i, (text, command, color) in enumerate(basic_ops):
            btn = tk.Button(basic_frame, text=text, command=command,
                           bg=color, fg=self.css_colors['text'], relief='flat', bd=0,
                           font=('Segoe UI', 10, 'bold'), cursor='hand2',
                           activebackground=self.lighten_color(color, 20),
                           activeforeground=self.css_colors['text'])
            btn.pack(side='left', fill='x', expand=True, padx=2, ipady=10)
        
        # Create advanced operations row
        advanced_frame = tk.Frame(button_frame, bg=self.css_colors['dark'])
        advanced_frame.pack(fill='x')
        
        for i, (text, command, color) in enumerate(advanced_ops):
            btn = tk.Button(advanced_frame, text=text, command=command,
                           bg=color, fg=self.css_colors['text'], relief='flat', bd=0,
                           font=('Segoe UI', 10, 'bold'), cursor='hand2',
                           activebackground=self.lighten_color(color, 20),
                           activeforeground=self.css_colors['text'])
            btn.pack(side='left', fill='x', expand=True, padx=2, ipady=10)
    
    def create_result_display(self, parent):
        # Result display with modern styling using CSS colors
        result_container = tk.Frame(parent, bg=self.css_colors['dark'], relief='flat', bd=2)
        result_container.pack(fill='both', expand=True, pady=10)
        
        result_label = tk.Label(result_container, text="📋 Results:", 
                               **self.css_text['h2'],
                               bg=self.css_colors['dark'])
        result_label.pack(anchor='w', padx=15, pady=(15, 10))
        
        self.result_display = scrolledtext.ScrolledText(
            result_container,
            **self.css_text['code'],
            bg=self.lighten_color(self.css_colors['dark'], 5),
            insertbackground='white',
            relief='flat',
            bd=0,
            height=15,
            highlightthickness=1,
            highlightcolor=self.css_colors['primary']
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
    
    # Sidebar Navigation Methods
    def show_dashboard(self):
        self.log_result("📊 Dashboard: Main calculator view active")
    
    def show_operations(self):
        self.log_result("🔧 Operations: All mathematical operations available")
    
    def show_settings(self):
        self.log_result("⚙️ Settings: Configuration options (placeholder)")
    
    def show_history(self):
        if self.calculation_history:
            history_text = "📈 Calculation History:\n" + "\n".join(self.calculation_history[-10:])
            self.log_result(history_text)
        else:
            self.log_result("📈 History: No calculations performed yet")
    
    # Quick Action Methods
    def load_examples(self):
        self.array_a_entry.delete('1.0', 'end')
        self.array_b_entry.delete('1.0', 'end')
        self.array_a_entry.insert('1.0', '[[1, 2, 3], [4, 5, 6]]')
        self.array_b_entry.insert('1.0', '[[7, 8, 9], [10, 11, 12]]')
        self.log_result("🎯 Example arrays loaded!")
    
    def clear_all(self):
        self.array_a_entry.delete('1.0', 'end')
        self.array_b_entry.delete('1.0', 'end')
        self.result_display.delete('1.0', 'end')
        self.log_result("🧹 All fields cleared!")
    
    def save_result(self):
        try:
            result_text = self.result_display.get('1.0', 'end-1c')
            with open('calculator_results.txt', 'w') as f:
                f.write(result_text)
            self.log_result("💾 Results saved to 'calculator_results.txt'")
        except Exception as e:
            self.log_result(f"❌ Error saving: {str(e)}")
    
    def copy_result(self):
        try:
            self.root.clipboard_clear()
            result_text = self.result_display.get('1.0', 'end-1c')
            self.root.clipboard_append(result_text)
            self.log_result("📋 Results copied to clipboard!")
        except Exception as e:
            self.log_result(f"❌ Error copying: {str(e)}")
    
    # Array Operation Methods
    def get_arrays(self):
        """Parse and return numpy arrays from input fields"""
        try:
            a_text = self.array_a_entry.get('1.0', 'end-1c').strip()
            b_text = self.array_b_entry.get('1.0', 'end-1c').strip()
            
            array_a = np.array(eval(a_text))
            array_b = np.array(eval(b_text))
            
            return array_a, array_b
        except Exception as e:
            self.log_result(f"❌ Error parsing arrays: {str(e)}")
            return None, None
    
    def log_result(self, message):
        """Add a message to the result display"""
        self.result_display.insert('end', f"\n{message}\n")
        self.result_display.see('end')
        
        # Add to history
        if not message.startswith(('📊', '🔧', '⚙️', '📈', '🎯', '🧹', '💾', '📋')):
            self.calculation_history.append(message)
    
    def add_arrays(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = a + b
                self.log_result(f"➕ Addition Result:\n{result}")
            except Exception as e:
                self.log_result(f"❌ Addition Error: {str(e)}")
    
    def subtract_arrays(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = a - b
                self.log_result(f"➖ Subtraction Result:\n{result}")
            except Exception as e:
                self.log_result(f"❌ Subtraction Error: {str(e)}")
    
    def multiply_arrays(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = a * b
                self.log_result(f"✖️ Multiplication Result:\n{result}")
            except Exception as e:
                self.log_result(f"❌ Multiplication Error: {str(e)}")
    
    def divide_arrays(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = a / b
                self.log_result(f"➗ Division Result:\n{result}")
            except Exception as e:
                self.log_result(f"❌ Division Error: {str(e)}")
    
    def dot_product(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                result = np.dot(a, b)
                self.log_result(f"📊 Dot Product Result:\n{result}")
            except Exception as e:
                self.log_result(f"❌ Dot Product Error: {str(e)}")
    
    def transpose_a(self):
        try:
            a_text = self.array_a_entry.get('1.0', 'end-1c').strip()
            array_a = np.array(eval(a_text))
            result = array_a.T
            self.log_result(f"🔄 Transpose of Array A:\n{result}")
        except Exception as e:
            self.log_result(f"❌ Transpose Error: {str(e)}")
    
    def show_shapes(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            self.log_result(f"📐 Shape Information:\nArray A: {a.shape}\nArray B: {b.shape}")
    
    def show_statistics(self):
        a, b = self.get_arrays()
        if a is not None and b is not None:
            try:
                self.log_result(f"""📈 Statistical Analysis:
Array A:
  Mean: {np.mean(a):.4f}
  Std:  {np.std(a):.4f}
  Min:  {np.min(a)}
  Max:  {np.max(a)}

Array B:
  Mean: {np.mean(b):.4f}
  Std:  {np.std(b):.4f}
  Min:  {np.min(b)}
  Max:  {np.max(b)}""")
            except Exception as e:
                self.log_result(f"❌ Statistics Error: {str(e)}")

def main():
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
