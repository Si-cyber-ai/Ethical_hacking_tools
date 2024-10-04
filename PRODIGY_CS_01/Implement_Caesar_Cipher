print("===============Implement Caesar Cipher===============")
#Defining a function to implemnt the Caesar Cipher
def caesar_cipher(text, shift, mode='E'):
    #Empty string to store data
    result =''

    if mode =='D':
        shift=-shift
    
    #Iterating through each character     
    for x in text:
        if x.isalpha():
            ascii_offset = 65 if x.isupper() else 97
            result += chr((ord(x) - ascii_offset + shift) % 26 + ascii_offset)
        else :
            result+=x
    return result

#Main Function 
message=input("Enter the Message: ")
shift_value=int(input("Enter the Shift value: "))
action=input("Enter 'E' for encrypt or 'D' for decrypt: ").strip().upper()

# Perform the encryption or decryption based on the user's action
if action == 'E':
    encrypt_msg = caesar_cipher(message,shift_value,action)
    print("Encrypted Message: ",encrypt_msg)
elif action == 'D':
    decrypt_msg = caesar_cipher(message,shift_value,action)
    print("Decrypted Message: ",decrypt_msg)
else :
    print("Invalid action , Please choose 'E' of encrypt and 'D' for decrypt")
