from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
import os
import sqlite3
import threading

app = Flask(__name__)

# Database setup
DATABASE = 'shopping_list.db'
email_timer = None  # Global variable to hold the timer

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        conn.commit()

def get_items():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items')
        return cursor.fetchall()

def add_item_to_db(item):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO items (name) VALUES (?)', (item,))
        conn.commit()

def remove_item_from_db(item_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
        conn.commit()

# Access environment variables for email credentials
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

def send_email():
    items = get_items()
    item_list = [item[1] for item in items]  # Extract item names
    msg = MIMEText("\n".join(item_list))
    msg['Subject'] = 'Aktualizacja listy zakupów'
    msg['From'] = EMAIL_USER
    msg['To'] = RECIPENT

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

def reset_email_timer():
    global email_timer
    if email_timer is not None:
        email_timer.cancel()  # Cancel the previous timer
    email_timer = threading.Timer(40.0, send_email)  # Set a new timer for 40 seconds
    email_timer.start()

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', shopping_list=items)  # Pass entire item tuples

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    try:
        if item:
            add_item_to_db(item)
            reset_email_timer()  # Reset the email timer
        else:
            return "Item cannot be empty", 400
    except Exception as e:
        print(f"Error occurred while adding item: {e}")
        return "An error occurred while adding the item", 500
    return redirect(url_for('index'))

@app.route('/remove/<int:item_id>', methods=['POST'])
def remove_item(item_id):
    try:
        remove_item_from_db(item_id)  # Remove item from the database
        reset_email_timer()  # Reset the email timer
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while removing the item", 500
    return '', 204  # Return a 204 No Content response

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080)
