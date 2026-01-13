import tkinter as tk
from tkinter import font

class Calculator:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        self.center_window()
        
        self.expression = ""
        self.result_displayed = False
        
        self.create_display()
        self.create_buttons()
        
        self.root.bind('<Key>', self.key_press)
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#1e1e1e")
        display_frame.pack(pady=20, padx=20, fill=tk.BOTH)
        
        self.display = tk.Label(
            display_frame,
            text="0",
            font=("Segoe UI", 32, "bold"),
            bg="#2d2d2d",
            fg="#ffffff",
            anchor="e",
            padx=20,
            pady=20,
            relief=tk.FLAT
        )
        self.display.pack(fill=tk.BOTH, expand=True)
    
    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        buttons = [
            ['C', '⌫', '(', ')'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        btn_font = ("Segoe UI", 18, "bold")
        
        for i, row in enumerate(buttons):
            button_frame.grid_rowconfigure(i, weight=1)
            
            for j, btn_text in enumerate(row):
                button_frame.grid_columnconfigure(j, weight=1)
                
                if btn_text in ['C', '⌫']:
                    bg_color = "#d32f2f"
                    hover_color = "#f44336"
                elif btn_text == '=':
                    bg_color = "#0288d1"
                    hover_color = "#03a9f4"
                elif btn_text in ['+', '-', '*', '/', '(', ')']:
                    bg_color = "#455a64"
                    hover_color = "#607d8b"
                else:
                    bg_color = "#424242"
                    hover_color = "#616161"
                
                btn = tk.Button(
                    button_frame,
                    text=btn_text,
                    font=btn_font,
                    bg=bg_color,
                    fg="#ffffff",
                    activebackground=hover_color,
                    activeforeground="#ffffff",
                    relief=tk.FLAT,
                    borderwidth=0,
                    cursor="hand2"
                )
                
                btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
                
                if btn_text == 'C':
                    btn.config(command=self.clear)
                elif btn_text == '⌫':
                    btn.config(command=self.backspace)
                elif btn_text == '=':
                    btn.config(command=self.calculate)
                else:
                    btn.config(command=lambda x=btn_text: self.press(x))
                
                btn.bind('<Enter>', lambda e, b=btn, c=hover_color: b.config(bg=c))
                btn.bind('<Leave>', lambda e, b=btn, c=bg_color: b.config(bg=c))
    
    def press(self, key):
        if self.result_displayed:
            if key in ['+', '-', '*', '/']:
                self.result_displayed = False
            else:
                self.expression = ""
                self.result_displayed = False
        
        self.expression += str(key)
        self.update_display()
    
    def clear(self):
        self.expression = ""
        self.result_displayed = False
        self.update_display()
    
    def backspace(self):
        if self.expression:
            self.expression = self.expression[:-1]
            self.update_display()
    
    def calculate(self):
        if not self.expression:
            return
        
        try:
            calc_expression = self.expression.replace('×', '*').replace('÷', '/')
            
            result = eval(calc_expression)
            
            if isinstance(result, float):
                result = round(result, 10)
                if result == int(result):
                    result = int(result)
            
            self.expression = str(result)
            self.result_displayed = True
            self.update_display()
            
        except ZeroDivisionError:
            self.display.config(text="Error: Div by 0")
            self.expression = ""
        except Exception:
            self.display.config(text="Error: Invalid")
            self.expression = ""
    
    def update_display(self):
        display_text = self.expression if self.expression else "0"
        
        if len(display_text) > 20:
            display_text = display_text[-20:]
        
        self.display.config(text=display_text)
    
    def key_press(self, event):
        key = event.char
        
        if key in '0123456789.+-*/()':
            self.press(key)
        elif event.keysym in ['Return', 'KP_Enter', 'equal']:
            self.calculate()
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Escape' or key.lower() == 'c':
            self.clear()


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()