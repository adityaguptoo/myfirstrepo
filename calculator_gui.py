import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x700")
        self.root.resizable(False, False)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variables
        self.display_var = tk.StringVar(value="0")
        self.current_mode = tk.StringVar(value="Simple")
        self.expression = ""
        
        # Color scheme
        self.bg_color = "#2b2b2b"
        self.display_bg = "#1e1e1e"
        self.button_bg = "#3c3c3c"
        self.button_hover = "#4c4c4c"
        self.operator_bg = "#ff9500"
        self.operator_hover = "#ffad33"
        self.number_bg = "#505050"
        self.number_hover = "#606060"
        self.text_color = "#ffffff"
        
        self.root.configure(bg=self.bg_color)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Mode selector frame
        mode_frame = tk.Frame(self.root, bg=self.bg_color, pady=10)
        mode_frame.pack(fill=tk.X)
        
        tk.Label(mode_frame, text="Calculator Mode:", 
                bg=self.bg_color, fg=self.text_color, 
                font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=10)
        
        simple_btn = tk.Radiobutton(mode_frame, text="Simple", 
                                    variable=self.current_mode, 
                                    value="Simple",
                                    bg=self.bg_color, fg=self.text_color,
                                    selectcolor=self.button_bg,
                                    font=("Arial", 11),
                                    command=self.switch_mode)
        simple_btn.pack(side=tk.LEFT, padx=5)
        
        scientific_btn = tk.Radiobutton(mode_frame, text="Scientific", 
                                       variable=self.current_mode, 
                                       value="Scientific",
                                       bg=self.bg_color, fg=self.text_color,
                                       selectcolor=self.button_bg,
                                       font=("Arial", 11),
                                       command=self.switch_mode)
        scientific_btn.pack(side=tk.LEFT, padx=5)
        
        # Display frame
        display_frame = tk.Frame(self.root, bg=self.display_bg, padx=20, pady=20)
        display_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.display = tk.Label(display_frame, 
                               textvariable=self.display_var,
                               bg=self.display_bg,
                               fg=self.text_color,
                               font=("Arial", 24, "bold"),
                               anchor="e",
                               justify="right")
        self.display.pack(fill=tk.BOTH, expand=True)
        
        # Buttons frame
        self.buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.create_buttons()
        
    def switch_mode(self):
        """Switch between Simple and Scientific calculator"""
        self.clear_all()
        self.create_buttons()
        
    def create_buttons(self):
        """Create buttons based on current mode"""
        # Clear existing buttons
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        
        if self.current_mode.get() == "Scientific":
            self.create_scientific_buttons()
        else:
            self.create_simple_buttons()
            
    def create_simple_buttons(self):
        """Create buttons for simple calculator"""
        buttons = [
            ["C", "⌫", "/", "*"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "", ""]
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text:  # Only create button if text exists
                    btn = self.create_button(text, i, j, len(buttons[0]))
                    if text in ["C", "⌫"]:
                        btn.configure(bg="#ff4444", activebackground="#ff6666")
                    elif text in ["/", "*", "-", "+", "="]:
                        btn.configure(bg=self.operator_bg, activebackground=self.operator_hover)
                    else:
                        btn.configure(bg=self.number_bg, activebackground=self.number_hover)
        
        # Make "=" button span 2 rows
        equals_btn = self.create_button("=", 3, 3, 4)
        equals_btn.configure(bg=self.operator_bg, activebackground=self.operator_hover)
        equals_btn.grid(row=3, column=3, rowspan=2, sticky="nsew", padx=2, pady=2)
        
        # Make "0" button span 2 columns
        zero_btn = self.create_button("0", 4, 0, 4)
        zero_btn.configure(bg=self.number_bg, activebackground=self.number_hover)
        zero_btn.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        
        # Configure grid weights
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.buttons_frame.grid_columnconfigure(j, weight=1)
            
    def create_scientific_buttons(self):
        """Create buttons for scientific calculator"""
        # Scientific function buttons
        sci_buttons_row1 = ["sin", "cos", "tan", "√"]
        sci_buttons_row2 = ["log", "ln", "π", "e"]
        sci_buttons_row3 = ["x²", "x³", "^", "1/x"]
        sci_buttons_row4 = ["(", ")", "C", "⌫"]
        
        # Number and operator buttons
        num_buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]
        
        all_rows = [sci_buttons_row1, sci_buttons_row2, sci_buttons_row3, sci_buttons_row4] + num_buttons
        
        for i, row in enumerate(all_rows):
            for j, text in enumerate(row):
                if text:  # Only create button if text exists
                    btn = self.create_button(text, i, j, len(row))
                    if text in ["C", "⌫"]:
                        btn.configure(bg="#ff4444", activebackground="#ff6666")
                    elif text in ["/", "*", "-", "+", "=", "^"]:
                        btn.configure(bg=self.operator_bg, activebackground=self.operator_hover)
                    elif text in sci_buttons_row1 + sci_buttons_row2 + sci_buttons_row3 + ["(", ")"]:
                        btn.configure(bg="#6c5ce7", activebackground="#7d6ee8")
                    else:
                        btn.configure(bg=self.number_bg, activebackground=self.number_hover)
        
        # Make "0" button span 2 columns
        zero_btn = self.create_button("0", 7, 0, 4)
        zero_btn.configure(bg=self.number_bg, activebackground=self.number_hover)
        zero_btn.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        
        # Configure grid weights
        for i in range(8):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.buttons_frame.grid_columnconfigure(j, weight=1)
            
    def create_button(self, text, row, col, total_cols):
        """Create a styled button"""
        btn = tk.Button(self.buttons_frame,
                       text=text,
                       font=("Arial", 16, "bold"),
                       bg=self.button_bg,
                       fg=self.text_color,
                       activebackground=self.button_hover,
                       activeforeground=self.text_color,
                       relief=tk.FLAT,
                       borderwidth=0,
                       cursor="hand2",
                       command=lambda t=text: self.button_click(t))
        
        btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        return btn
        
    def button_click(self, value):
        """Handle button clicks"""
        if value == "C":
            self.clear_all()
        elif value == "⌫":
            self.backspace()
        elif value == "=":
            self.calculate()
        elif value == "π":
            self.expression += str(math.pi)
            self.update_display()
        elif value == "e":
            self.expression += str(math.e)
            self.update_display()
        elif value == "sin":
            self.apply_function("sin")
        elif value == "cos":
            self.apply_function("cos")
        elif value == "tan":
            self.apply_function("tan")
        elif value == "√":
            self.apply_function("sqrt")
        elif value == "log":
            self.apply_function("log10")
        elif value == "ln":
            self.apply_function("log")
        elif value == "x²":
            self.apply_power(2)
        elif value == "x³":
            self.apply_power(3)
        elif value == "^":
            self.expression += "**"
            self.update_display()
        elif value == "1/x":
            self.apply_reciprocal()
        else:
            self.expression += str(value)
            self.update_display()
            
    def apply_function(self, func_name):
        """Apply a mathematical function"""
        try:
            if self.expression:
                value = float(eval(self.expression, {"__builtins__": None}, {"math": math}))
            else:
                value = float(self.display_var.get())
            
            if func_name == "sin":
                result = math.sin(math.radians(value))
            elif func_name == "cos":
                result = math.cos(math.radians(value))
            elif func_name == "tan":
                result = math.tan(math.radians(value))
            elif func_name == "sqrt":
                result = math.sqrt(value)
            elif func_name == "log10":
                result = math.log10(value)
            elif func_name == "log":
                result = math.log(value)
            
            self.expression = str(result)
            self.update_display()
        except:
            self.display_var.set("Error")
            self.expression = ""
            
    def apply_power(self, power):
        """Apply power function"""
        try:
            if self.expression:
                value = float(eval(self.expression, {"__builtins__": None}, {"math": math}))
            else:
                value = float(self.display_var.get())
            
            result = value ** power
            self.expression = str(result)
            self.update_display()
        except:
            self.display_var.set("Error")
            self.expression = ""
            
    def apply_reciprocal(self):
        """Apply reciprocal function"""
        try:
            if self.expression:
                value = float(eval(self.expression, {"__builtins__": None}, {"math": math}))
            else:
                value = float(self.display_var.get())
            
            result = 1 / value
            self.expression = str(result)
            self.update_display()
        except:
            self.display_var.set("Error")
            self.expression = ""
            
    def calculate(self):
        """Calculate the expression"""
        try:
            if self.expression:
                result = eval(self.expression, {"__builtins__": None}, {"math": math})
                self.display_var.set(str(result))
                self.expression = str(result)
            else:
                self.display_var.set("0")
        except:
            self.display_var.set("Error")
            self.expression = ""
            
    def clear_all(self):
        """Clear the display and expression"""
        self.expression = ""
        self.display_var.set("0")
        
    def backspace(self):
        """Remove last character"""
        if self.expression:
            self.expression = self.expression[:-1]
            self.update_display()
        else:
            self.display_var.set("0")
            
    def update_display(self):
        """Update the display"""
        if self.expression:
            self.display_var.set(self.expression)
        else:
            self.display_var.set("0")

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
