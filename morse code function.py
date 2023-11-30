# Define a custom exception class for Morse code errors
class MorseCodeError(Exception):
    pass

def english_to_morse(text):
    # Dictionary mapping English characters to Morse code
    encrypt = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'
    }

    morse_text = []  # Placeholder for storing Morse code text
    for char in text:
        # Check if the character is not a valid English character or space
        if char.upper() not in encrypt and char != ' ':
            # Raise an error if the character is not in the Morse code dictionary
            raise MorseCodeError(f"Error: Character '{char}' is not in the Morse code dictionary.")
        # Convert character to Morse code and append to the list
        morse_text.append(encrypt.get(char.upper(), ''))  