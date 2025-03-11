def get_letter_indices(word):
    letter_dict = {}
    for index, letter in enumerate(word):
        if letter not in letter_dict:
            letter_dict[letter] = []
        letter_dict[letter].append(index)
    return letter_dict

def main():
    word = input("Enter a word: ")
    result = get_letter_indices(word)
    print(result)
    print("\nExamples:")
    examples = ["dodo", "froggy", "grapes"]
    for example in examples:
        print(f'"{example}" ➞ {get_letter_indices(example)}')

if __name__ == "__main__":
    main()