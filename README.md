# E-CRYPT ⚿
### Video Demo:  <https://youtu.be/Zy_DNJJAo84>
### Description:
#### This is a software for encrypting and decrypting messages. It is based on two encoding methods: "Morse Code" and "Binary Code".

## ◼ Foreword about Morse Code and Binary Code: 

### ▪ "Morse Code":

Invented by Samuel Morse in 1836, Morse Code is a method for sending and receiving text messages using short and long beeps. 
Conventionally, a short beep is called a "dot" and a long one is a "dash" (also known, respectively, as a dit and a dah). Every letter of the 
alphabet has a unique sequence of dots and dashes. 

E-CRYPT uses the International Morse Code chart which consists of only the uppercase alphabet letters from A to Z, and digits from 0 to 9.
It's not a must to use sound for this, although this is the most common way Morse Code was used. Hence, E-CRYPT provides an option for the 
user to hear the Beep sounds of the encrypted Morse Code message.

It can be done with anything that can be turned on and off; this could be a torch, raising and lowering a flag, or even just blinking the 
eyes quickly and slowly. This makes it one of the most versatile forms of telecommunication. It is often used by military armies around the 
world. 

When writing a message using this code each letter is separated with a " " (space) and each word with a " / " (slash between 2 spaces). 


### ▪ "Binary Code"

It represents text, computer processor instructions, or any other data using a two-symbol system. The two-symbol system used is often "0" and 
"1" from the binary number system. The Binary Code assigns a pattern of binary digits, also known as bits, to each character, instruction, etc. 
For example, a binary string of eight bits (which is also called a byte) can represent any of 256 possible values and can, therefore, 
represent a wide variety of different items.

In computing and telecommunications, binary codes are used for various methods of encoding data, such as character strings, into bit strings. 
Those methods may use fixed-width or variable-width strings. In a fixed-width Binary Code, each letter, digit, or other character is represented 
by a bit string of the same length; that bit string is interpreted as a binary number. There are many character sets and many character 
encodings for them.

E-CRYPT, consists of a fixed-width Binary Code, uses a wide variety of special characters, digits from 0 to 9, and all alphabet letters 
(lowercase and uppercase) from A to Z.

When writing a message using this code each letter is separated with a "space character" and each word with a "space character" because 
the actual space character has its own binary number that represents it, so eventually while decoding it will appear how to separate words. 

----------------------------------------------------------------

## ◼ Introduction:

The user can enter any text message he wants, and chooses the method he prefers in order to encrypt it. The software also provides the option of 
decryption in both of the methods, so basically he can type any cipher message he has (encoded in Morse or Binary Code only) and the software 
will decode it easily. 

The output result, whether it's an encrypted message or a decrypted cipher, will be displayed on the screen and automatically copied to the
clipboard as a bonus action for a practical use in case the user wants to paste it in a specific document.

Only the cipher in Morse Code will be decrypted to a text message where all letters in uppercase following the International Morse Code chart.

Since Morse Code is a signal language used in military and other areas, this software provides the option to listen to the encrypted 
cipher signal as Beep sounds (of 800 Hz Frequency), but this option is not applicable to Binary Code since it's not a signal language.

Another bonus option is the ability to listen to the text message spoken after being decrypted whether from Morse Code or Binary Code. 

----------------------------------------------------------------

## ◼ List of contents

### 1 - helpers.py
### 2 - functions.py
### 3 - user_interface.py
### 4 - main.py
### 5 - requirements.txt
### 6 - images folder

----------------------------------------------------------------

### 1 - helpers.py

This file contains the basic tools for E-crypt, two dictionaries and four boolean methods. 

Those two dictionaries "INTERNATIONAL_MORSE_CODE" and "BINARY_CODE" contain the letter translation for Morse Code and Binary Code 
respectively, and will come in handy when encoding messages and decoding ciphers by referring to them in order to translate every letter:

- "INTERNATIONAL_MORSE_CODE": is used for Morse Code translation, contains digits from 0 to 9, and all 26 alphabetical 
  uppercase letters from A to Z. It simply follows the Morse Code international general rule of that consists of translating only the capital 
  letters of the alphabet with the digits from 0 to 9.


- "BINARY_CODE": is used for the Binary Code translation. It basically consists of the maximum number of special characters 
  used in typing with all the alphabetical letters from A to Z (uppercase and lowercase) and the digits from 0 to 9.


There are two functions "can_encrypt_morse()" and "can_encrypt_binary" that check the validity of the text message entered by the user:

- "can_encrypt_morse(*text*)": checks whether the text message passed as argument is valid for Morse Code encryption or not. By looping 
  through every letter of the text, it checks if this letter, after converting it to uppercase (Morse Code rule), exists in the keys of the 
  "INTERNATIONAL_MORSE_CODE" dictionary. If yes, the function returns "True", otherwise it breaks the loop and returns "False" which 
  indicates that there's an invalid letter that cannot be translated to Morse Code, so the whole text message is invalid and cannot be 
  encrypted. And if the letter was a space character " " the loop will skip it and continue since it's a separator between the words of the 
  text message.


- "can_encrypt_binary(*text*)": checks whether the text message passed as argument is valid for Binary Code encryption or not. By looping 
  through every letter of the text, it checks if this letter exists in the keys of the "BINARY_CODE" dictionary. If yes, the function returns 
  "True" otherwise it breaks the loop and returns "False" which indicates that there's an invalid letter that cannot be translated to Binary 
  Code, so the whole text message  is invalid and cannot be encrypted. And if the letter was a space character " " the loop will skip it and 
  continue since it's a separator between the words of the text message.

There are two functions "is_morse_code"  and "is_binary_code" that check the validity of the cipher message entered by the user:

- "is_morse_code(*cipher*)": checks whether the cipher message passed as argument is valid for Morse Code decryption or not. It converts this 
  cipher to a list using "split()" method and selecting the delimiter of " / " following the Morse Code cipher format (" / " between words 
  and 1 space between letters ). Then it loops through every word of the list obtained, and here it loops through every letter of the word after 
  converting the latter to a list using the "split()" method also and selecting the delimiter of 1 space this time, and checks if this letter 
  exists in the values of the "INTERNATIONAL_MORSE_CODE" dictionary. If yes, the function returns "True" otherwise it breaks the loop and 
  returns "False" which indicates that there's an invalid letter in this cipher that cannot be decoded from Morse Code, so the whole cipher 
  message is invalid and cannot be decrypted.


- "is_binary_code(*cipher*)": checks whether the cipher message passed as argument is valid for Binary Code decryption or not. It converts this 
  cipher to a list using "split()" method and selecting the delimiter of 1 space following the Binary Code cipher format (1 space between words
  and 1 space between letters as well) which will lead to obtaining one big list of Binary Code letters (Bytes). Then it loops through every 
  letter of the list obtained, and checks if this letter exists in the values of the "BINARY_CODE" dictionary. If yes, the function returns 
  "True" otherwise it breaks the loop and returns "False" which indicates that there's an invalid letter in this cipher that cannot be 
  decoded from Binary Code, so the whole cipher message is invalid and cannot be decrypted.


----------------------------------------------------------------

### 2 - functions.py

This file contains the essential methods for E-crypt, that are responsible for encryption and decryption, and also 2 functions for playing 
sounds, 1 for Morse Code Beep signal and 1 for playing the decrypted text speech respectively.


- "morse_encode(*plaintext*)": encodes a text passed as argument to Morse Code cipher. It converts the plaintext argument to a list using 
  "split()" method and selecting the delimiter to 1 space. Then it starts looping through every word of the list obtained, also it loops 
  through every letter of this current word and converts it to uppercase (for Morse Code rule) and catch the related translation from the 
  Morse Code dict imported from "helpers" module to concatenate it to the "cipher_word" variable that is reset at every iteration. If the 
  letter is space " ", this means there is a sequence of spaces (where "split()" didn't catch but 1) so break the loop and don't add it to 
  "cipher_word" for a neat result output. If nothing concatenated to "cipher_word" in case of sequence of spaces (word of spaces), such word 
  would not be appended to the result cipher list created at the start of this function. Otherwise, (after finishing the word) append it to 
  the list. Finally, it converts the cipher list to a string using "join()" and adding "/ " (joiner) between words (there's 1 space before 
  slash from above concatenation) to eventually return the final result after stripping it from the last space at the end.

 
- "binary_encode(*plaintext*)": encodes a text passed as argument to Binary Code cipher. It converts the plaintext argument to a list using 
  "split()" method and selecting the delimiter to 1 space. Then it starts looping through every word of the list obtained, also it loops 
  through every letter of this current word and catch the related translation from the Binary Code dict imported from "helpers" module to 
  concatenate it to the "cipher_word" variable that is reset at every iteration. If the letter is space " ", this means there is a sequence 
  of spaces (where "split()" didn't catch but 1) so break the loop and don't add it to "cipher_word" for a neat result output. If nothing 
  concatenated to "cipher_word" in case of sequence of spaces (word of spaces), such word would not be appended to the result cipher list 
  created at the start of this function. Otherwise, (after finishing the word) append it to the list after concatenating cipher_word with the 
  binary code of 1 space (to have a neat result) following each word of the plaintext. Finally, it converts the cipher list to a string using 
  "join()" and adding 1 space (joiner) between words (there's 1 space between letters of Binary Code and 1 space between words) to eventually 
  return the final result.


- "decrypt_letter_morse(*code*)": decrypts one letter in Morse Code passed as argument to original alphanumeric letter. It loops through 
  every (key, value) of Morse Code dict imported from "helpers" module and returns the key (letter) once value (code) is found.
  
  
- "morse_decode(*cipher*)": decodes a Morse Code cipher passed as argument to plain text. It converts the plaintext argument to a list using 
  "split()" method and selecting the delimiter to " / ". Then it starts looping through every word of the list obtained, also it loops 
  through every letter of this current word (after converting the latter to a list with delimiter of 1 space) and decrypts the Morse Code 
  letter using "decrypt_letter_morse()" method created above. After finishing the plaintext word (that is reset at every iteration) it appends 
  it to the plaintext list created at the start of this function. Finally, it converts the plain text list to a string using "join()" method 
  and adding 1 space (joiner) between words, and eventually it returns the result all in uppercase as per the international Morse Code chart.

 
- "decrypt_letter_binary(*code*)": decrypts one letter in Binary Code passed as argument to original letter. It loops through every
  (key, value) of Binary Code dict imported from "helpers" module and returns the key (letter) once value (code) is found.


- "binary_decode(*cipher*)": decodes a Binary Code cipher passed as argument to plain text. It converts the plaintext argument to a list using 
  "split()" method and selecting the delimiter to 1 space. Then it starts looping through every letter of the list obtained and decrypts 
  the Binary Code letter using "decrypt_letter_binary()" method created above then appends it to the plaintext list created at the start of 
  this function. Finally, it converts the plain text list to a string using "join()" method without adding a space (joiner) between words cz 
  the space already decrypted as a letter, and eventually it returns the result without the last space for a neat final result using "strip()"
  method.


- "morse_beeps(*cipher*)": This function plays a morse code beep sounds by using the imported module "winsound" in order to let out the Beep 
  sounds 
  using the "Beep()" method. All timings are defined as multiples of one dot length. A dash is three times the length of a dot. Each dot or 
  dash has a short gap of silence after it (usually 1 dot length). Letters in a word have a slightly longer gap of silence between them 
  (usually 3 dot lengths). Words have an even longer gap of silence between them (usually 7 dot lengths).

  It takes cipher message as an argument, then it declares few variables to set the frequency To 800 Hertz, to set the duration of dot beep 
  sound (250 ms) and dash beep sound (3x250=750) in ms (milliseconds), and to set the duration of silence in s (seconds) to use it in 
  "time.sleep()" method (silence after a dot/dash is 0.25 s, after a letter is 3x0.25=0.75 s, and silence after word is 7x0.25=1.75 s).
  
  It converts the cipher to a list using "split()" method and selecting the delimiter of " / ". Then it starts looping through every word of 
  the list obtained in order to play sounds accordingly and hold silence between letters and between words as per international morse 
  code rules. It loops also through every letter of the current word and checks it in order to play the related beep sound for the related 
  duration. It also adds silence duration using "time.sleep()" method without any beep sounds, and eventually after every word it also adds a 
  moment of silence.


- "text_speech(*text*)": speaks the text passed as argument. it initializes the text-to-speech engine from the "pyttsx3" module, converts the 
  text (argument) to a speech using ".say()" method and finally plays the sound by calling the method ".runAndWait()".
  This function will be called out whenever the user presses the "Play 🔊" button.

----------------------------------------------------------------


### 3 - user_interface.py

This file contains the graphical user interface methods for E-CRYPT. It declares "EcryptInterface()" class that inherits all the "Tk()" class 
properties and methods from "tkinter" module.
It initializes a tkinter root window and declares all the widgets required with their designs, styles, and layouts. It also keeps listening 
to the events by using the "mainloop()" method that acts as an event listener.   


- "create_widgets(self)": creates the widgets and configurate the created ones (declared in "init()") to be displayed. It sets the required 
  layout using "grid()" and creates canvas object then customize it with the above declared widgets. It is in this function where "mainloop()"
  method is called out to Keep listening for events


- "homepage(self)": creates the home page for the application, and puts the layout of the widgets. It adds texts with colors and fonts styles to 
  canvas and configure the layouts more properly in order to get a well organised homepage. It configures the 2 new buttons with two commands 
  (functionalities): 1 with the command "self.morse_code()" entitled as "Morse Code" and the other with the command "self.binary_code()" 
  entitled as "Binary Code".


- "input_widgets(self)": creates the widget for user input and adjust the earlier widgets accordingly. It updates the titles, deletes the logo 
  widget in this page, adjusts the 2 buttons to become 1 entitled as "Encrypt" with the command "self.encrypt()" and the other entitled as 
  "Decrypt" with the command "self.decrypt()". Finally it configures (make it appear) the text input that is declared in "init()" using "Text()".
  It is also responsible for the layout and graphical design of this page.


- "morse_code(self)": sets the method to "morse" and calls "input_widgets()" for display whenever the user presses "Morse Code" button in the 
  homepage. It adjusts the text displayed on canvas also to make it read "- Morse Code -".

  
- "binary_code(self)": sets the method to "binary" and calls "input_widgets()" for display whenever the user presses "Binary Code" button in the 
  homepage. It adjusts the text displayed on canvas also to make it read "- Binary Code -".


- "encrypt(self)": encrypts the text message typed by the user following the specific encryption method. It catches user text input using 
  "get()" and strip it from extra spaces "strip()". If text input is empty the function will raise a message error using ".showinfo()" from 
  "messagebox" class of "tkinter" module, same thing when checking if method is "morse" and there's invalid characters for Morse Code 
  encryption cz "can_encrypt_morse()" method from "functions" module with "user_input" passed as an argument returns False. Furthermore, 
  if method is "binary" and there's invalid characters for Binary Code encryption cz "can_encrypt_binary()" method from "functions" module with 
  "user_input" passed as an argument returns False, the function will raise a message error using ".showinfo()" from "messagebox" class of 
  "tkinter" module.
  When no errors raised, the text message can be encrypted, so the function sets the mode to "encrypt" and saves the user input in "self.
  message_input" then calls "self.display_result()" method.
            

- "decrypt(self)": decrypts the cipher message typed by the user following the specific decryption method. It catches user text input using 
  "get()" and strip it from extra spaces "strip()". If text input is empty the function will raise a message error using ".showinfo()" from 
  "messagebox" class of "tkinter" module, same thing when checking if method is "morse" and there's invalid characters for Morse Code 
  cipher cz "is_morse_code()" method from "functions" module with "user_input" passed as an argument returns False. Furthermore, 
  if method is "binary" and there's invalid characters for Binary Code cipher cz "is_binary_code()" method from "functions" module with 
  "user_input" passed as an argument returns False, the function will raise a message error using ".showinfo()" from "messagebox" class of 
  "tkinter" module.
  When no errors raised, the cipher message can be decrypted, so the function sets the mode to "decrypt" and saves the user input in "self.
  message_input" then calls "self.display_result()" method.


- "display_result(self)": displays results according to method ("morse" or "binary") and mode ("encrypt" or "decrypt"). It adjusts the 2 
  buttons to become 1 entitled as "Play 🔊" with the command "self.play_sound()" and the other entitled as "Home" with the command
  "self.return_home()", it also configures their layouts and designs.
  As per mode ("encrypt" or "decrypt") it sets the title and saves it, also as per method ("binary" or "morse") encodes message (using 
  "binary_encode()" or "morse_encode()") or decodes cipher (using "binary_decode()" or "morse_decode()") with passing "self.message_input" 
  saved above accordingly, and saves the result in "self.message_output".
  Now it sets the new saved title using "canvas.itemconfig()" and copies the output result to the clipboard for practical action using 
  "pyperclip.copy()" (imported "pyperclip" module) and finally replaces the value of text input with the result output (using "delete()" and 
  "insert()" respectively), then it disables this text input to prevent the user from editing it, now the text input acts as a display only 
  for the output result whether encoded text message or decoded cipher message.


- "play_sound(self)": plays Beep sounds for Morse Code. It checks if method is "encrypt" to play Beep sounds for Morse Code only cz if its 
  binary code there's no playable sound for that then it raises a message error using ".showinfo()" from "messagebox" class of "tkinter" module.
  It plays beep sound for morse code using "morse_beeps()" imported from "helpers" and by passing the encrypted cipher saved in 
  "self.message_output". Now if method is "decrypt", it only plays the text speech using "text_speech()" imported from "helpers" and by passing 
  the decrypted text message saved in "self.message_output" whenever the user presses the sound button.


- "destroy_widgets(self)": destroys the widgets. It deletes the title widgets (canvas text creations: "self.greeting" and "self.choice") 
  using "canvas.delete()" then destroys the text input widget using ".destroy()" only to recreate it for later use.


- "return_home(self)": returns user to home page. It destroys display widgets using ".destroy_widgets()" method and calls out the ".homepage()"
  method to recreate everything (widgets and layouts) from scratch once again for later use.


----------------------------------------------------------------

### 4 - main.py

This file is the main module of the whole E-CRYPT project. It basically imports the "EcryptInterface" class from "user_interface" module and 
define "launch_app()" function which will act as the main function.
After checking if it's the main module using the conditional "if __name__ == "__main__"", it simply calls out the launching method 
"launch_app()" where a variable "e_crypt" is declared as "EcryptInterface()" class that initializes the whole graphical interface and keeps 
listening to events from the user (as per the tkinter "mainloop()" method initialized in the class).

----------------------------------------------------------------

### 5 - requirements.txt

This file lists all the dependencies for this E-CRYPT Python project. It includes all types of the standard packages and libraries that are 
used. It is a great way to keep track of the required Python modules.
This file was created for anyone who wants to try this software, it saves them the hassle of having to track down and install all of the 
required modules manually. 

It consists of 3 major modules:

- "Pillow 9.3.0": This library provides extensive file format support, an efficient internal representation, and fairly powerful image 
  processing capabilities. The core image library is designed for fast access to data stored in a few basic pixel formats. It should provide a 
  solid foundation for a general image processing tool.
  It is used in this project to fix the tkinter error of not recognizing data in image file on canvas inside the graphical interface.
 
- "pyperclip 1.8.2": This library is a cross-platform Python module for copy and paste clipboard functions.
  It is used in this project to be able to automatically copy the output result (encrypted text or decrypted cipher) to the clipboard for 
  a practical use, so the user can paste it directly anywhere he wants. 
 
- "pyttsx3 2.90": This library is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline.
  It is used in this project to be able to listen or play the sound of the speech of the text message decrypted whether from Morse 
  Code or Binary Code.


----------------------------------------------------------------

### 6 - images folder

This "images" directory contains the images files used in this project. In this case, this project uses only 1 image file in order to stay 
consistent and simple. this image file acts as a background for the software and is placed on the tkinter canvas object of the graphical 
interface class.

The following is the background image used in E-CRYPT:

![](images/e_crypt_bg.jpg)


