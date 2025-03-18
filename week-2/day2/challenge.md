 # 🚀 Daily challenge : SQL Puzzle
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
---

### 🔍Q2 :
```sql
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
```
---

### 🔍 **Q3 :**
```sql
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
```
 
---

### 🔍 **Q4 :**
```sql
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
```
---
### 🏆 **Résumé des Prédictions**
| **Query** | **Résultat Attendu** |
|-----------|----------------|
| **Q1** | `0` |
| **Q2** | `2` |
| **Q3** | `0` |
| **Q4** | `2` |

------
 
=======
## 🚀OUTPUT 
![Local Image](./data-1.csv)
![Local Image](./data-2.csv)
![Local Image](./data-3.csv)
![Local Image](./data-4.csv)
 
