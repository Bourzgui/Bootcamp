# Exercise 2: Movie Tickets

def calculate_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

def calculate_family_cost(family_dict):
    total_cost = 0
    print(f"\nNumber of family members: {len(family_dict)}")
    print("Individual ticket prices:")
    for name, age in family_dict.items():
        price = calculate_ticket_price(age)
        total_cost += price
        print(f"{name.capitalize()} (age {age}) has to pay: ${price}")
    return total_cost
# Part 1 
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
print("\n--- Given Family Tickets ---")
total_cost = calculate_family_cost(family)
print(f"Total cost for the family: ${total_cost}")

# Part 2
 
print("\n--- Enter Custom Family Members ---")
custom_family = {}
while True:
    name = input("\nEnter family member's name (or 'done' to finish): ").lower()
    if name == 'done':
        break
    try:
        age = int(input("Enter their age: "))
        custom_family[name] = age
    except ValueError:
        print("Please enter a valid age!")

if custom_family:
    print("\n--- Custom Family Tickets ---")
    total_custom_cost = calculate_family_cost(custom_family)
    print(f"Total cost for the custom family: ${total_custom_cost}")
