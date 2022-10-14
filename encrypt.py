import random

vowel = 'AEIOUaeiou'
spaces = '6789' 
var = {
    'b':'k', 'k':'s', 's':'c', 'c':'l', 'l':'t', 't':'d', 'd':'m',
    'm':'v', 'v':'f', 'f':'n', 'n':'w', 'w':'g', 'g':'p', 'p':'x',
    'x':'h', 'h':'q', 'q':'y', 'y':'j', 'j':'r', 'r':'z', 'z':'b',
    '`':'&', '&':'$', '$':'>', '>':'^', '^':'#', '#':'<', '<':'%',
    '%':'@', '@':'|', '|':':', ':':'"', '"':'=', '=':'+', '+':'?',
    '?':'_', '_':'/', "/":"'", "'":"!", '!':'\\', '\\':'-', '-':'.',
    '.':'*', '*':';', ';':',', ',':'`', '(':'}', '}':'[', '[':')',
    ')':'{', '{':']', ']':'(', ' ':random.choice(spaces)
}
# Layer 1 is the replacement of all vowels in the user input
def layer_1():
    msg = input("Enter the sentence or phrase you wish to encrypt:")
    msg = msg.replace('a', '1')
    msg = msg.replace('A', '1')
    msg = msg.replace('e', '2')
    msg = msg.replace('E', '2')
    msg = msg.replace('i', '3')
    msg = msg.replace('I', '3')
    msg = msg.replace('o', '4')
    msg = msg.replace('O', '4')
    msg = msg.replace('u', '5')
    msg = msg.replace('U', '5')

    # Layer 2 will deal with choosing a character and replacing it with a vowel.
    # This layer replaces 1 character with a vowel for every 5 characters in a row.
    # The pattern for chosing a variable is as follows:
    # their     # (A)heir
    # there     # t(U)ere
    # throw     # th(I)re
    # night     # nig(O)t
    # raven     # rave(E)
    def layer_2(msg):
        i = 0
        j = 0
        final = ''
        r_var = ''
        sen = ''
        for c in msg:
            if c != ' ':
                if i == j:
                    final += random.choice(vowel)
                    r_var += c
                else:
                    final += c
                j += 1
                if j == 5:
                    j = 0
                    i += 1
                if i == 5:
                    i = 0
            else:
                final += ' ' 
        # Layer 2 also deals with replacing all other characters within the user input
        # Replacing the letters within the user input
        # Replacing the symbols and punctuations
        # Replacing the spaces 
        sen = ''.join(var.get(c, c) for c in final)
                   
        # print(f"Characters replaced by vowels : {r_var}")
        # This print statement keeps track of the vowels removed
        return sen
                        
    print(f"Encrypted Data: {layer_2(msg)}")

layer_1()