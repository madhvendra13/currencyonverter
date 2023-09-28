import tkinter as tk
from tkinter import ttk
import requests

# Function to convert currency
def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()
    
    # Fetch real-time exchange rates from Open Exchange Rates API
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    url = f'https://open.er-api.com/v6/latest/{from_currency}/{to_currency}'
    response = requests.get(url)
    data = response.json()
    
    # Calculate the converted amount
    converted_amount = amount * data['rate']
    
    # Update the result label
    result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create and configure widgets
label_from_currency = tk.Label(root, text="From Currency:")
label_to_currency = tk.Label(root, text="To Currency:")
label_amount = tk.Label(root, text="Amount:")
result_label = tk.Label(root, text="Result:")

combo_from_currency = ttk.Combobox(root)
combo_to_currency = ttk.Combobox(root)
entry_amount = ttk.Entry(root)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)

# Place widgets on the grid
label_from_currency.grid(row=0, column=0)
label_to_currency.grid(row=1, column=0)
label_amount.grid(row=2, column=0)
result_label.grid(row=4, column=0, columnspan=2)

combo_from_currency.grid(row=0, column=1)
combo_to_currency.grid(row=1, column=1)
entry_amount.grid(row=2, column=1)
convert_button.grid(row=3, column=0, columnspan=2)

# Set default values for currency combo boxes
combo_from_currency.set("USD")
combo_to_currency.set("EUR")

# Run the Tkinter main loop
root.mainloop()
