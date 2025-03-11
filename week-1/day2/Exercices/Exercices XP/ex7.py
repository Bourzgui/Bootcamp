import random

def get_season_from_month(month):
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    else:
        return 'autumn'

def get_random_temp(season):
    temp_ranges = {
        'winter': (-10, 16),
        'spring': (0, 23),
        'summer': (16, 40),
        'autumn': (8, 28)
    }
    min_temp, max_temp = temp_ranges[season]
    return round(random.uniform(min_temp, max_temp), 1)

def get_temperature_advice(temp):
    if temp < 0:
        return " that's freezing! Wear some extra layers today"
    elif 0 <= temp < 16:
        return "Quite chilly! Don't forget your coat"
    elif 16 <= temp < 23:
        return "Pleasant temperature. Perfect for a light jacket!"
    elif 23 <= temp < 32:
        return "Warm weather! Time for t-shirts"
    else:
        return "Hot day! Don't forget to stay hydrated"

def main():
    try:
        month = int(input("Enter the month number (1-12): "))
        if not 1 <= month <= 12:
            print("Invalid month. Please enter a number between 1 and 12.")
            return
            
        season = get_season_from_month(month)
        temperature = get_random_temp(season)
        
        print(f"\nFor month {month} ({season})")
        print(f"The temperature right now is {temperature} degrees Celsius.")
        print(get_temperature_advice(temperature))
        
    except ValueError:
        print("Please enter a valid number between 1 and 12.")

if __name__ == "__main__":
    main()