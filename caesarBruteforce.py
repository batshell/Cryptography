#This function will decrypt the given key
def bruteForce(message,key_start,key_end):
    #The usual symbol stack
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()[];'<>,./\\\""
    #Loop through the given key range
    for i in range(key_start, key_end+1):
        translated = ''
        #Rest is the usual code
        for j in message:
            if j in symbols:
                sympos = symbols.find(j)
                trans_pos = (sympos - i) % len(symbols)
                translated = translated + symbols[trans_pos]
            else:
                translated = translated + j
        #Print the translated data in the given range
        print("Shift by",i,": ", translated)

def main():
    message = input("Enter the cipher text to be decrypted: ")
    #Total number of symbols that we have here is 84 and 84 combinations is way too much
    #In order to limit it, the bruteforce function takes two arguments, key_start and key_end
    #The program will bruteforce the cipher in the given range of numbers only
    key_start = int(input("Enter the starting key (Range must be between 1 and 83: "))
    key_end = int(input("Enter the ending key (Range must be between 1 and 83: "))
    #Driver code:
    bruteForce(message, key_start,key_end)

if __name__ == "__main__": main()
