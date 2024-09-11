def vigenere_solve(cipher_text, key_length):
    # Initialize an empty list to store the solved text
    solved_text = []
    
    # Split the cipher text into chunks of the key length
    chunks = [cipher_text[i:i+key_length] for i in range(0, len(cipher_text), key_length)]
    
    # Iterate through each chunk
    for chunk in chunks:
        # Initialize a dictionary to store the letter counts
        letter_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                         'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                         'Y': 0, 'Z': 0}
        
        # Count the occurrences of each letter in the chunk
        for letter in chunk:
            letter_counts[letter] += 1
        
        # Find the most frequent letter in the chunk
        most_frequent_letter = max(letter_counts, key=letter_counts.get)
        
        # Calculate the shift based on the most frequent letter
        shift = ord(most_frequent_letter) - ord('A')
        
        # Add the solved letter to the solved text
        for letter in chunk:
            if letter.isupper():
                solved_text.append(chr((ord(letter) - shift - ord('A')) % 26 + ord('A')))
            else:
                solved_text.append(chr((ord(letter) - shift - ord('a')) % 26 + ord('a')))
            
    # Convert the list of characters to a string
    solved_text = ''.join(solved_text)
    
    # Return the solved text
    return solved_text

cipher_text = input("Enter the cypher text: ")
key_length = int(input("Enter the suspected key length: "))
solved_text = vigenere_solve(cipher_text, key_length)
print(solved_text)