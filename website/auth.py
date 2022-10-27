from flask import Blueprint, render_template, request
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # POST request to send email and password data to us, the server
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # will need to process these
        #to add - flashing messages
        #hi
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>You have successfully logged out.</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form
        firstName = request.form.get('firstName')
        pword1 = request.form.get('password1')
        pword2 = request.form.get('password2')

        #will need to process these
        if len(email) < 4:
            print("email too short")

        
    return render_template("signup.html")

