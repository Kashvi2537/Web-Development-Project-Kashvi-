from flask import Flask, render_template,url_for

app = Flask(__name__)



@app.route('/Model')
def model_page():
    return render_template('Model.html')



@app.route('/')
def home():
    return render_template('intro.html')  # Change this if needed

if __name__ == '__main__':
    app.run(debug=True)