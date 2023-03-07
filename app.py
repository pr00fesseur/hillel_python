from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index(*args, **kwargs):
    breakpoint()
    context = {'name': 'Karolina'}
    return render_template('index.html', **context)
