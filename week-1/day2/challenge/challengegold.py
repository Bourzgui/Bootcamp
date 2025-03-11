def create_matrix():
    return [
        ['7', 'i', 'i'],
        ['T', 's', 'x'],
        ['h', '%', '?'],
        ['i', ' ', '#'],
        ['s', 'M', ' '],
        ['$', 'a', ' '],
        ['#', 't', '%'],
        ['^', 'r', '!']
    ]

def is_alpha(char):
    return char.isalpha()

def decode_matrix(matrix):
    if not matrix or not matrix[0]:
        return ""
    
    rows = len(matrix) # nbr element in row
    cols = len(matrix[0])
    message = []
    last_was_alpha = False
    
    for col in range(cols):
        for row in range(rows):
            char = matrix[row][col]
            
            if is_alpha(char):
                if not last_was_alpha and message and message[-1] != ' ':
                    message.append(' ')
                message.append(char)
                last_was_alpha = True
            else:
                last_was_alpha = False
    
    return ''.join(message).strip() #enlève les espaces au début et à la fin d'une chaîne

def main():
    matrix = create_matrix()
    print("Original Matrix:")
    for row in matrix:
        print(row)
    
    secret_message = decode_matrix(matrix)
    print("\nSecret Message:")
    print(secret_message)

if __name__ == "__main__":
    main()