from flask import Flask, request, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'SIH*v-6u)c>q<;;h&);cRw,1E_CO8>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess = int(request.form['guess'])
        low_value = session['low']
        high_value = session['high']
        if guess < session['magic_number']:
            message = 'Your guess is too low!'
            low_value = guess + 1
        elif guess > session['magic_number']:
            message = 'Your guess is too high!'
            high_value = guess - 1
        else:
            message = "VICTORY!"
    else:
        low_value = 1
        high_value = 50
        session['magic_number'] = random.randint(low_value, high_value)
        message = ''

    session['low'] = low_value
    session['high'] = high_value

    return render_template('index.html', message = message,
        low_value = low_value, high_value = high_value)

if __name__ == '__main__':
    app.run()
