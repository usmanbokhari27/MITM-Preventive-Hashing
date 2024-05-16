from flask import Flask, render_template, request, redirect, url_for
import os
from custom_hash import custom_checksum, pad_message, custom_hash
from attack import modify_message, main as perform_attack

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sender', methods=['GET', 'POST'])
def sender():
    if request.method == 'POST':
        message = request.form['message'].encode()
        padded_message = pad_message(message)
        nonce = request.form['nonce']
        hash_value = custom_hash(padded_message)
        combined_data = hash_value + nonce
        checksum = custom_checksum(combined_data)

        # Simulate sending the message and hash to the receiver
        return render_template('sender_result.html', hash_value=hash_value, nonce=nonce, checksum=checksum)

    return render_template('sender.html')

@app.route('/receiver', methods=['GET', 'POST'])
def receiver():
    if request.method == 'POST':
        received_hash = request.form['received_hash']
        received_message = request.form['received_message'].encode()
        nonce = request.form['nonce']
        received_checksum = int(request.form['received_checksum'])
        
        # Simulate receiving the message and hash from the sender
        computed_hash = custom_hash(pad_message(received_message))  
        combined_data = computed_hash + nonce
        computed_checksum = custom_checksum(combined_data)

        if computed_hash == received_hash and computed_checksum == received_checksum:
            message = "Message is Authentic."
        else:
            message = "Message may have been tampered with."

        return render_template('receiver_result.html', message=message)

    return render_template('receiver.html')

@app.route('/attack', methods=['GET', 'POST'])
def attack():
    if request.method == 'POST':
        received_hash = request.form['received_hash']
        nonce = request.form['nonce']
        received_checksum = int(request.form['received_checksum'])
        message = request.form['message'].encode()
        user_message = request.form['user_message'].encode()

        # Modify the user's message using modify_message function
        modified_message = modify_message(message, user_message)

        # Compute hash of modified message using custom hash function
        modified_hash = custom_hash(pad_message(modified_message))

        
        message = "Hash Matched. Message is Authentic."

        return render_template('attack_result.html', message=message)

    return render_template('attack.html')

if __name__ == '__main__':
    app.run(debug=True)
