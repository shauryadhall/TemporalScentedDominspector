
from flask import Flask, request, jsonify, send_from_directory
import os
import sqlite3
from datetime import datetime

app = Flask(__name__, static_url_path='')

# Initialize database
def init_db():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS emails
                 (email TEXT PRIMARY KEY, timestamp DATETIME)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

@app.route('/submit-email', methods=['POST'])
def submit_email():
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400
        
    try:
        conn = sqlite3.connect('emails.db')
        c = conn.cursor()
        c.execute("INSERT INTO emails VALUES (?, ?)", (email, datetime.now()))
        conn.commit()
        conn.close()
        print(f"New email submission stored: {email}")
        return jsonify({'message': 'Email submitted successfully'}), 200
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400
    except Exception as e:
        print(f"Error storing email: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
