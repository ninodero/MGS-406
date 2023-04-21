from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my Flask app!'

@app.route('/greetings/<season>')
def greetings(season):
    if season == 'christmas':
        return 'Merry Christmas!'
    elif season == 'newyear':
        return 'Happy New Year!'
    else:
        return 'Greetings for ' + season

if __name__ == '__main__':
    app.run(debug=True)
