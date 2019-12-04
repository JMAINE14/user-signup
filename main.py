from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

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


        if not username:
            username_error = "Please enter valid username!"

        if not password:
            password_error = "Please enter valid password"

        if not verify:
            verify_error = "Please verify password"

        if not email:
            email_error = "Please enter valid email"


    return render_template('form.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

# @app.route("/login", methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         user = User.query.filter_by(email=email).first()
#         if user and user.password == password:
#             session['email'] = email
#             flash("Logged in")
#             return redirect('/')
#         else:
#             flash('Email/Password aint right, or user does not exist', 'error')

#     return render_template('login.html')












if __name__=="__main__":
    app.run(debug=True)







