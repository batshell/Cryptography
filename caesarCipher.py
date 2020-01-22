def main():
    key = int(input("Enter key (number) to be shifted to (1-83): "))
    message = input("Enter the plain/cipher text to be encrypted/decrypted: ")
    mode = input("Enter 'e' for encryption and 'd' for decryption: ")
    #Let's call this our symbol stack:
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()[];'<>,./\\\""
    #Will store the plain/cipher text, based on the mode
    translated = ''
    #Go through all the symbols in the given plain text
    for i in message:
        #If the current symbol is in the symbol stack
        if i in symbols:
            #Find it's position in the symbol stack
            sympos = symbols.find(i)
            #If the mode is e i.e. encryption
            if mode == 'e':
                #Add the key to be shifted by, to the position
                #The modulus operator ensures that the translated position doesn't falls out of the stack
                trans_pos = (sympos+key) % len(symbols)
            #If the mode is d i.e. decryption
            if mode == 'd':
                # Subtract the key to be shifted by, from the position
                # The modulus operator ensures that the translated position doesn't falls out of the stack
                trans_pos = (sympos-key) % len(symbols)
            #Append the symbol on to the translated variable
            translated = translated + symbols[trans_pos]
        else:
            translated = translated + i
    print(translated)
if __name__ == "__main__": main()
