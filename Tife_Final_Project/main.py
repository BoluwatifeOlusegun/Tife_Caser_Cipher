#Modules
import time #Importing the time module
import sys  #Importing the system module
from logo import art
print(art)


# Defining a variable alphabet as a string containing all letters.
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# =========================================GREETINGS =========================================
from greeting import greeting_audio


if __name__ == "__main__":
    # Get the user's name as input
    user = input("Enter your name: ")
    
    # Define the greeting message with the user's name
    greeting_message = f"Hello {user}, welcome to Caesar Cipher"
    
    # Calling the function to play the greeting audio
    greeting_audio(greeting_message)
# ============================================================================================


# ========================================= MENU =============================================
# Importing the functions and variables from menu.py
from menu import show_menu
from menu import run
from menu import links
from menu import faq
from menu import module


#Import from menu
if __name__ == "__main__":
    show_menu()
# ===========================================================================================


# =========================================LOADING ANIMATION WITHIN CODE ====================
#Module to load animation within the code
import animation
# ===========================================================================================


# ========================================= CAESER USER INPUT ===============================

# Prompting users to type encode/decode for input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# Get user input for the text to be encrypted/decrypted and convert it to lowercase.
text = input("Type your message:\n").lower()

# Get user input for the shift amount.
shift = int(input("Type the shift number:\n"))
# ============================================================================================

# ========================================= ENCRYPT/DECRYPT ==================================
# Defining a function to perform Caesar cipher encryption/decryption.
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    
    # Checking if the user chose 'decode' and adjust the shift amount.
    if cipher_direction == 'decode':
        shift_amount *= -1
        
    # Iterate through each character in the input text.
    for letter in start_text:
        if letter in alphabet:
            # If the character is in the alphabet, find its position.
            position = alphabet.index(letter)
            
            # Calculate the new position after applying the shift and use modulo to wrap around.
            new_position = (position + shift_amount) % 26
            
            # Append the corresponding letter from the alphabet to the result.
            end_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet (e.g., space or punctuation), leave it unchanged.
            end_text += letter
    
    # Print the encrypted/decrypted text.
    print(f"The {cipher_direction}d text is {end_text}")

# Calling the caesar function with user-provided inputs.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
