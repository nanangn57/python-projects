alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode(message, shift_code):
    new_message = []
    for letter in message:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            new_index = current_index + shift_code
            if new_index > (len(alphabet) - 1):
                new_index -= (len(alphabet) - 1)
            new_letter = alphabet[new_index]
            new_message.append(new_letter)
        else:
            new_message.append(letter)

    new_message_join = ''.join(new_message)
    return new_message_join


def decode(message, shift_code):
    new_message = []
    for letter in message:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            new_index = current_index - shift_code
            if new_index < 0:
                new_index -= 1
            new_letter = alphabet[new_index]
            new_message.append(new_letter)
        else:
            new_message.append(letter)

    new_message_join = ''.join(new_message)
    return new_message_join


cont = 'yes'

while cont == 'yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        new_text = encode(text, shift)
        print(f"Here is the encoded result: {new_text}")
    elif direction == 'decode':
        new_text = decode(text, shift)
        print(f"Here is the decoded result: {new_text}")
    else:
        print(f"Wrong direction, input again")

    cont = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

