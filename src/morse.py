#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
                  '9': '----.'
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

    if letter_bag != set('.-'):
        raise MorseCodeDecodeError("Letter contains non Morse Code characters",
                                   letter)
    try:
        return INVERSE_MORSE_ALPHABET[letter]
    except KeyError:
        raise MorseCodeDecodeError("Invalid Morse Code Letter", letter)
