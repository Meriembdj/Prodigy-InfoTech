def caesar_cipher(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans
def main():
    while True:
        print("Caesar Cipher Encryption and Decryption")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted = caesar_cipher(message, -shift)
            print("Decrypted message:", decrypted)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()