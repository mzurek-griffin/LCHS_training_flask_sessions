from flask import Flask, request, render_template
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        low_value = 1
        high_value = 50
        magic_number = random.randint(low_value, high_value)

        message = ''

    return render_template('index.html', message = message,
        low_value = low_value, high_value = high_value)

if __name__ == '__main__':
    app.run()
