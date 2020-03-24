from flask import Flask, request
import random
app = Flask(__name__)
accountdic = {"admin": "admin"}

def checkwin(key, passwrd):
    if key in accountdic and accountdic[key] == passwrd:
        return "OK"
    else:
        return "Not OK"

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "POST":
        text = request.form.get('Username')
        pswrd = request.form.get('Password')
        if checkwin(text, pswrd) == "OK":
            return '''
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Results</title>
  </head>
  <body bgcolor="#3dccc2">
    <center>
    <h2>OK</h2>
    </center>
  </body>
</html>'''


    return"""
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>RPS!!!!</title>
    </head>
    <body bgcolor="#3dccc2">
        <center>
        <h1 style="color:blue;">Login Page</h1>
        <form method="POST">
            <p>Username</p>
            <input type="text" name="Username" style="color:blue;">
            <p>Password</p>
            <input type="text" name="Password" style="color:blue;">
            <p></p>
            <input type="submit" Value="Login">
        </form>
        </center>
        </body>
        </html>"""


if __name__ == '__main__':
    app.run(debug=True, port=5000)
