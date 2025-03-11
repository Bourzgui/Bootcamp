from datetime import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def create_cake(candles):
    # Create the candles part
    candles_str = "i" * candles
    spaces = (11 - candles) // 2
    top_line = " " * 7 + "_" * spaces + candles_str + "_" * spaces

    # Create the cake
    cake = [
        top_line,
        "      |:H:a:p:p:y:|",
        "    __|___________|__",
        "   |^^^^^^^^^^^^^^^^^|",
        "   |:B:i:r:t:h:d:a:y:|",
        "   |                 |",
        "   ~~~~~~~~~~~~~~~~~~~"
    ]
    return "\n".join(cake)

# Get user's birthdate
while True:
    try:
        birthdate = input("Please enter your birthdate (DD/MM/YYYY): ")
        birth_date = datetime.strptime(birthdate, "%d/%m/%Y")
        break
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY")

# Calculate age
today = datetime(2025, 3, 10)  # Using the current date from metadata
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Get the last digit of age for candles
candles = age % 10

# Check if it's a leap year
birth_year = birth_date.year
is_leap = is_leap_year(birth_year)

# Print the cake(s)
print("\nHappy Birthday!")
print(create_cake(candles))

if is_leap:
    print("\ncake for being born in a leap year!")
    print(create_cake(candles))