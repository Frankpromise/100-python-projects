alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
new_message = ''

message = input("please enter the message you wish to send: ")

for character in message:
    position = alphabet.find(character)
    new_position =  (position + key) % 26
    new_character = alphabet[new_position]
    new_message+= new_character

print(new_message)