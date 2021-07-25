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
        session['turns_taken'] += 1
        still_guessing = True
        if guess < session['magic_number']:
            message = f'Your guess ({guess}) is too low.'
            low_value = guess + 1
        elif guess > session['magic_number']:
            message = f'Your guess ({guess}) is too high.'
            high_value = guess - 1
        else:
            message = f"VICTORY! You took {session['turns_taken']} tries to guess the magic number."
            still_guessing = False
    else:
        low_value = 1
        high_value = 50
        session['magic_number'] = random.randint(low_value, high_value)
        still_guessing = True
        message = ''
        session['turns_taken'] = 0

    session['low'] = low_value
    session['high'] = high_value

    return render_template('index.html', message = message,
        low_value = low_value, high_value = high_value, still_guessing = still_guessing)

if __name__ == '__main__':
    app.run()
