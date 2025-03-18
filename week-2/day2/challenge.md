 
| **FirstTab** |        |
|-------------|--------|
| ID         | Name   |
| 5          | Pawan  |
| 6          | Sharlee|
| 7          | Krish  |
| NULL       | Avtaar |

| **SecondTab** |
|-------------|
| ID         |
| 5         |
| NULL      |


### 🔍Q1 :
```sql
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
```
#### **Prédiction du Résultat**  
- La sous-requête `SELECT id FROM SecondTab WHERE id IS NULL` retourne `NULL`.  
- `ft.id NOT IN (NULL)` donne **NULL** pour chaque ligne de `FirstTab`, ce qui signifie qu'aucune ligne ne satisfait la condition.  
- Résultat : **0**  

---

### 🔍Q2 :
```sql
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
```
#### Prédiction du Résultat  
- `SELECT id FROM SecondTab WHERE id = 5` retourne `{5}`.  
- `ft.id NOT IN (5)` sélectionne toutes les lignes de `FirstTab` sauf celles où `id = 5`.  
- Les valeurs restantes sont `{6, 7, NULL}`.  
- `NULL NOT IN (5)` est **inconnu (NULL)**, donc cette ligne n'est pas comptée.  
- Résultat : **2** (lignes avec `id = 6` et `id = 7`)

---

### 🔍 **Q3 :**
```sql
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
```
#### **Prédiction du Résultat**  
- `SELECT id FROM SecondTab` retourne `{5, NULL}`.  
- `ft.id NOT IN (5, NULL)` entraîne une **ambiguïté** (car `NOT IN` avec `NULL` donne toujours NULL).  
- Par conséquent, **aucune ligne ne satisfait la condition**.  
- Résultat : **0**  

---

### 🔍 **Q4 :**
```sql
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
```
#### **Prédiction du Résultat**  
- `SELECT id FROM SecondTab WHERE id IS NOT NULL` retourne `{5}`.  
- `ft.id NOT IN (5)` sélectionne `{6, 7, NULL}`.  
- `NULL NOT IN (5)` est **NULL**, donc cette ligne est ignorée.  
- Résultat : **2** (`id = 6` et `id = 7`)

---

### 🏆 **Résumé des Prédictions**
| **Query** | **Résultat Attendu** |
|-----------|----------------|
| **Q1** | `0` |
| **Q2** | `2` |
| **Q3** | `0` |
| **Q4** | `2` |

---

💡 **Prochaine Étape :** Exécuter les requêtes pour valider ces résultats. Dis-moi si tu veux que je t'explique comment tester ces requêtes ! 🚀