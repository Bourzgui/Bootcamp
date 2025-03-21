import tkinter as tk
from tkinter import messagebox
from menu_item import MenuItem
from menu_manager import MenuManager

class MenuEditor:
    def __init__(self, root):
        self.root = root # fenetre principale
        self.root.title("Restaurant Menu Manager")
        self.show_user_menu()

    def show_user_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy() # supprimer les widgets 
            
        tk.Label(self.root, text="Menu Manager").pack(pady=10)
        
        tk.Button(self.root, text="View an Item (V)", command=self.view_item).pack()
        tk.Button(self.root, text="Add an Item (A)", command=self.add_item_to_menu).pack()
        tk.Button(self.root, text="Delete an Item (D)", command=self.remove_item_from_menu).pack()
        tk.Button(self.root, text="Update an Item (U)", command=self.update_item_from_menu).pack()
        tk.Button(self.root, text="Show the Menu (S)", command=self.show_restaurant_menu).pack()
        tk.Button(self.root, text="Exit", command=self.exit_program).pack(pady=10)

    def view_item(self):
        self.input_window = tk.Toplevel(self.root)
        tk.Label(self.input_window, text="Enter item name:").pack()
        self.view_entry = tk.Entry(self.input_window)
        self.view_entry.pack()
        tk.Button(self.input_window, text="View", command=self.process_view).pack()

    def process_view(self):
        name = self.view_entry.get()
        item = MenuManager.get_by_name(name)
        self.input_window.destroy()
        if item:
            messagebox.showinfo("Item Info", f"Name: {item.name}\nPrice: ${item.price}")
        else:
            messagebox.showerror("Error", "Item not found")

    def add_item_to_menu(self):
        self.input_window = tk.Toplevel(self.root)
        tk.Label(self.input_window, text="Enter item name:").pack()
        self.name_entry = tk.Entry(self.input_window)
        self.name_entry.pack()
        tk.Label(self.input_window, text="Enter item price:").pack()
        self.price_entry = tk.Entry(self.input_window)
        self.price_entry.pack()
        tk.Button(self.input_window, text="Add", command=self.process_add).pack()

    def process_add(self):
        name = self.name_entry.get()
        price = int(self.price_entry.get())
        item = MenuItem(name, price)
        item.save()
        self.input_window.destroy()
        messagebox.showinfo("Success", "Item was added successfully")

    def remove_item_from_menu(self):
        self.input_window = tk.Toplevel(self.root)
        tk.Label(self.input_window, text="Enter item name to remove:").pack()
        self.remove_entry = tk.Entry(self.input_window)
        self.remove_entry.pack()
        tk.Button(self.input_window, text="Delete", command=self.process_remove).pack()

    def process_remove(self):
        name = self.remove_entry.get()
        item = MenuManager.get_by_name(name)
        self.input_window.destroy()
        if item:
            item.delete()
            messagebox.showinfo("Success", "Item was deleted successfully")
        else:
            messagebox.showerror("Error", "Item not found")

    def update_item_from_menu(self):
        self.input_window = tk.Toplevel(self.root)
        tk.Label(self.input_window, text="Enter current item name:").pack()
        self.old_name_entry = tk.Entry(self.input_window)
        self.old_name_entry.pack()
        tk.Label(self.input_window, text="Enter new item name:").pack()
        self.new_name_entry = tk.Entry(self.input_window)
        self.new_name_entry.pack()
        tk.Label(self.input_window, text="Enter new price:").pack()
        self.new_price_entry = tk.Entry(self.input_window)
        self.new_price_entry.pack()
        tk.Button(self.input_window, text="Update", command=self.process_update).pack()

    def process_update(self):
        old_name = self.old_name_entry.get()
        new_name = self.new_name_entry.get()
        new_price = int(self.new_price_entry.get())
        item = MenuManager.get_by_name(old_name)
        self.input_window.destroy() #fermer la fenetre
        if item:
            item.update(new_name, new_price)
            messagebox.showinfo("Success", "Item was updated successfully")
        else:
            messagebox.showerror("Error", "Item not found")

    def show_restaurant_menu(self):
        items = MenuManager.all_items()
        menu_text = "Restaurant Menu:\n"
        for item in items:
            menu_text += f"{item.name}: ${item.price}\n"
        messagebox.showinfo("Menu", menu_text)

    def exit_program(self):
        self.show_restaurant_menu() #afficher le menu
        self.root.quit()

if __name__ == "__main__": 
    root = tk.Tk() # fenetre principale
    app = MenuEditor(root) #fenetre secondaire
    root.mainloop()    #  boucle principale 