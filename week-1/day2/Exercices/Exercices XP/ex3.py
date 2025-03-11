# 1 
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# 2
brand["number_stores"] = 2

# 3 
print("Zara's clients are:", ", ".join(brand["type_of_clothes"]))

# 4 
brand["country_creation"] = "Spain"

# 5 
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6 
del brand["creation_date"]

# 7 
print("Last international competitor:", brand["international_competitors"][-1])

# 8 
print("Major clothes colors in the US:", ", ".join(brand["major_color"]["US"]))

# 9 
print("Number of key-value pairs:", len(brand))

# 10 
print("Dictionary keys:", list(brand.keys()))

# 11 
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# 12 
brand.update(more_on_zara)

# 13
print("Number of stores:", brand["number_stores"])
print("The number of stores changed from 2 to 10000 because we updated the dictionary with new values from more_on_zara")