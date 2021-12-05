from art import logo


def caesar(cipher_text, shift, direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if direction == 'decode':
        shift *= -1

    new_text = ''
    for i in cipher_text:
        if i in alphabet:
            index = (alphabet.index(i) + shift) % len(alphabet)
            new_text += alphabet[index]
        else:
            new_text += i
    print(f"The {direction}d text is: {new_text}")


print(logo)

go_again = 'yes'

while go_again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    caesar(text, shift, direction)
    go_again = input("Type 'yes' if you want to go again:\n").lower()

print('Bye!')