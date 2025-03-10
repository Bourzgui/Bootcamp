# Créer un ensemble avec mes nombres favoris
my_fav_numbers = {7, 13, 23, 42, 99}
print("Mes nombres favoris initiaux:", my_fav_numbers)

# Ajouter deux nouveaux nombres
my_fav_numbers.add(8)
my_fav_numbers.add(15)
print("Après ajout de deux nombres:", my_fav_numbers)

# Convertir en liste pour pouvoir retirer le dernier élément
numbers_list = list(my_fav_numbers)
numbers_list.pop()
my_fav_numbers = set(numbers_list)
print("Après suppression du dernier nombre:", my_fav_numbers)

# Créer l'ensemble des nombres favoris de mon ami
friend_fav_numbers = {3, 11, 21, 33}
print("Nombres favoris de mon ami:", friend_fav_numbers)

# Concaténer les deux ensembles
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Nos nombres favoris combinés:", our_fav_numbers)