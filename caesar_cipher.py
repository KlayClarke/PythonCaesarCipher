from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text_length = len(text)

def caesar(direction,text, shift):
    new_text=''
    for letter in text:
        if direction=='encode':
            letter_index=alphabet.index(letter)
            new_letter=alphabet[letter_index+shift]
            new_text+=new_letter
        elif direction=='decode':
            letter_index=alphabet.index(letter)
            new_letter=alphabet[letter_index-shift]
            new_text+=new_letter
    print(f'Here is the {direction} result: {new_text}')

caesar(direction,text,shift)    
