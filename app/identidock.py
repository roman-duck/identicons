from flask import Flask, Response, request
import requests
import hashlib

app = Flask(__name__)
SALT = "this is a salt"
DEFAULT_NAME = "Joe Bloggs"

@app.route('/', methods=['GET', 'POST'])
def mainpage():
    name = DEFAULT_NAME
    if request.method == 'POST':
        name = request.form['name']
    salted_name = SALT + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()
    header = '<html><head><title>IdentiIcons</title></head><body>'
    body = '''<form method="POST">
            Hello <input type="text" name="name" value="{0}">
            <input type="submit" value="Submit">
            </form>
            You look like a:
            <img src="/monster/{1}">
            '''.format(name, name_hash)
    footer = '</body></html>'
    return header + body + footer

@app.route('/monster/<name>')
def get_identicon(name):
    r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
    image = r.content

    return Response(image, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
