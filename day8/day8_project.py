alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_message, shift_letters):
    encrypted_text = ""
    for letter in text_message:
        if letter == " ":
            encrypted_text += " "
        else:
            letter_to_shift = alphabet.index(letter)
            shifted_letter = letter_to_shift + shift_letters
            new_letter = alphabet[shifted_letter]
            encrypted_text += new_letter

    print(f"The encoded text is : {encrypted_text}")

def decrypt(text_message, shift_letters):
    clear_text = ""
    for letter in text_message:
        if letter == " ":
            clear_text += " "
        else:
            letter_to_shift = alphabet.index(letter)
            shifted_letter = letter_to_shift - shift_letters
            new_letter = alphabet[shifted_letter]
            clear_text += new_letter

    print(f"The decoded text is : {clear_text}")

# main function to run
direction = direction.lower()
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("please enter one of the choices!")
