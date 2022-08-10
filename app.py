from crypt import methods
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # return "gan"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)