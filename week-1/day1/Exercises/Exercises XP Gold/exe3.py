
my_name = "Bourzgui"  
# Keep asking for name until it matches
while True:
    user_input = input("Please enter a name: ")
    if user_input == my_name:
        print(f"Hello {my_name}!")
        break
    print("That's not my name. Try again!")