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

    return ' '.join(morse_text)  # Join the Morse code characters to form the final Morse code string
def morse_to_english(text):
    # Dictionary mapping Morse code to English characters
    encrypt = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'
    }
    decrypt = {value: key for key, value in encrypt.items()}  # Create a dictionary for decoding Morse code

    translated_words = []  # Placeholder for storing translated words
    for word in text.split('/'):  # Split input text by '/'
        for char in word.split():  # Split words by space to get individual Morse code characters
            if char not in decrypt:
                # Raise an error if the Morse code character is not in the Morse code dictionary
                raise MorseCodeError(f"Error: Character '{char}' is not in the Morse code dictionary.")
            # Append decoded character to the translated words
            translated_words.append(decrypt[char])

        translated_words.append(' ')  # Add a space after each word
    return ''.join(translated_words).rstrip()  # Join the translated words and remove trailing whitespac
