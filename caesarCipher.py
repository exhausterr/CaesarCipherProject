FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE +1 

def caesar_shift(message, shift):


    # result plcaeholder 
    result = ''

    #go through each letter of the message 

    for char in message:
        if char.isalpha():

            char_code = ord(char) #char to ascii code 
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE


            new_char = chr(new_char_code)
            result += new_char        
        else:
            result += char
    return(result)

# This part only runs if you run caesarCipher.py directly
if __name__ == "__main__":
    user_message = input("text to encrypt: ")
    user_shift_key = int(input("enter shift key (int): "))
    encrypted = caesar_shift(user_message, user_shift_key)
    print("Encrypted:", encrypted)

