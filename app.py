from flask import Flask, render_template, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="coursedb"
    )

@app.route('/')
def index():
    return render_template('redirect.html')

@app.route('/redirect')
def redirect():
    return render_template('redirect.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/db_register', methods=['POST'])
def db_register():
    mydb = get_db()
    mycursor = mydb.cursor()
    username = request.json['username']
    password = request.json['password']

    try:
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({'status': 'success'})
    except:
        return jsonify({'status': 'error'})

@app.route('/db_login', methods=['POST'])
def db_login():
    mydb = get_db()
    mycursor = mydb.cursor()
    username = request.json['username']
    password = request.json['password']

    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return jsonify({'status': 'success', 'token': username})
    else:
        return jsonify({'status': 'error'})

if __name__ == '__main__':
    app.run(port=8080)
