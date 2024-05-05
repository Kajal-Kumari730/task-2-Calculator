import tkinter as tk

def press_key(key):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(key))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except SyntaxError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Syntax Error")
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Math Error")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for display
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    button_bg = "lightgrey" if button.isdigit() or button == '.' else "lightblue"
    tk.Button(root, text=button, width=5, height=2, background=button_bg, foreground="black", font=('Arial', 12),
              command=lambda key=button: press_key(key) if key != '=' else calculate()).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Button to clear the entry
tk.Button(root, text="C", width=5, height=2, foreground="black", background="red", command=clear_entry).grid(row=row_val, column=col_val, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
