import re

class Morse:

    def __init__(self):
        self.morse_code = [
        '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
        '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '..--.-',
        '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.'
        ]

        self.alphabet_and_numbers = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', ' ',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ]

        self.morse_dict = dict(zip(self.alphabet_and_numbers, self.morse_code))
        self.alpha_dict = dict(zip(self.morse_code, self.alphabet_and_numbers))
        self.input_text = ''

    @property
    def clean_input(self):
        return (re.sub(r'[^a-zA-Z 0-9]', '', self.input_text)).lower()

    def encode(self):
        encoded_list = []
        for word in self.clean_input:
            encoded_list.append(self.morse_dict[word])
        encoded_text = ' '.join(encoded_list)
        print(f'Here is your encoded message: {encoded_text}')

    def decode(self):
        decoded_list = []
        for word in self.input_text.split():
            decoded_list.append(self.alpha_dict[word])
        decoded_text = ''.join(decoded_list)
        print(f'Here is your decoded message: {decoded_text}')