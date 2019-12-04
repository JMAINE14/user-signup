from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

def correct(inpt):
    if len(inpt) < 3 or len(inpt) > 20:
        return True
    elif ' ' in inpt:
        return True
    return False

def correct_email(inpt):
    if '@' in inpt:
        return True
    return False

@app.route("/", methods=['POST', 'GET'])
def index():
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']


        if correct(username) or not username:
            username_error = "Please enter valid username!"
            username = ''

        if correct(password) or not password:
            password_error = "Please enter valid password"
            password = ''

        if password == verify_error:
            verify_error = "Please verify password"
        else:
            verify = ''

        if email == email_error:
            email_error = "Please enter valid email"
        else:
            email = ''


    return render_template('form.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)


@app.route('/Welcome', methods=['GET'])
def welcome():
    username = request.args.get('username')
    return render_template('base.html', username=username)



if __name__=="__main__":
    app.run(debug=True)







