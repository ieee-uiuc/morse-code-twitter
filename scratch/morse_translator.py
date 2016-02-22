morseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}

inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())

testCode = "-- --- .-. ... . / ..-. .. -. --. . .-. ... / - ..- .-. -. / - --- / - .-- .. - - . .-. / ..-. .. -. --. . .-. ..."


# parse a morse code string
def decode_morse(code):
    decoded = ''
    words = code.split('/')
    for word in words:
        letters = word.strip().split(' ')
        for letter in letters:
            decoded += inverseMorseAlphabet[letter]
        decoded += ' '
    return decoded


# encode a message in morse code, spaces between words are represented by '/'
def encode_to_morse(message):
    encoded_message = ""
    for char in message:
        encoded_message += morseAlphabet[char.upper()] + " "

    return encoded_message

print(decode_morse(testCode))
