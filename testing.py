from Morse_Code_Translator import english_to_morse, morse_to_english, MorseCodeError  # Importing functions and exceptions from Morse_Code_Translator module
import unittest  # Importing the 'unittest' module for testing

class TestMorseCodeConversion(unittest.TestCase):
    
    # Testing English to Morse code conversion for 'PYTHON'
    def test_english_to_morse_conversion(self):
        expected_result = '.--. -.-- - .... --- -.'  # Expected Morse code for 'PYTHON'
        actual_result = english_to_morse('PYTHON')  # Converting 'PYTHON' to Morse code
        self.assertEqual(actual_result, expected_result, f"Expected: {expected_result}\nActual: {actual_result}")  # Checking if the actual result matches the expected result
   # Testing Morse code to English conversion for '.--. -.-- - .... --- -.'
    def test_morse_to_english_conversion(self):
        expected_result = 'PYTHON'  # Expected English text for the provided Morse code
        actual_result = morse_to_english('.--. -.-- - .... --- -.')  # Converting Morse code to English
        self.assertEqual(actual_result, expected_result, f"Expected: {expected_result}\nActual: {actual_result}")  # Checking if the actual result matches the expected result

    # Testing invalid characters for English to Morse code conversion
    def test_invalid_english_characters(self):
        with self.assertRaises(MorseCodeError):  # Checking if MorseCodeError is raised for invalid English characters
            english_to_morse('#Invalid#')

    # Testing invalid Morse code for Morse to English conversion
    def test_invalid_morse_code(self):
        with self.assertRaises(MorseCodeError):  # Checking if MorseCodeError is raised for invalid Morse code
            morse_to_english('.... . .-.. .-.. --- / .-- --- .-. .-.. -.. #Invalid#')

    # Testing empty input for English to Morse code conversion
    def test_empty_input_english_to_morse(self):
        self.assertEqual(english_to_morse(''), '')  # Checking if empty input returns an empty string

    # Testing empty input for Morse code to English conversion
    def test_empty_input_morse_to_english(self):
        self.assertEqual(morse_to_english(''), '')  # Checking if empty Morse code input returns an empty string

if __name__ == '__main__':
    unittest.main()  # Running the unit tests if this file is executed as a script