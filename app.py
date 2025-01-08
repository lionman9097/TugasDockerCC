from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from google.cloud import storage
import pandas as pd
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "skey.json"
app = Flask(__name__)
app.secret_key = 'secrethehe'

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()  
            conn.close()
            return render_template("admin_page.html", users=users)
        
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid username or password"
    return render_template('login.html')

@app.route('/redirect')
def redir():
    return render_template('register.html')

@app.route('/redirect2')
def redir2():
    return render_template('changepass.html')

@app.route('/change', methods=['POST'])
def change():
    if request.method == 'POST':
        username = request.form['username']
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password=? WHERE username=? AND password=?", (new_password, username, old_password))
        conn.commit()
        conn.close()
        return render_template("login.html")

@app.route('/remove', methods=['POST'])
def remove():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username = ? AND name = ?", (username, name))
        conn.commit()
        conn.close()
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return render_template("admin_page.html", users=users)
@app.route('/backup', methods=['POST'])
def backup():
    output_csv_path = "data_export.csv"
    if request.method == 'POST':
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        try:
            # Read data from the database
            df = pd.read_sql_query("SELECT * FROM users", conn)
            # Export to CSV
            df.to_csv(output_csv_path, index=False)
            print(f"Data exported to {output_csv_path}")
        finally:
            conn.close()
        client = storage.Client()
        bucket = client.bucket("bucketcc1rafi")
        blob = bucket.blob("data/data_export.csv")
        blob.upload_from_filename("data_export.csv")
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return render_template("admin_page.html", users=users)

@app.route('/register', methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )''')
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        conn.close()
        return "Username already taken."
    
    cursor.execute('''INSERT INTO users (name, username, password) VALUES (?, ?, ?)''', (name, username, password))
    conn.commit()
    conn.close()
    return render_template("login.html")

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)