from flask import Flask, request, session, redirect, render_template

app = Flask(__name__)
app.secret_key = 'supersecretghost'

# Simulated database (username: password)
users_db = {}

@app.route('/')
def index():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    global users_db
    users_db = {}  # Clear users on each visit (DEV ONLY - REMOVE in prod)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print("[DEBUG] Trying to register:", username)
        print("[DEBUG] Existing users:", list(users_db.keys()))

        if username in users_db:
            return 'Username already taken!'

        users_db[username] = password
        return redirect('/login')

    return render_template('register.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if users_db.get(username) == password:
            session['user'] = username  # No .capitalize()
            return redirect('/admin')
        return 'Invalid credentials!'

    return render_template('login.html')


    return render_template('login.html')

@app.route('/admin')
def admin():
    print("[DEBUG] session['user']:", session.get('user'))
    print("[DEBUG] ord values:", [ord(c) for c in session.get('user', '')])

    if session.get('user') == 'Admin':
        return render_template('admin.html', flag='D4rk{homoglyph_attack_success}')
    return 'Access Denied!', 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
