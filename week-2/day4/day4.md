# Gestion de Menus, Authentification et Données de Pays avec Python 🐍
Day4 on a trois projets Python démontrant l'utilisation de Tkinter pour les interfaces graphiques, SQLite pour la gestion de bases de données, et des appels API pour récupérer des données. Voici un aperçu des projets inclus :

## 1. Restaurant Menu Manager 🍽️
**Fichier :** `menu_editor.py`

### Description
Une application graphique pour gérer un menu de restaurant. Créez, modifiez, supprimez et affichez des plats avec leurs prix.

### Fonctionnalités ✨
- **Ajouter** : Créez un nouvel élément avec un nom et un prix ➕
- **Supprimer** : Retirez un élément existant 🗑️
- **Mettre à jour** : Modifiez le nom ou le prix d’un élément ✏️
- **Afficher** : Consultez la liste complète du menu 📋
- **Voir** : Affichez les détails d’un élément spécifique 🔍

### Prérequis
- Python 3.x
- Modules : `tkinter` (inclus avec Python)

### Utilisation
1. Exécutez le script :
   ```bash
   python menu_editor.py
   ```
2. Une fenêtre s’ouvre avec des boutons pour gérer le menu.

### Exemple
- Ajouter "Pizza" avec un prix de 12 $ :
  - Cliquez sur "Add an Item", entrez "Pizza" et "12", puis validez.
  - Message : "Item was added successfully".

---

## 2. Authentication System 🔒
**Fichier :** `auth_app.py`

### Description
Un système d’authentification sécurisé avec inscription et connexion. Les mots de passe sont hachés avec un sel pour une sécurité accrue.

### Fonctionnalités ✨
- **Connexion** : Vérifiez les identifiants existants 🔐
- **Inscription** : Créez un nouveau compte avec un nom d’utilisateur unique 📝
- **Sécurité** : Hachage SHA-256 avec sel pour les mots de passe 🔑
- **Base de données** : Stockage persistant dans SQLite 💾

### Prérequis
- Python 3.x
- Modules : `tkinter`, `sqlite3`, `hashlib`, `os` (tous inclus avec Python)

### Utilisation
1. Exécutez le script :
   ```bash
   python auth_app.py
   ```
2. Une fenêtre s’ouvre pour vous connecter ou vous inscrire.

### Exemple
- Inscription :
  - Entrez "alice" comme nom d’utilisateur et "secret123" comme mot de passe.
  - Cliquez sur "Sign Up" → "Signup successful!"
- Connexion :
  - Entrez "alice" et "secret123", cliquez sur "Login" → "Logged in as alice".

---
 3. Random Countries Database 🌍
 
### Description
Un script qui récupère des données sur 10 pays aléatoires via l’API REST Countries et les stocke dans une base SQLite.

### Fonctionnalités ✨
- **Récupération** : Appel API pour obtenir des données de pays 🌐
- **Stockage** : Sauvegarde dans une table SQLite (nom, capitale, drapeau, sous-région, population) 🗄️
- **Affichage** : Liste des pays en console 🖨️
- **Aléatoire** : Sélection de 10 pays au hasard 🎲

### Prérequis
- Python 3.x
- Modules : `requests`, `sqlite3` (inclus), `random` (inclus)
- Connexion Internet pour l’API

### Utilisation
1. Installez `requests` si nécessaire :
   ```bash
   pip install requests
   ```
### Exemple de sortie
```
Successfully added 10 random countries to the database!
ID: 1, Name: Japan, Capital: Tokyo, Population: 125360000
ID: 2, Name: Brazil, Capital: Brasília, Population: 212559417
...
```

---
 
 

 