print( """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                                                           
           00             88                                 
           ""             88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# caesar cipher implementation
def caesar(start_text, shift, cipher_direction):
    end_text = ""
    #if we are decoding we need to change the shift to negative number
    if cipher_direction == 'decode':
            shift *= -1
    # for every letter in the phrase
    for letter in start_text:
        #if the user enters a number/symbol/space we just add it to the end result
        if letter not in alphabet:
            end_text += letter
        else:
            # find the shifted index
            shifted_index = (alphabet.index(letter) + shift) % len(alphabet)
            # add that new shifted letter to the result
            end_text += alphabet[shifted_index]
    # print cipher
    print(f"The {cipher_direction}d text is {end_text}")
   
# function that will be repeated in while loop of the app
def restart_program():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # mod 25 to prevent the user from abusing very large shift
    shift = shift % 25

    caesar(start_text=text, shift=shift, cipher_direction=direction)
#Import and print the logo from art.py when the program starts.


choice = 'yes'

while choice == 'yes':
    restart_program()
    choice = input('Would you like to do again? (yes/no) \n')
