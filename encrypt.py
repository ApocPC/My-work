import random

vowels = "AEIOUaeiou"
spaces = "6789"
encrypt_dict = {
    "b": "k",
    "k": "s",
    "s": "c",
    "c": "l",
    "l": "t",
    "t": "d",
    "d": "m",
    "m": "v",
    "v": "f",
    "f": "n",
    "n": "w",
    "w": "g",
    "g": "p",
    "p": "x",
    "x": "h",
    "h": "q",
    "q": "y",
    "y": "j",
    "j": "r",
    "r": "z",
    "z": "b",
    "`": "&",
    "&": "$",
    "$": ">",
    ">": "^",
    "^": "#",
    "#": "<",
    "<": "%",
    "%": "@",
    "@": "|",
    "|": ":",
    ":": '"',
    '"': "=",
    "=": "+",
    "+": "?",
    "?": "_",
    "_": "/",
    "/": "'",
    "'": "!",
    "!": "\\",
    "\\": "-",
    "-": ".",
    ".": "*",
    "*": ";",
    ";": ",",
    ",": "`",
    "(": "}",
    "}": "[",
    "[": ")",
    ")": "{",
    "{": "]",
    "]": "(",
    " ": random.choice(spaces),
}
vowel_dict = {
    "a": "1",
    "e": "2",
    "i": "3",
    "o": "4",
    "u": "5",
    "A": "1",
    "E": "2",
    "I": "3",
    "O": "4",
    "U": "5",
}
# Step 1 is the replacement of all vowels in the user input
def encrypt():
    user_input = input("Enter the sentence or phrase you wish to encrypt:")
    msg = [vowel_dict.get(x, x) for x in user_input]
    encrypted_message = step_2(msg)
    print(f"Encrypted Data: {encrypted_message}")


def step_2(msg):
    # Layer 2 will deal with choosing a character and replacing it with a vowel.
    # This layer replaces 1 character with a vowel for every 5 characters in a row.
    # The pattern for chosing a variable is as follows:
    # their  =>  # (A)heir
    # there  =>  # t(U)ere
    # throw  =>  # th(I)re
    # mercy  =>  # mer(O)y
    # raven  =>  # rave(E)
    text_file = ""  # Character Text File
    vowel_sen = ""  # New vowel string
    encrypted_message = ""
    offset = 0
    cycle = 0
    for character in msg:
        if character != " ":
            if offset == cycle:
                vowel_sen += random.choice(vowels)
                text_file += character
            else:
                vowel_sen += character
            cycle += 1
            if cycle == 5:
                cycle = 0
                offset += 1
            if offset == 5:
                offset = 0
        else:
            vowel_sen += " "
    # Layer 2 also deals with replacing all other characters within the user input
    # Replacing the letters within the user input
    # Replacing the symbols and punctuations
    # Replacing the spaces
    encrypted_message = "".join(encrypt_dict.get(c, c) for c in vowel_sen)
    # Here a text file will hold the replaced characters
    char_txt = open("char.txt", "w")
    char_txt.writelines(text_file)
    # This print statement keeps track of the characters removed
    return encrypted_message
encrypt()