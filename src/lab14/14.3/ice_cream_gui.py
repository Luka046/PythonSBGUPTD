import tkinter as tk
from tkinter import messagebox

class IceCreamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Кафе-мороженое")

        self.flavors = ["ванильное", "шоколадное", "клубничное"]

        self.label = tk.Label(root, text="Выберите сорт мороженого:")
        self.label.pack()

        self.flavor_var = tk.StringVar(value=self.flavors[0])
        self.flavor_menu = tk.OptionMenu(root, self.flavor_var, *self.flavors)
        self.flavor_menu.pack()

        self.order_button = tk.Button(root, text="Заказать", command=self.place_order)
        self.order_button.pack()

    def place_order(self):
        selected_flavor = self.flavor_var.get()
        messagebox.showinfo("Заказ", f"Вы заказали {selected_flavor} мороженое!")

root = tk.Tk()
app = IceCreamApp(root)
root.mainloop()