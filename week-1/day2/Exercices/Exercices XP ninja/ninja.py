# Exercise 1 
cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = cars_string.split(", ")
 
print(f"There are {len(cars_list)} manufacturers in the list.")
print("Manufacturers in descending order:", sorted(cars_list, reverse=True))

# with 'o'
names_with_o = [car for car in cars_list if 'o' in car.lower()]
print(f"{len(names_with_o)} manufacturers have the letter 'o'.")

#  without 'i'
names_without_i = [car for car in cars_list if 'i' not in car.lower()]
print(f"{len(names_without_i)} manufacturers do not have the letter 'i'.")

# Handling duplicates
duplicate_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_cars = list(set(duplicate_list))
print(f"Unique manufacturers: {', '.join(unique_cars)}")
print(f"There are now {len(unique_cars)} unique manufacturers.")
 
reversed_names = sorted([car[::-1] for car in unique_cars])
print("Manufacturers with reversed names (A-Z):", reversed_names)

# Exercise 2 
def get_full_name(first_name, last_name, middle_name=""):
    if middle_name:
        return f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    return f"{first_name.capitalize()} {last_name.capitalize()}"

# Testing get_full_name()
print(get_full_name("john", "lee", "hooker"))
print(get_full_name("bruce", "lee"))

# Exercise 3
def english_to_morse(text):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ' ': '/',
    }
    return ' '.join(morse_dict[char.upper()] for char in text if char.upper() in morse_dict)

def morse_to_english(morse):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '-----': '0', '/': ' '
    }
    return ''.join(morse_dict[code] for code in morse.split())

print(english_to_morse("hello world"))
print(morse_to_english(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))
