# IMPORTING
from flask import Flask,render_template,request

# INTERACTION
app = Flask(__name__)

# MAPPING
@app.route('/')


# INPUT
def homepage():
    return render_template('index.html')  

# MAIN

if __name__ == '__main__':
    app.run(debug=True)
    
