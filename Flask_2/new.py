from flask import Flask, render_template, request
import os


app = Flask(__name__)

pic_folder = os.path.join('static')
app.config['UPLOAD_FOLDER'] = pic_folder
@app.route('/')
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'PL.jpg')
    return render_template('home.html',user_image= pic)

@app.route('/second')
def second():
    # return "welcome to the second page"
    return render_template('second.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)