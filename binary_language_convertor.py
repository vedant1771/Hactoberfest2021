def to_binary(string):
    letter_list, binary_letter_list = [], []
    # first loop takes each letter in the string and adds it to letter_list
    for i in string:
        letter_list.append(ord(i))

    # second loop takes each letter from letter_list, converts it to binary, then adds it to binary letter list
    for i in letter_list:
        binary_letter_list.append(int(bin(i)[2:]))

    # therefore, a list of binary values, each value for one character of the string is returned to the caller
    return binary_letter_list


string = input("Please enter the required string\n")
list_of_binary = to_binary(string)

# the binary values of all the characters and joined together, separated by a space
binary_sentence = ' '.join(str(i) for i in list_of_binary)

print(f"The above string in binary form is:\n{binary_sentence}")
