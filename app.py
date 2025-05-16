
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/submit-email', methods=['POST'])
def submit_email():
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400
        
    # Here you can add code to store the email (e.g., in a database)
    # For now, we'll just print it
    print(f"New email submission: {email}")
    return jsonify({'message': 'Email submitted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
