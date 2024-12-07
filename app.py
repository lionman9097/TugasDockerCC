from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import pandas as pd

app = Flask(__name__)
app.secret_key = 'secrethehe'

# Halaman utama (Login)
@app.route('/')
def home():
    return render_template('login.html')

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    
    # Menggunakan query parameter untuk menghindari SQL injection
    users = pd.read_sql_query("SELECT * FROM users WHERE username=? AND password=?", conn, params=(username, password))
    
    if not users.empty:
        nama = users['name'].iloc[0]
        session['username'] = username
        return f"Login successful, Selamat datang {nama}"
    else:
        return "Invalid username or password"

# Redirect ke halaman registrasi
@app.route('/redirect')
def redir():
    return render_template('register.html')

# Register route
@app.route('/register', methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    
    # Cek apakah username sudah ada
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        return "Username already exists. Please choose a different one."
    
    # Membuat tabel jika belum ada
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    
    # Menambahkan data user baru
    cursor.execute('''
    INSERT INTO users (name, username, password) VALUES(?, ?, ?)
    ''', (name, username, password))
    conn.commit()
    conn.close()
    
    return redirect(url_for('home'))  # Redirect ke halaman login setelah berhasil registrasi

if __name__ == '__main__':
    app.run(debug=True)
