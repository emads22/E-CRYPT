
from tkinter import *
from tkinter import messagebox              # to raise errors as message boxes
from PIL import ImageTk, Image              # to fix tkinter error of not recognizing data in image file on canvas
import pyperclip                            # to copy result (text or cipher) on clipboard for practical use
from helpers import can_encrypt_morse, can_encrypt_binary, is_morse_code, is_binary_code
from functions import morse_encode, morse_decode, binary_encode, binary_decode, morse_beeps, text_speech


BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#A4BE7B"
GREETING_FONT = ('Courier', 30, 'bold')
CHOICE_FONT = ('Courier', 25, 'bold')
BUTTON_FONT = ('Courier', 23, 'bold')
SOUND_BTN_FONT = ('Courier', 25, 'bold')


class EcryptInterface(Tk):
    # Inheriting Tk() class and all its properties, and initializing the application interface
    def __init__(self):
        super().__init__()
        self.message_input = ""
        self.message_output = ""
        self.method = ""
        self.mode = ""
        # Root Window
        self.title("E-crypt")
        self.config(bg=BACKGROUND_COLOR)
        # Canvas
        self.canvas = Canvas()
        self.greeting = self.canvas.create_text(0, 0, text="")
        self.choice = self.canvas.create_text(0, 0, text="")
        self.logo = self.canvas.create_text(0, 0, text="")
        self.mode_index = self.canvas.create_text(0, 0, text="")
        # Buttons
        self.button_A = Button()
        self.button_B = Button()
        self.home_button = Button()
        self.sound_button = Button()
        self.text_input = Text()

        self.create_widgets()


    def create_widgets(self):
        # create the widgets and configurate the created ones to be displayed

        self.canvas.config(width=670, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
        crypt_img = ImageTk.PhotoImage(Image.open("images/e_crypt_bg.jpg"))
        self.canvas_bg_img = self.canvas.create_image(335, 200, image=crypt_img)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.homepage()
        # Keep listening for events
        self.mainloop()


    def homepage(self):
        # creates the home page for the application, and put the layout of the widgets

        self.greeting = self.canvas.create_text(335, 70, text="Welcome to E-CRYPT", font=GREETING_FONT, fill=FONT_COLOR)
        self.logo = self.canvas.create_text(335, 205, text="⚿", font=('Courier', 60, 'bold'), fill=FONT_COLOR)
        self.choice = self.canvas.create_text(335, 330, text="Select Encryption Method", font=CHOICE_FONT, fill=FONT_COLOR)
        # Button_A is for morse code functionality in this page
        self.button_A.config(text="Morse Code", bg=BACKGROUND_COLOR, font=BUTTON_FONT, fg=FONT_COLOR, highlightthickness=0,
                             command=self.morse_code)
        self.button_A.grid(row=1, column=0, pady=20)
        # Button_B is for binary code functionality in this page
        self.button_B.config(text="Binary Code", bg=BACKGROUND_COLOR, font=BUTTON_FONT, fg=FONT_COLOR, highlightthickness=0,
                             command=self.binary_code)
        self.button_B.grid(row=1, column=1, pady=20)


    def input_widgets(self):
        # creates the widget for user input and adjust the earlier widgets accordingly

        self.canvas.itemconfig(self.greeting, text="Enter Message Below")
        # delete the logo in this page
        self.canvas.delete(self.logo)
        # Button_A is for encryption functionality in this page
        self.button_A.config(text="Encrypt", command=self.encrypt)
        # Button_B is for decryption functionality in this page
        self.button_B.config(text="Decrypt", command=self.decrypt)
        # Text input
        self.text_input.config(width=35, height=5, font=('Courier', 18))
        self.text_input.focus()
        self.text_input.grid(row=0, column=0, columnspan=2)


    def morse_code(self):
        # sets the method to "morse" and calls input_widgets() for display

        self.method = "morse"
        self.input_widgets()
        self.canvas.itemconfig(self.choice, text="- Morse Code -")


    def binary_code(self):
        # sets the method to "binary" and calls input_widgets() for display

        self.method = "binary"
        self.input_widgets()
        self.canvas.itemconfig(self.choice, text="- Binary Code -")


    def encrypt(self):
        # encrypt the user message following the specific encryption method

        # catch user text input and strip it from extra spaces
        user_input = self.text_input.get("1.0", END).strip()
        # show error if empty field
        if len(user_input) == 0:
            messagebox.showinfo(title="Error", message="Empty Field.")
        # show error if invalid characters for morse code encryption
        elif self.method == "morse" and not can_encrypt_morse(user_input):
            messagebox.showinfo(title="Error", message="Invalid characters for Morse Code Encryption.\n\n"
                                                       "(No special characters)")
        # show error if invalid characters for binary code encryption
        elif self.method == "binary" and not can_encrypt_binary(user_input):
            messagebox.showinfo(title="Error", message='Invalid characters for Binary Code Encryption')
        # no errors, message can be encrypted. set the mode to 'encrypt' and save the user input then display results
        else:
            self.mode = "encrypt"
            self.message_input = user_input
            self.display_result()

    def decrypt(self):
        # decrypt the user cipher following the specific decryption method

        user_input = self.text_input.get("1.0", END).strip()
        # show error if empty field
        if len(user_input) == 0:
            messagebox.showinfo(title="Error", message="Empty Field.")
        # show error if invalid characters of morse code cipher
        elif self.method == "morse" and not is_morse_code(user_input):
                messagebox.showinfo(title="Error", message='Invalid characters (or extra spaces) in Morse Code Cipher.')
        # show error if invalid characters of binary code cipher
        elif self.method == "binary" and not is_binary_code(user_input):
                messagebox.showinfo(title="Error", message='Invalid characters (or extra spaces) in Binary Code Cipher.')
        # no errors, cipher can be decrypted. set the mode to 'decrypt' and save the user input then display results
        else:
            self.mode = "decrypt"
            self.message_input = user_input
            self.display_result()


    def display_result(self):
        # display results according to method (morse or binary) and mode (encrypt or decrypt)

        # Button_A is for 'play sound' functionality in this page
        self.button_A.config(text="Play 🔊", bg=BACKGROUND_COLOR, font=BUTTON_FONT, fg=FONT_COLOR, highlightthickness=0,
                             command=self.play_sound)
        # Button_B is for 'return home' functionality in this page
        self.button_B.config(text=" Home ", bg=BACKGROUND_COLOR, font=BUTTON_FONT, fg=FONT_COLOR, highlightthickness=0,
                             command=self.return_home)
        # as per mode (encrypt or decrypt) choose the title and save it
        if self.mode == "encrypt":
            result_title = "Your Encoded Cipher"
            # as per method (binary or morse) encode message and save the result
            if self.method == "morse":
                self.message_output = morse_encode(self.message_input)
            else:   # self.method == "binary"
                self.message_output = binary_encode(self.message_input)
        else:   # self.mode == "decrypt":
            result_title = "Your Decoded Message"
            # as per method (binary or morse) decode cipher and save the result
            if self.method == "morse":
                self.message_output = morse_decode(self.message_input)
            else:   # self.method == "binary"
                self.message_output = binary_decode(self.message_input)

        # set the new saved title
        self.canvas.itemconfig(self.greeting, text=result_title)
        # copy the output to the clipboard for practical use
        pyperclip.copy(self.message_output)
        # replace the value of text input with the result output, and disable it to not edit it by user
        self.text_input.delete(1.0, END)
        self.text_input.config(font=('Courier', 18, 'bold'))
        self.text_input.insert(1.0, self.message_output)
        self.text_input.config(state='disabled')


    def play_sound(self):
        # play beep sounds for morse code

        # check if method is 'encrypt' to play beep sounds for morse code only
        if self.mode == "encrypt":
            # check if its binary code cz theres no playable sound for that
            if self.method == "binary":
                messagebox.showinfo(title="Error", message='No Playable Sound for Binary Code.')
            # play beep sound for morse code
            else:   # self.method == "morse"
                morse_beeps(self.message_output)
        # if method is 'decrypt' to play text speech if user wants
        elif self.mode == "decrypt":
            text_speech(self.message_output)


    def destroy_widgets(self):
        # destroy the widgets

        # delete title widgets
        self.canvas.delete(self.greeting)
        self.canvas.delete(self.choice)
        # destroy text input widget
        self.text_input.destroy()
        # recreate it for later use
        self.text_input = Text()


    def return_home(self):
        # return to home page

        # destroy display widgets
        self.destroy_widgets()
        # call back the home page to recreate everything from scratch once again for later use
        self.homepage()
