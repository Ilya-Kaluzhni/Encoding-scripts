# Atbash Cipher
en_alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
atbash_en_alphabet = en_alphabet[::-1]

try:
    word = "".join(word.lower() for word in input() if word.isalpha())
    operation = int(input('1 - Encode ; 2 - Decode'))
    result = ''
    
    if operation == 1:
        for i in word:
            result += atbash_en_alphabet[word.index(i)] 
        print(f'Encoded message: {result}')
    
    if operation == 2:
        for i in word:
            result += en_alphabet[word.index(i)]
        print(f'Decoded message: {result}')

except ValueError:
    print(f'An incorrect value was entered - "{operation}". Restart the program')
