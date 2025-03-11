 # List of names
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Get user input
user_name = input("Please enter a name: ")

# Check if name exists and get index
if user_name in names:
    index = names.index(user_name)
    print(f"The first occurrence of {user_name} is at index {index}")
else:
    print(f"{user_name} is not in the list")