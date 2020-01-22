def main():
    key = int(input("Enter key (number) to be shifted to (1-83): "))
    message = input("Enter the plain/cipher text to be encrypted/decrypted: ")
    mode = input("Enter 'e' for encryption and 'd' for decryption: ")
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()[];'<>,./\\\""
    translated = ''
    for i in message:
        if i in symbols:
            sympos = symbols.find(i)
            #Trial 1:
            if mode == 'e':
                trans_pos = (sympos+key) % len(symbols)
            if mode == 'd':
                trans_pos = (sympos-key) % len(symbols)
            translated = translated + symbols[trans_pos]
        else:
            translated = translated + i
    print(translated)
if __name__ == "__main__": main()
