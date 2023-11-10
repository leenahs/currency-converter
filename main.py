import requests
import tkinter as tk
from tkinter import ttk
import sv_ttk

# * ------------------------------------------------------------
# TODO: Make "convert" button disabled if amount text box is empty + didn't choose base and target currencies
# ! background color for buttons doesn't work at all.
# * ------------------------------------------------------------

class Test:
    def __init__(self):
        self.base = ""
        self.target = ""
        self.amount = ""

    def history_conversion(self, base, target, amount, results):
        history_label = ttk.Label(side_frame, text=f"{amount} {base} -> {results} {target}",
                                                font=("", 12))
        history_label.grid(padx=8, pady=8)
    
    # * Conversion function  
    def conversion(self, base, target, amount):
        # * checks if one of inputs is empty
        if not base or not target or not amount:
            print("empty!")
            label_results.config(text="Invalid or empty input")
        else:
            url=f"https://v6.exchangerate-api.com/v6/6f1c6d3b96344831bac336d9/pair/{base}/{target}/{amount}"
            results = requests.get(url).json()["conversion_result"]
            label_before.config(text=f"{amount} {base}")
            label_results.config(text=f"{results:.2f} {target}")
            # self.history_conversion(base, target, amount, results)

    # * Callback button function    
    def button_callback(self):     
        base = optionmenu1.get()
        target = optionmenu2.get()
        amount = entry.get()
        try:
            self.conversion(base, target, amount)
        except ValueError:
            print("empty")

    # * Switch button function  
    def switch_currencies(self):
        base = optionmenu2.get()
        target = optionmenu1.get()
        amount = entry.get()

        optionmenu1.set(base)
        optionmenu2.set(target)
        try:
            self.conversion(base, target, amount)
        except ValueError:
            print("empty")
# * ---------------------------------------------------------------------#
app = tk.Tk()
app.title("Currency Converter")
app.configure(bg='white')
# sv_ttk.set_theme("light")
# app.geometry("650x450")
# app.resizable(width=True, height=True)
# * ---------------------------------------------------------------------#

# class Widgets:


# * retrieve button functions from class Test()
call = Test()
real_button = call.button_callback
real_switch = call.switch_currencies

# * declare and itienilize style components
style = ttk.Style()
default_font = "Segoe UI Light"
style.configure('convert.TButton', font = (default_font, 12), bg='blue')
style.configure('font.TLabel', font = (default_font, 12))

# * Insert a temporary text in entry widget
def temp_text(e):
    entry.delete(0, "end")

# * List of currencies goes here:
currencies=["USD", "SAR", "JPY", "BHD", "CAD", "GBP"]

# * Base frame
frame=ttk.LabelFrame(app)
frame.grid(padx=30, pady=30)

# * Head / title frame
head_frame = ttk.Frame(frame)
head_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")
# * Main frame
main_frame=ttk.LabelFrame(frame, text="Convert")
main_frame.grid(row=1, column=0, padx=10, pady=10)
# * Results frame
side_frame = ttk.LabelFrame(frame)
side_frame.grid(row=2, column=0, padx=10, pady=10, sticky="we")

# * History panel
history_frame = ttk.LabelFrame(frame)
history_frame.grid(row=3, column=0, padx=10, pady=10, sticky="we")

# * TITLE
label_title = ttk.Label(head_frame, text="CURRENCY CONVERTER", font=(default_font, 24, "bold"))
label_title.grid(padx=10, pady=15, sticky="w")

# * Label "AMOUNT"
label_amount = ttk.Label(main_frame, text="AMOUNT", style="font.TLabel")
label_amount.grid(row=0, column=0, padx=5, sticky="")

# * Amount entry box
entry = ttk.Entry(main_frame, font=(default_font, 12))
entry.insert(0, "Enter amount")
entry.grid(row=1, column=0, padx=5, pady=10, sticky="")
entry.bind("<FocusIn>", temp_text)

# * Label "FROM"
label_from = ttk.Label(main_frame, text="FROM", style="font.TLabel")
label_from.grid(row=0, column=1, padx=5, sticky="")

# * option menu "FROM"
optionmenu1_var = tk.StringVar()
optionmenu1 = ttk.Combobox(main_frame, values=currencies, textvariable=optionmenu1_var, font=(default_font, 12))
optionmenu1.insert(0, "From...")
optionmenu1.grid(row=1, column=1, padx=14, pady=10, sticky="")

# * Label "TO"
label_from = ttk.Label(main_frame, text="TO", font=(default_font, 12))
label_from.grid(row=2, column=1, padx=5, sticky="")

# * option menu "TO"
optionmenu2_var = tk.StringVar()
optionmenu2 = ttk.Combobox(main_frame, values=currencies, textvariable=optionmenu2_var, font=(default_font, 12))
optionmenu2.insert(0, "To...")
optionmenu2.grid(row=3, column=1, padx=14, pady=10)

# * Convert button
button_convert = ttk.Button(main_frame, text="Convert", command=real_button, style="convert.TButton")
button_convert.grid(row=3, column=2, padx=14, pady=10)

# * Switch button
button_switch = ttk.Button(main_frame, text="Switch", command=real_switch, style='convert.TButton')
button_switch.grid(row=3, column=0, padx=7, pady=10, sticky="e")

# * Label "Before"
label_before = ttk.Label(side_frame, text=" ", style="font.TLabel")
label_before.grid(row=0, padx=3, sticky="w")

# * Label "Results"
label_results = ttk.Label(side_frame, text="", font=(default_font, 18))
label_results.grid(row=1, padx=3, pady=1, sticky="w")

# * set grid column figure
app.grid_columnconfigure(0, weight=1)

app.mainloop()