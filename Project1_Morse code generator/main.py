from morse import Morse

if __name__ == '__main__':

    morse_code = Morse()

    while True:
        morse_code.input_text = input("Input your message here:\n")
        type_encode = input("Do you want to encode or decode your message (encode/ decode): ")

        if type_encode == 'encode':
            morse_code.encode()
        elif type_encode == 'decode':
            morse_code.decode()
        else:
            print("Your input is not correct. Please try again.")

        cont = input("Do you want to continue (y/n): ")
        if cont == 'y':
            continue
        else:
            break