# Initialize the longest sentence length
longest_length = 0

print("Welcome to the 'No Letter A' Challenge!")
print("Try to write the longest sentence without using the letter 'A' or 'a'")
print("Type 'quit' to exit the game")

while True:
    # Get user input
    sentence = input("\nEnter your sentence: ")
    
    # Check if user wants to quit
    if sentence.lower() == 'quit':
        print(f"\nGame Over! Your longest valid sentence was {longest_length} characters long.")
        break
    
    # Check if sentence contains 'a' or 'A'
    if 'a' in sentence.lower():
        print("Sorry! Your sentence contains the letter 'A'. Try again!")
        continue
    
    # Check if this is the longest valid sentence
    current_length = len(sentence)
    if current_length > longest_length:
        longest_length = current_length
        print(f"Congratulations! New record: {longest_length} characters!")
    else:
        print(f"Good try! But not longer than your best: {longest_length} characters.")