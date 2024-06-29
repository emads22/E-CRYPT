
# International Morse Code Table, contains uppercase alphabetical letters and digits from 0 to 9 only without any special characters
INTERNATIONAL_MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
                            'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


# Binary Code Table, contains all alphabetical letters (uppercase and lowercase) and digits and special characters
BINARY_CODE = {' ': '00100000', '!': '00100001', '"': '00100010', '#': '00100011', '$': '00100100', '%': '00100101', '&': '00100110',
               "'": '00100111', '(': '00101000', ')': '00101001', '*': '00101010', '+': '00101011', ',': '00101100', '-': '00101101',
               '.': '00101110', '/': '00101111', '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011', '4': '00110100',
               '5': '00110101', '6': '00110110', '7': '00110111', '8': '00111000', '9': '00111001', ':': '00111010', ';': '00111011',
               '<': '00111100', '=': '00111101', '>': '00111110', '?': '00111111', '@': '01000000', 'A': '01000001', 'B': '01000010',
               'C': '01000011', 'D': '01000100', 'E': '01000101', 'F': '01000110', 'G': '01000111', 'H': '01001000', 'I': '01001001',
               'J': '01001010', 'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000',
               'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111',
               'X': '01011000', 'Y': '01011001', 'Z': '01011010', '[': '01011011', '\\': '01011100', ']': '01011101', '^': '01011110',
               '_': '01011111', '`': '01100000', 'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101',
               'f': '01100110', 'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100',
               'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001', 'r': '01110010', 's': '01110011',
               't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000', 'y': '01111001', 'z': '01111010',
               '{': '01111011', '|': '01111100', '}': '01111101', '~': '01111110'}


def can_encrypt_morse(text):
    # checks if text can be encrypted in morse code

    # loop in every letter of the text
    for letter in text:
        # if the letter is space (or even several spaces), ignore and keep looping since its just to separate words
        if letter == " ":
            continue
        # in every letter of text (convert it to uppercase) check if its a valid letter for encryption (present in keys of morse code dict)
        if letter.upper() not in INTERNATIONAL_MORSE_CODE.keys():
            return False
    return True


def can_encrypt_binary(text):
    # checks if text can be encrypted in binary code

    for letter in text:
        # if the letter is space (or even several spaces), ignore and keep looping since its just to separate words
        if letter == " ":
            continue
        # in every letter of text check if its a valid letter for encryption (present in keys of binary code dict)
        if letter not in BINARY_CODE.keys():
            return False
    return True


def is_morse_code(cipher):
    # checks if cipher is a valid morse code

    # loop in every word of cipher (after converting the latter to a list with delimiter " / ")
    for word in cipher.split(" / "):
        # in every letter of this word (after converting the latter to a list with delimiter 1 space) check if its a valid letter for
        # decryption (present in values of morse code dict)
        for letter in word.split(" "):
            if letter not in INTERNATIONAL_MORSE_CODE.values():
                return False
    return True


def is_binary_code(cipher):
    # checks if cipher is a valid binary code

    # in every letter of this cipher (after converting the latter to a list with delimiter 1 space) check if its a valid letter for
    # decryption (present in values of morse code dict)
    for letter in cipher.split(" "):
        if letter not in BINARY_CODE.values():
            return False
    return True




