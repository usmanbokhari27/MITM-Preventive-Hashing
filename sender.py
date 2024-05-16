import math
from custom_hash import custom_checksum, pad_message, custom_hash  # Importing our custom hash function


def convert_file_to_message(file_path):
    try:
        with open(file_path, 'rb') as file:  
            file_contents = file.read()
            return pad_message(file_contents)
    except FileNotFoundError:
        print("File not found.")
        return None

def main():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        input_choice = input("Do you want to provide a message (M) or a text file (F) to receive? ").upper()

        if input_choice == 'M':
            message = input("Enter your message: ").encode()  # Encode string to bytes
            padded_message = pad_message(message)
            break
        elif input_choice == 'F':
            file_path = input("Enter the path to the received text file: ")
            try:
                with open(file_path, 'rb') as file:
                    received_message = file.read()
                padded_message = pad_message(received_message)
                break
            except FileNotFoundError:
                print("File not found.")
        else:
            print("Invalid input. Please enter 'M' for message or 'F' for text file.")

        attempts += 1
    
    if attempts == max_attempts:
        print("Max attempts reached. Exiting.")
        return
    
    # Get the nonce value
    nonce = input("Enter the value for your nonce: ")
    # Compute hash using custom hash function
    hash_value = custom_hash(padded_message)
    combined_data = hash_value + nonce
    checksum = custom_checksum(combined_data)

    # Simulate sending the message and hash to the receiver
    print("Sender: Message and Hash sent to Receiver") 
    print("Hash:", hash_value)
    print("Checksum: ", checksum)

if __name__ == "__main__":
    main()
