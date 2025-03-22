from flask import Flask, request, session, redirect, render_template
import unicodedata

app = Flask(__name__)
app.secret_key = 'supersecretghost'

# Simulated database (username: password)
users_db = {}

@app.route('/')
def index():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Normalize and store lowercase version
        normalized_username = unicodedata.normalize('NFC', username.lower())

        if normalized_username in users_db:
            return 'Username already taken!'

        users_db[normalized_username] = password
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        normalized_username = unicodedata.normalize('NFC', username.lower())
        if users_db.get(normalized_username) == password:
            # Capitalize first character (bypass opportunity here)
            session['user'] = username.capitalize()
            return redirect('/admin')
        return 'Invalid credentials!'

    return render_template('login.html')

@app.route('/admin')
def admin():
    if session.get('user') == 'Admin':
        return render_template('admin.html', flag='D4rk{homoglyph_attack_success}')
    return 'Access Denied!', 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
