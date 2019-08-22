alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '0','1', '2', '3', '4','5', '6', '7', '8', '9', '.', ',' ,'?', ';', ':', '/', '-', '\'', '(', ')', '_', '@', '!', '&', '=', '+', '"', '$']
morse_alphabet =['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', ' ', '-----','.----', '..---', '...--', '....-','.....', '-.....', '--...', '---..', '----.', '.-.-.-', '--..--' ,'..--..', '-.-.-', '---...', '-..-.', '-....-', '.----.', '-.--.', '-.--.-', '..--.-', '.--.-.', '-.-.--', '.-...', '-...-', '.-.-.', '.-..-.', '...-..-']


def translator(sentence):
    list_sentence = list(sentence.upper())
    indexes = []
    illegal_characters = []
    count = -1
    for letters in list_sentence:
        try:
            indexes.append(alphabet.index(letters))
        except ValueError:
            if letters not in alphabet:
                count += 1
                illegal_characters.append(letters)
                #print('That cannot be converted '+ illegal_characters[count])
            
    morse_sentence = []
    for numbers in indexes:
        morse_sentence.append(morse_alphabet[numbers])

    translated = ' '.join(morse_sentence)
    print(translated)

while True:
    new_sentence = str(raw_input('what would you like to translate? '))
    translator(new_sentence)
