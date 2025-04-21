# IMPORTING
from flask import Flask,render_template,request

# INTERACTION
web  = Flask(__name__)

# MAPPING
@web.route('/')
@web.route('/register')
# INPUT
def homepage():
    return render_template('register.html')  

#redirecting

#MAPPING
@web.route('/confirmation' , methods=['POST','GET'])

# INPUT
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        phone = request.form.get('phone')
        email = request.form.get('email')
        return render_template('confirmation.html', name=name, city=city, phone=phone, email=email)
    else:
        return render_template('register.html')


# MAIN

if __name__ == '__main__':
    web.run(debug=True, port=5000)