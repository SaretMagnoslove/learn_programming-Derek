message = input('Enter a message to code: ')
encoded_message = ''
decoded_message = ''
for letter in message:
    encoded_message += str(ord(letter)+100)
print('Encoded message is: ',encoded_message)
for num in range(0, len(encoded_message)-1 ,3):
    code = encoded_message[num] + encoded_message[num+1]+encoded_message[num+2]
    decoded_message += chr(int(code)-100)
print ('Decoded message is: ', decoded_message)


    
    