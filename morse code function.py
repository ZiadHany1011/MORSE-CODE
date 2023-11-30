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
# Loop for the translation menu
while True:
    print("\nChoose an option:")  # Print the options for the translation menu
    print("1. Translate from English to Morse")
    print("2. Translate from Morse to English")
    print("0. Exit")

    choice = input("Enter your choice: ")  # Prompt the user to input their choice

    try:
        if choice == '1':  # Check if the user chose to translate from English to Morse
            while True:
                text = input('Enter the text to translate to Morse code: ')  # Input text to translate to Morse code
                if text.strip():
                    # Check if the input text contains only valid English characters and spaces
                    if all(char.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ' for char in text):
                        translated_text = english_to_morse(text)  # Translate input text to Morse code
                        print("Translated Text (English to Morse):", translated_text)
                        break
                    else:
                        raise MorseCodeError("Error: Input contains characters not in the Morse code dictionary.")
                else:
                    raise MorseCodeError("Error: Please enter some text.")
        elif choice == '2':  # Check if the user chose to translate from Morse to English
            while True:
                text = input('Enter the Morse code to translate to English (use space between each letter and "/" between each word): ')
                if text.strip():
                    # Check if the input Morse code contains valid Morse code characters
                    if all(code in ['.', '-', '/', ' '] for code in text):
                        translated_text = morse_to_english(text)  # Translate input Morse code to English
                        print("Translated Text (Morse to English):", translated_text)
                        break
                    else:
                        raise MorseCodeError("Error: Input contains characters not in the Morse code dictionary.")
                else:
                    raise MorseCodeError("Error: Please enter some text.")
        elif choice == '0':  # Check if the user chose to exit the program
            print("Exiting the translator...")  # Print an exit message
            break
        else:
            raise MorseCodeError("Error: Invalid choice. Please choose a valid option (0, 1, or 2).")  # Raise an error for an invalid choice
    
    except MorseCodeError as e:
        print(e)  # Print the specific error message for Morse code errors
    except Exception as e:
        print("An unexpected error occurred:", str(e))  # Print a generic error message for unexpected errors