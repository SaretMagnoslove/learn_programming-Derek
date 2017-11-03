cipher = input('Enter code to cipher: ')
key = int(input('Enter shift: '))
message = ''
d_message = ''
for letter in cipher:
    if letter.isalpha():
        letter = ord(letter)+key
        while (letter>90 and letter<97) or letter>122:
            letter -= 26
        letter = chr(letter)
        message += (letter)
    else: message += (letter)
print ('Chipherd message is: ',message)
for letter in message:
    if letter.isalpha():
        letter = ord(letter)-key
        while (letter>90 and letter<97) or letter<65:
            letter += 26
        letter = chr(letter)
        d_message += (letter)
    else: d_message += (letter)
print ('Deciphered message is: ',d_message)
    
