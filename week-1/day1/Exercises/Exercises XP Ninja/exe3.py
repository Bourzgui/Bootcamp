# Store the paragraph in a variable
paragraph = """Python is a versatile programming language created by Guido van Rossum. It emphasizes code readability with its notable use of significant whitespace. Python's features include an intuitive syntax and powerful libraries for data manipulation. Many developers choose Python because it supports multiple programming paradigms, including procedural, object-oriented, and functional programming. The language's simplicity and extensive documentation make it an excellent choice for beginners."""

# Function to count sentences (basic implementation)
def count_sentences(text):
    # Count periods, exclamation marks, and question marks that end sentences
    return len([char for char in text if char in '.!?'])

# Get basic stats
total_chars = len(paragraph)
total_sentences = count_sentences(paragraph)
words = paragraph.split()
total_words = len(words)
unique_words = len(set(words))

# Get bonus stats
non_whitespace = len([char for char in paragraph if not char.isspace()])
avg_words_per_sentence = total_words / total_sentences if total_sentences > 0 else 0
non_unique_words = total_words - unique_words

# Print the analysis
print("Paragraph Analysis:")
print("-" * 20)
print(f"1. Total characters: {total_chars}")
print(f"2. Total sentences: {total_sentences}")
print(f"3. Total words: {total_words}")
print(f"4. Unique words: {unique_words}")
print("\nBonus Statistics:")
print("-" * 20)
print(f"5. Non-whitespace characters: {non_whitespace}")
print(f"6. Average words per sentence: {avg_words_per_sentence:.2f}")
print(f"7. Non-unique words: {non_unique_words}")