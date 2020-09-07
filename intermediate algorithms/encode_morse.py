# create a function that takes a string as an argument and return a non-encoded, encrypted string

def encode(string):
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }

    # make the whole string uppercase letters
    string = string.upper()

    # convert a string to a list
    def convert_to_list(string):
        letters = []
        # this will "push" each letter into the letters list as a new index
        letters[:0] = string
        return letters

    letter_list = convert_to_list(string)

    # declaring an empty list to add morse codes
    morse = []

    # finds the morse code, appends to morse list
    for let in letter_list:
        morse_letter = char_to_dots[let]
        morse.append(morse_letter)

    # joins the list with a space seperation
    morse_string = " ".join(morse)

    return morse_string


print(encode("EDABBIT CHALLENGE"))
print("\n. -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .")
# print(encode("HELP me !"))
