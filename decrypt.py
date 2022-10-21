import random

decrypt_dict = {
    "k": "b",
    "s": "k",
    "c": "s",
    "l": "c",
    "t": "l",
    "d": "t",
    "m": "d",
    "v": "m",
    "f": "v",
    "n": "f",
    "w": "n",
    "g": "w",
    "p": "g",
    "x": "p",
    "h": "x",
    "q": "h",
    "y": "q",
    "j": "y",
    "r": "j",
    "z": "r",
    "b": "z",
    "&": "`",
    "$": "&",
    ">": "$",
    "^": ">",
    "#": "^",
    "<": "#",
    "%": "<",
    "@": "%",
    "|": "@",
    ":": "|",
    '"': ":",
    "=": '"',
    "+": "=",
    "?": "+",
    "_": "?",
    "/": "_",
    "'": "/",
    "!": "'",
    "\\": "!",
    "-": "\\",
    ".": "-",
    "*": ".",
    ";": "*",
    ",": ";",
    "`": ",",
    "}": "(",
    "[": "}",
    ")": "[",
    "{": ")",
    "]": "{",
    "(": "]",
}
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
}
vowel_dict = {
    "1": "a",
    "2": "e",
    "3": "i",
    "4": "o",
    "5": "u",
    "1": "A",
    "2": "E",
    "3": "I",
    "4": "O",
    "5": "U",
}
space_dict = {"6": " ", "7": " ", "8": " ", "9": " "}

# Here we open the text file containing the removed characters from the encrypting part
with open("char.txt", "r") as char_txt:
    text_file = str(char_txt.read())
    text = [vowel_dict.get(index, index).lower() for index in text_file]
    text = [encrypt_dict.get(k, k) for k in text]


def decrypt():
    # First we will place back all the vowels removed
    # As well as placing the spaces back in the user input
    user_input = input("Enter the sentence or phrase you wish to decrypt:")
    user_input_2 = (vowel_dict.get(x, x).lower() for x in user_input)
    msg = (space_dict.get(n, n) for n in user_input_2)
    decrypted_sentence = step_2(msg)
    # Layer 2 will focus on replacing the original characters
    print(f"Decrypted data: {decrypted_sentence}")


def step_2(msg):
    offset = 0
    cycle = 0
    final = ""
    decrypted_sentence = ""
    text_index = 0
    for character in msg:
        if character != " ":
            if offset == cycle:
                # Here we will replace the random vowels chosen with the original characters
                # that were provided by the user's input. The text file contains the
                # characters removed and the order in which they are to be placed back in
                final += text[text_index]
                text_index += 1
            else:
                final += character
            cycle += 1
            if cycle == 5:
                cycle = 0
                offset += 1
            if offset == 5:
                offset = 0
        else:
            final += " "
    # This will match the keys with their value pairs
    decrypted_sentence = "".join(decrypt_dict.get(c, c) for c in final)
    return decrypted_sentence

decrypt()