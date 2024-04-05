from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/signUp', methods=['POST'])
def signUp():
    email = request.form['email']
    address = request.form['Address']
    password = request.form['password']
    confirm_password = request.form['confirm password']

    # Perform any necessary validation or processing with the form data

    # Return a response or redirect to another page

    # Example response
    return 'SignUp successful!'

if __name__ == '__main__':
    app.run()
    
    
import random
import string

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXWZ"
numbers = "0123456789"
symbols = "~!@#$%^&*()_+"

string = lower + upper + numbers + symbols
length = 16

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
password = generate_password(length)
print("Generated Password:", password)