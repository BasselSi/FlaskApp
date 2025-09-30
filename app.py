import flask

def sum(x, y):
    return x + y

app = flask.Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello():
    result = None
    if flask.request.method == 'POST':
        try:
            x = int(flask.request.form.get('x', 0))
            y = int(flask.request.form.get('y', 0))
            sum(x, y)
        except ValueError:
            result = 'Invalid input'
    return '''
        <form method="post">
            <input name="x" type="number" step="any" required> +
            <input name="y" type="number" step="any" required>
            <button type="submit">Calculate Sum</button>
        </form>
        <div>Result: {}</div>
    '''.format(result if result is not None else '')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
