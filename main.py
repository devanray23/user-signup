from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/index', methods=['POST','GET'])
def index():

    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']

        email_error = ''
        username_error = ''
        password_error = ''

        if not username:
            username_error = 'Not a valid username.'

        if not password:
            password_error = 'Must enter a password.'

        if not verify:
            password_error = 'Must verify password.'

        if len(password) < 3 or len(password) > 20:
            password_error = 'Password must be between 3-20 characters.'

        if ' ' in password:
            password_error = 'Password cannot contain spaces.'

        if not password == verify:
            password_error = 'Passwords do not match.'

        if '@' not in email and '.' not in email:
            email_error = 'Not a vaild email'

        if len(email) < 3 or len(email) > 20:
            email_error = 'Email must be between 3-20 characters.'

        if ' ' in email:
            email_error = 'Email cannot contain spaces.'


        if not email_error and not username_error and not password_error:
            return render_template('home.html', username=username)
        else:
            return render_template('index.html', email=email, username=username, 
                email_error=email_error, username_error=username_error,
                password_error=password_error)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()