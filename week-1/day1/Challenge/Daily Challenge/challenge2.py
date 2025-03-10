# Demander un mot à l'utilisateur
word = input("Entrez un mot: ")
# Fonction pour supprimer les lettres consécutives en double
def remove_duplicates(text):
    if len(text) <= 1:
        return text
    
    result = text[0]  # Garder la première lettre
    for char in text[1:]:
        # Ajouter la lettre seulement si elle est différente de la dernière lettre ajoutée
        if char != result[-1]:
            result += char
    return result

# Afficher le résultat
cleaned_word = remove_duplicates(word)
print(f"\nuser's word : \"{word}\" ➞ \"{cleaned_word}\"")
