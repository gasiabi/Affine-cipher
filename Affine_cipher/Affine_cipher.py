# affine cipher
import math

alphabet_small = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś',
                  't', 'u', 'w', 'y', 'z', 'ź', 'ż']
alphabet_large = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś',
                  'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']

dictionary_alphabet = {
    'A': 0, 'Ą': 1, 'B': 2, 'C': 3, 'Ć': 4, 'D': 5,
    'E': 6, 'Ę': 7, 'F': 8, 'G': 9, 'H': 10, 'I': 11,
    'J': 12, 'K': 13, 'L': 14, 'Ł': 15, 'M': 16, 'N': 17,
    'Ń': 18, 'O': 19, 'Ó': 20, 'P': 21, 'R': 22, 'S': 23,
    'Ś': 24, 'T': 25, 'U': 26, 'W': 27, 'Y': 28, 'Z': 29,
    'Ź': 30, 'Ż': 31,
    'a': 0, 'ą': 1, 'b': 2, 'c': 3, 'ć': 4, 'd': 5,
    'e': 6, 'ę': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11,
    'j': 12, 'k': 13, 'l': 14, 'ł': 15, 'm': 16, 'n': 17,
    'ń': 18, 'o': 19, 'ó': 20, 'p': 21, 'r': 22, 's': 23,
    'ś': 24, 't': 25, 'u': 26, 'w': 27, 'y': 28, 'z': 29,
    'ź': 30, 'ż': 31
}
reverse_dict_small = {0: 'a', 1: 'ą', 2: 'b', 3: 'c', 4: 'ć', 5: 'd',
                      6: 'e', 7: 'ę', 8: 'f', 9: 'g', 10: 'h', 11: 'i',
                      12: 'j', 13: 'k', 14: 'l', 15: 'ł', 16: 'm', 17: 'n',
                      18: 'ń', 19: 'o', 20: 'ó', 21: 'p', 22: 'r', 23: 's',
                      24: 'ś', 25: 't', 26: 'u', 27: 'w', 28: 'y', 29: 'z',
                      30: 'ź', 31: 'ż'}
reverse_dict_large = {0: 'A', 1: 'Ą', 2: 'B', 3: 'C',
                      4: 'Ć', 5: 'D', 6: 'E', 7: 'Ę',
                      8: 'F', 9: 'G', 10: 'H', 11: 'I',
                      12: 'J', 13: 'K', 14: 'L', 15: 'Ł',
                      16: 'M', 17: 'N', 18: 'Ń', 19: 'O',
                      20: 'Ó', 21: 'P', 22: 'R', 23: 'S',
                      24: 'Ś', 25: 'T', 26: 'U', 27: 'W',
                      28: 'Y', 29: 'Z', 30: 'Ź', 31: 'Ż'}


def generate_the_key():
    key_text = 'passwd.txt'
    with open(key_text, 'r', encoding='utf-8') as f:
        keys = f.read().split()
        result_keys = [int(key) for key in keys]

    return result_keys


# checking if the chosen keys are correct
def checking_the_key(a, alph_length):
    if (math.gcd(a, alph_length)) != 1:
        print("The a value is not correct. Please change it so that the GCD of a and the alphabet length equals to 1.")
        exit()


# encrypting the text
def encrypt_the_text(text, dictionary, reversed_dictionary_small, reversed_dictionary_large):
    keys = generate_the_key()
    a, b = keys
    checking_the_key(a, len(alphabet_large))
    encrypted_text = []

    for letter in text:
        if letter in alphabet_small:
            value = dictionary[letter]
            new_value = ((a*value)+b) % len(alphabet_small)
            new_letter = reversed_dictionary_small.get(new_value)
            encrypted_text.append(new_letter)
        elif letter in alphabet_large:
            value = dictionary[letter]
            new_value = ((a*value)+b) % len(alphabet_large)
            new_letter = reversed_dictionary_large.get(new_value)
            encrypted_text.append(new_letter)
        else:
            encrypted_text.append(letter)

    final_encrypted_text = ''.join(encrypted_text)

    return final_encrypted_text


# uploading the file and encrypting ot
def upload_the_file():
    file = 'plain.txt'
    new_file = 'substitute_proprietary.txt'

# utf-8 used to use Polish diacritical marks
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    encrypted_text = encrypt_the_text(text, dictionary_alphabet, reverse_dict_small, reverse_dict_large)

    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

    return text


if __name__ == '__main__':
    upload_the_file()




