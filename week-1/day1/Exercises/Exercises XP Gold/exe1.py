 # Get month number from user
try:
    month = int(input("Enter a month number (1-12): "))
    
    if not 1 <= month <= 12:
        print("Please enter a valid month number between 1 and 12")
    else:
        # Determine season based on month
        if month in [3, 4, 5]:
            season = "Spring"
        elif month in [6, 7, 8]:
            season = "Summer"
        elif month in [9, 10, 11]:
            season = "Autumn"
        else:  # month in [12, 1, 2]
            season = "Winter"
            
        print(f"The season for month {month} is: {season}")
        
except ValueError:
    print("Please enter a valid number")