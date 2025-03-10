# Liste initiale des commandes
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
print("Commandes initiales:", sandwich_orders)

# Supprimer tous les sandwichs au pastrami
print("\nDésolé, nous n'avons plus de pastrami!")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

print("Commandes après retrait du pastrami:", sandwich_orders)

# Préparer les sandwichs
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Je prépare votre {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

# Afficher tous les sandwichs préparés
print("\nTous les sandwichs ont été préparés:")
for sandwich in finished_sandwiches:
    print(f"J'ai préparé votre {sandwich}")