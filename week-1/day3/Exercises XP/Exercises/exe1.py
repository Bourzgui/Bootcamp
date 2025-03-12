class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# instances
cat1 = Cat("bibich", 1)
cat2 = Cat("louli", 3)
cat3 = Cat("nouri", 5)

def find_oldest_cat(*cats):
    return max(cats, key=lambda cat: cat.age)
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
def find_miniold_cat(*cats):
    return min(cats, key=lambda cat: cat.age)
miniold_cat = find_miniold_cat(cat1, cat2, cat3) 

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
print(f"The mini olde cat is {miniold_cat.name}, and is {miniold_cat.age} years old.")