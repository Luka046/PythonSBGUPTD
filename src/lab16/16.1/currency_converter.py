import tkinter as tk
from tkinter import messagebox
import requests

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер валют")

        self.amount_label = tk.Label(root, text="Сумма:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.from_currency_label = tk.Label(root, text="Из валюты:")
        self.from_currency_label.pack()

        self.from_currency_entry = tk.Entry(root)
        self.from_currency_entry.pack()

        self.to_currency_label = tk.Label(root, text="В валюту:")
        self.to_currency_label.pack()

        self.to_currency_entry = tk.Entry(root)
        self.to_currency_entry.pack()

        self.convert_button = tk.Button(root, text="Конвертировать", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        amount = self.amount_entry.get()
        from_currency = self.from_currency_entry.get().upper()
        to_currency = self.to_currency_entry.get().upper()

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Ошибка", "Неверная валюта")
        else:
            rate = data['rates'][to_currency]
            converted_amount = float(amount) * rate
            messagebox.showinfo("Результат", f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

root = tk.Tk()
app = CurrencyConverterApp(root)
root.mainloop()