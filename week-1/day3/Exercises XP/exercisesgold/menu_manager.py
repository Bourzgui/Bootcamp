class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        
        new_dish = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(new_dish)
        print(f"Le plat '{name}' a été ajouté au menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"Le plat '{name}' a été mis à jour.")
                return
        print(f"Erreur: Le plat '{name}' n'est pas dans le menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                self.menu.remove(dish)
                print(f"Le plat '{name}' a été supprimé du menu.")
                print("Menu mis à jour:", self.menu)
                return
        print(f"Erreur: Le plat '{name}' n'est pas dans le menu.")

if __name__ == "__main__":
    manager = MenuManager()
    
    print("Menu initial:")
    for dish in manager.menu:
        print(dish)
    
    print("\nTests des méthodes:")

    manager.add_item("Pizza", 20, "B", True)
    
    manager.update_item("Soup", 12, "A", False)
    
    manager.remove_item("Salad")
    
    manager.update_item("Sushi", 15, "A", False)
    manager.remove_item("Sushi")