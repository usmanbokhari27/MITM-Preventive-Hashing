import os
from custom_hash import custom_checksum, pad_message, custom_hash  # Importing our custom hash function

def convert_message_to_file(message, file_name):
    try:
        with open(file_name, 'wb') as file:
            file.write(message)
            print(f"Message saved to '{file_name}' successfully.")
    except Exception as e:
        print("Error occurred while saving the message to file:", e)

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

    received_hash = input("Enter the received hash: ")
    nonce = input("Enter the nonce value: ")
    received_checksum = int(input("Enter the received checksum value: "))

    # Compute hash of received message using custom hash function
    computed_hash = custom_hash(pad_message(received_message))
    combined_data = computed_hash + nonce
    computed_checksum = custom_checksum(combined_data)
    
    # Verify if computed hash matches the received hash
    if computed_hash == received_hash and computed_checksum == received_checksum:
        print("Receiver: Hash Matched. Message is Authentic.")
        print(received_message)
        save_file_choice = input("Do you want to save the received message to a file? (Y/N) ").upper()
        if save_file_choice == 'Y':
            file_name = input("Enter the file name to save the message: ")
            convert_message_to_file(received_message, file_name) 
    else:
        print("Receiver: Hash Mismatch. Message may have been tampered with.")

if __name__ == "__main__":
    main()
