# Demander à l'utilisateur un nombre et une longueur
number = int(input("Entrez un nombre: "))
length = int(input("Entrez la longueur souhaitée: "))

# Créer la liste des multiples
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

# Afficher le résultat
print(f"\nnumber: {number} - length {length} ➞ {multiples}")
