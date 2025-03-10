# Créer un tuple avec des entiers
my_tuple = (1, 2, 3, 4, 5)
print("Tuple original:", my_tuple)
try:
    my_tuple.append(6)  # Ceci va générer une erreur
except AttributeError as e:
    print("\nErreur lors de la tentative d'ajout:", e)
    print("Les tuples sont immuables - on ne peut pas les modifier!")

# La seule façon de "modifier" un tuple est de créer un nouveau tuple
new_tuple = my_tuple + (6,)
print("\nNouveau tuple créé par concaténation:", new_tuple)
print("Tuple original (inchangé):", my_tuple)