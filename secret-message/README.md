# Python Projects: Secret Message 🐍

Python Script <br>
This python code runs in such a way that it uses  uses an encryption program to send and receive secret messages with a friend <br>
Run the code.

```
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

```

## CODE EXPLANATION

The code starts with hardcoding the 26 alphabets, defining a variable that takes in a number 3 specifying how many position forward the program will find an alphabet for the encryption <br>
Then it defines another variable that takes in an empty string to hold the secret message. <br>
Next, another variable that holds the input of the user. <br>

Now is time to iterate over the `message` variable <br>

For the character in `message`, the program will find the character, hold on to the character in `position + key % 26` then goes further to  add the new character to the `new message`
