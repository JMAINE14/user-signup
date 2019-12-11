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
    if '@' in inpt and "." in inpt:
        return True
    return False

@app.route("/", methods=['POST', 'GET'])
def index():
    username = ''
    email = ''
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
            password_error = "Please enter matching password"
            password = ''
        else:
            if verify != password:
                verify_error = "Please enter valid password"        

        # if password == '':
        #     password_error = "Please enter a password"

        if email != '':
            if email.count('@') != 1 or email.count('.') != 1:
                email_error = "Invalid Email"


        if not username_error and not password_error and not verify_error and not email_error:
            return redirect('/welcome?username={0}'.format(username))
            return render_template('welcome.html', username=username)

    return render_template('form.html', username_error=username_error, password_error=password_error, 
    verify_error=verify_error, email_error=email_error, username=username, email=email)




@app.route('/welcome', methods=['GET'])
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)



if __name__=="__main__":
    app.run(debug=True)







