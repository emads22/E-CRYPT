
from helpers import INTERNATIONAL_MORSE_CODE, BINARY_CODE
import winsound             # for audio beeps
import pyttsx3              # for text speech
import time


# ---------------------------------------- Encryption Functions ----------------------------------------


def morse_encode(plaintext):
    # encodes a text to morse code cipher text

    # list to store cipher
    cipher_list = []
    # loop in every word in text (after converting the latter to a list with delimiter 1 space)
    for word in plaintext.split(" "):
        # reset cipher word at every loop
        cipher_word = ""
        for letter in word:
            # break loop in case of sequence of spaces (where split() didn't catch but 1) and don't add it to cipher_word for better result
            if letter == " ":
                break
            # loop in every letter of word (convert it to uppercase), convert it to morse code and concatenate it wth space to cipher_word
            else:
                cipher_word += INTERNATIONAL_MORSE_CODE[letter.upper()] + " "
        # if nothing concatenated to cipher_word in case of sequence of spaces (word of spaces), such word would not be appended to list.
        # Otherwise (after finishing the word) append it to the list.
        if cipher_word != "":
            cipher_list.append(cipher_word)
    # convert the cipher list to a string by adding '/ ' (joiner) between words (there's 1 space before slash from above concatenation)
    cipher = "/ ".join(cipher_list)
    # remove last space using strip()
    return cipher.strip()


def binary_encode(plaintext):
    # encodes a text to binary code cipher text

    # list to store cipher
    cipher_list = []
    # loop in every word in text (after converting the latter to a list with delimiter 1 space)
    for word in plaintext.split(" "):
        # reset cipher word at every loop
        cipher_word = ""
        for letter in word:
            # break loop in case of sequence of spaces (where split() didn't catch but 1) and don't add it to cipher_word for better result
            if letter == " ":
                break
            # loop in every letter of current word and convert it to binary code and concatenate it wth 1 space to cipher_word
            else:
                cipher_word += BINARY_CODE[letter] + " "
        # if nothing concatenated to cipher_word in case of sequence of spaces (word of spaces), such word would not be appended to list.
        # Otherwise (after finishing the word) append it to the list
        if cipher_word != "":
            # after each word concatenate cipher_word wth the binary code of 1 space (to have a neat result)
            cipher_word += BINARY_CODE[" "]
            # after finishing the word append it to the list
            cipher_list.append(cipher_word)
    # convert the cipher list to a string by adding 1 space (joiner) between words (there's 1 space between letters of binary code)
    cipher = " ".join(cipher_list)
    return cipher


# ---------------------------------------- Decryption Functions ----------------------------------------


def decrypt_letter_morse(code):
    # decrypts one letter in morse code to original alphabetical letter

    # loop in (key, value) of morse code dict and return key once code is found
    for letter, morse_code in INTERNATIONAL_MORSE_CODE.items():
        if code == morse_code:
            return letter


def morse_decode(cipher):
    # decodes a morse code cipher to plain text

    # list to store plain text result
    plaintext_list = []
    # loop in every word in cipher (after converting the latter to a list with delimiter " / ")
    for word in cipher.split(" / "):
        # reset plaintext word at every loop
        plain_word = ""
        # loop in every letter of current word (after converting the latter to a list with delimiter 1 space)
        for letter in word.split(" "):
            # decrypt this morse code letter
            plain_word += decrypt_letter_morse(letter)
        # after finishing the plaintext word append it to the plaintext list
        plaintext_list.append(plain_word)
    # convert the plain text list to a string by adding 1 space (joiner) between words
    plaintext = " ".join(plaintext_list)
    return plaintext


def decrypt_letter_binary(code):
    # decrypts one letter in binary code to original letter

    # loop in (key, value) of binary code dict and return key once code is found
    for letter, byte in BINARY_CODE.items():
        if code == byte:
            return letter


def binary_decode(cipher):
    # decodes a binary code cipher to plain text

    # list to store plain text result
    plaintext_list = []
    # loop in every letter in cipher (after converting the latter to a list with delimiter 1 space)
    for letter in cipher.split(" "):
        # decrypt this binary code letter and append it to the plaintext list
        plaintext_list.append(decrypt_letter_binary(letter))
    # convert the plain text list to a string without adding a space (joiner) between words cz the space already decrypted as a letter
    plaintext = "".join(plaintext_list)
    # remove last space using strip()
    return plaintext.strip()


# ---------------------------------------- Sound Functions ----------------------------------------


def morse_beeps(cipher):
    """
    This function plays a morse code beep sounds.
    All timings are defined as multiples of one dot length.
    A dash is three times the length of a dot.
    Each dot or dash has a short gap of silence after it (usually 1 dot length).
    Letters in a word have a slightly longer gap of silence between them (usually 3 dot lengths).
    Words have an even longer gap of silence between them (usually 7 dot lengths).
    """

    # set frequency To 800 Hertz
    frequency = 800
    # set duration of dot and dash beep sounds in ms (milliseconds)
    dot_length = 250
    dash_length = 3 * dot_length
    # set duration of silence in s (seconds) to use it in 'time.sleep()'
    dot_dash_silence = 0.25                                  # dot_length = 250 ms = 0.25 s
    letters_silence = 3 * dot_dash_silence                   # 3 * dot_length = 3 * 250 = 750 ms = 0.75 s
    words_silence = 7 * dot_dash_silence                     # 7 * dot_length = 7 * 250 = 1750 ms = 1.75 s

    # loop in every word of cipher (after converting the latter to a list with delimiter " / "), then play sounds accordingly and hold
    # silence between letters and between words according to international morse code rules
    for word in cipher.split(" / "):
        # loop in every letter of word
        for c in word:
            if c == ".":
                # play dot beep
                winsound.Beep(frequency, dot_length)
                # silence after dot beep
                time.sleep(dot_dash_silence)
            elif c == "-":
                # play dash beep
                winsound.Beep(frequency, dash_length)
                # silence after dash beep
                time.sleep(dot_dash_silence)
            elif c == " ":
                # silence between letters
                time.sleep(letters_silence)
        # silence between words
        time.sleep(words_silence)


def text_speech(text):
    # speaks the text passed as argument

    # initialize Text-to-speech engine
    engine = pyttsx3.init()
    # convert this text to speech
    engine.say(text)
    # play the speech
    engine.runAndWait()

