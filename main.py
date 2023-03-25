print("Welcome to the Text to Morse code generator!")



morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': ' / '}

def to_morse_code(text):
    morse_code = ''
    for char in text.upper():
        morse_code += morse_code_dict[char] + ' '
    return morse_code

input_text = input("Enter the text to convert to Morse code: ")
print(to_morse_code(input_text))
