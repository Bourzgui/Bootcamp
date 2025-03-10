# Créer le panier initial
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("Panier initial:", basket)

# Supprimer Banana
basket.remove("Banana")
print("Après suppression de Banana:", basket)

# Supprimer Blueberries
basket.remove("Blueberries")
print("Après suppression de Blueberries:", basket)

# Ajouter Kiwi à la fin
basket.append("Kiwi")
print("Après ajout de Kiwi:", basket)

# Ajouter Apples au début
basket.insert(0, "Apples")
print("Après ajout de Apples au début:", basket)

# Compter les pommes
apple_count = basket.count("Apples")
print("Nombre de pommes dans le panier:", apple_count)

# Vider le panier
basket.clear()
print("Panier après vidage:", basket)