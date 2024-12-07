from flask import Flask, render_template, request,session
import sqlite3
import pandas as pd
app = Flask(__name__)
app.secret_key = 'secrethehe'
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    users=pd.read_sql_query("SELECT * FROM users WHERE username=? AND password=?",conn,params=(username,password,))
    if not users.empty:
            nama=users['name'].iloc[0]
            session['username'] = username
            return  f"Login successful, Selamat datang {nama}"
    else:
        return "Invalid username or password"
@app.route('/redirect')
def redir():
    return render_template('register.html')

@app.route('/register',methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    INSERT INTO users (name,username,password) VALUES(?,?,?)
    ''',(name,username,password,))
    conn.commit()
    conn.close()
if __name__ == '__main__':
    app.run(debug=True)