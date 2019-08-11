from flask import Flask
from flask import request
from flask import render_template, redirect, url_for, request
APP = Flask(__name__)
@APP.route('/')
def login1():
      return render_template('login1.html')
@APP.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            return redirect(url_for('login1'))
        else:
           return render_template('hello.html', error=error)

if __name__ == '__main__':
      APP.debug=True
      APP.run()
