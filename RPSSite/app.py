from flask import Flask, request
import random
options = ["r", "p", "s"]
app = Flask(__name__)


def checkwin(a):
    compgen = random.choice(options)
    if compgen == a:
        return "Tie"
    elif compgen == "r" and a == "p":
        return "Player"
    elif compgen == "p" and a == "r":
        return "Computer"
    elif compgen == "p" and a == "s":
        return "Player"
    elif compgen == "s" and a == "p":
        return "Computer"
    elif compgen == "r" and a == "s":
        return "Computer"
    elif compgen == "s" and a == "r":
        return "Scissors"


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "POST":
        text = request.form.get('Text')
        return '''<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Results</title>
  </head>
  <body bgcolor="#3dccc2">
    <center>
    <h2>{}<h2>
    </center>
  </body>
</html>'''.format(checkwin(text))

    return """<html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>RPS!!!!</title>
        </head>
        <body bgcolor="#3dccc2">
        <center>
        <h1 style="color:blue;">Rock Paper Scissors!!!</h1>
        <form method="POST">
        <input type="text" name="Text">
        <p></p>
        <input type="submit" value="Play">
        <h3 style="color:blue;">r is Rock, s is Scissors, p is Paper</h3>
        </form>
        </center>
        </body>
        </html>"""


if __name__ == '__main__':
    app.run(debug=True, port=5000)
