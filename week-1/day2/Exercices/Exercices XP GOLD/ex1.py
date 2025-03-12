import random

# Exercise 1: Birthday Look-up
birthdays = {
    "Alice": "1995/04/23",
    "Bob": "1987/11/15",
    "Charlie": "2000/06/30",
    "David": "1992/09/12",
    "Eve": "1985/02/05"
}

print("Welcome! You can look up the birthdays of the people in the list!")
name = input("Enter a name: ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")

# Exercise 2: Birthdays Advanced
print("Here are the names in the database:")
for person in birthdays.keys():
    print(person)
name = input("Enter a name: ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")

# Exercise 3: Sum
def sum_pattern(x: int) -> int:
    return x + int(str(x) * 2) + int(str(x) * 3) + int(str(x) * 4)

x = int(input("Enter an integer: "))
print(f"Result: {sum_pattern(x)}")

# Exercise 4: Double Dice
def throw_dice() -> int:
    return random.randint(1, 6)

def throw_until_doubles() -> int:
    count = 0
    while True:
        die1, die2 = throw_dice(), throw_dice()
        count += 1
        if die1 == die2:
            break
    return count

def main():
    results = [throw_until_doubles() for _ in range(100)]
    total_throws = sum(results)
    average_throws = round(total_throws / 100, 2)
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws}")

if __name__ == "__main__":
    main()
