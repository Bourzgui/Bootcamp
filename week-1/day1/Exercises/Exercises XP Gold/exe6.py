import random

games_won = 0
games_lost = 0

while True:
    try:
        user_num = int(input("Enter a number between 1 and 9 (or 0 to quit): "))
        if user_num == 0:
            break
        if not 1 <= user_num <= 9:
            print("Please enter a number between 1 and 9")
            continue
            
        computer_num = random.randint(1, 9)
        
        if user_num == computer_num:
            print("Winner!")
            games_won += 1
        else:
            print(f"Better luck next time. The number was {computer_num}")
            games_lost += 1
            
    except ValueError:
        print("Please enter a valid number")

print(f"\nGame Over!")
print(f"Games won: {games_won}")
print(f"Games lost: {games_lost}")