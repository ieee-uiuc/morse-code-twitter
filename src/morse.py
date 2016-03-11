#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# morse-code-twitter

MORSE_ALPHABET = {'A': '.-',     'B': '-...',   'C': '-.-.',
                  'D': '-..',    'E': '.',      'F': '..-.',
                  'G': '--.',    'H': '....',   'I': '..',
                  'J': '.---',   'K': '-.-',    'L': '.-..',
                  'M': '--',     'N': '-.',     'O': '---',
                  'P': '.--.',   'Q': '--.-',   'R': '.-.',
                  'S': '...',    'T': '-',      'U': '..-',
                  'V': '...-',   'W': '.--',    'X': '-..-',
                  'Y': '-.--',   'Z': '--..',

                  '0': '-----',  '1': '.----',  '2': '..---',
                  '3': '...--',  '4': '....-',  '5': '.....',
                  '6': '-....',  '7': '--...',  '8': '---..',
                  '9': '----.',
                  ' ': '/',  # Turn spaces between words into slashes.
                  '@56ek ': '......'
                  }

INVERSE_MORSE_ALPHABET = dict((v, k) for (k, v) in MORSE_ALPHABET.items())


class MorseCodeDecodeError(ValueError):
    """ Raised when there's an error decoding Morse Code. """
    def __init__(self, message, invalid_str, *args):
        self.message = message
        self.invalid_str = invalid_str
        super().__init__(self.message, invalid_str, *args)


def decode_letter(letter):
    """ Given a letter in morse code, validate it as a proper letter, and
        return its translation.
    """
    letter_bag = set(letter)

    if not letter_bag.issubset(set('.-/ ')):
        raise MorseCodeDecodeError("Letter contains non Morse Code characters",
                                   letter)
    try:
        return INVERSE_MORSE_ALPHABET[letter]
    except KeyError:
        raise MorseCodeDecodeError("Invalid Morse Code Letter", letter)


def decode_message(message):
    """ Given a message in morse code, translate it back into text. """
    return ''.join(decode_letter(char) for char in message.split(' '))


def encode_message(message):
    """ Given a message, encode it in morse code. """
    try:
        return ''.join(MORSE_ALPHABET[char] + ' '
                       for char in message.upper()).strip()
    except KeyError:
        raise MorseCodeDecodeError(
            "Message contains ASCII without Morse code translation", message)


def main():
    """ Show off the functionality of the module. """
    message = "This is a test"
    print(message)
    morse_message = encode_message(message)
    print(morse_message)

    translated = decode_message(morse_message)
    print(translated)

    assert(translated == message.upper())


if __name__ == '__main__':
    main()
