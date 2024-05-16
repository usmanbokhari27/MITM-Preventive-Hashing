import os
from custom_hash import custom_checksum, pad_message, custom_hash  # Importing our custom hash function

def modify_message(message, _message):
    # Modify the message content here
    modified_message = _message
    return modified_message

def main():
    input_choice = input("Do you want to provide a message (M) or a text file (F) to receive? ").upper()

    if input_choice == 'M':
        received_message = input("Enter the received message: ").encode()  # Encode string to bytes
    elif input_choice == 'F':
        file_path = input("Enter the path to the received text file: ")
        try:
            with open(file_path, 'rb') as file:
                received_message = file.read()
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid input. Please enter 'M' for message or 'F' for text file.")
        return

    _message = input("Enter the message you want to tamper it with: ").encode()
    received_hash = input("Enter the received hash: ")
    nonce = input("Enter the nonce value: ")
    received_checksum = int(input("Enter the received checksum value: "))

    # Perform MITM attack by modifying the message
    modified_message = modify_message(received_message, _message)

    # Compute hash of modified message using custom hash function
    modified_hash = custom_hash(pad_message(modified_message))

    # Verify if modified hash matches the received hash and checksum
    if modified_hash == received_hash and custom_checksum(modified_hash + nonce) == received_checksum:
        print("Receiver: Hash Matched. Message is Authentic.")
        
        save_file_choice = input("Do you want to save the received message to a file? (Y/N) ").upper()
        if save_file_choice == 'Y':
            file_name = input("Enter the file name to save the message: ")
            try:
                with open(file_name, 'wb') as file:
                    file.write(modified_message)
                    print(f"Modified message saved to '{file_name}' successfully.")
            except Exception as e:
                print("Error occurred while saving the modified message to file:", e)
    else:
        print("Receiver: Hash Mismatch. Message may have been tampered with.")

if __name__ == "__main__":
    main()
