from flask import Flask, request, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'Lugg@ge_pw:12345'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess = request.form['guess']
        if guess < magic_number:
            low_value = guess
            message = f'{guess} is too low!'
        elif guess > magic_number:
            high_value = guess
            message = f'{guess} is too high!'
        elif guess == magic_number:
            message = f'Congratualations!  {guess} was the magic number!'
            still_guessing = False
        else:
            message = 'Please enter a valid input'
        low_value = 1
        high_value = 50
        still_guessing = True
    else:
        low_value = 1
        high_value = 50
        magic_number = random.randint(low_value, high_value)
        still_guessing = True

        message = ''

    return render_template('index.html', message = message,
        low_value = low_value, high_value = high_value, still_guessing = still_guessing)

if __name__ == '__main__':
    app.run()
