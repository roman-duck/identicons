from flask import Flask

app = Flask(__name__)
DEFAULT_NAME = "World"

@app.route("/")
def get_identicon():
    name = DEFAULT_NAME
    header = '<html><head><title>IdentiIcons</title></head><body>'
    body = '''<form method="POST">
            Hello <input type="text" name="name" value="{}">
            <input type="submit" value="Submit">
            </form>
            You look like a:
            <img src="/monster/monster.png">
            '''.format(name)
    footer = '</body></html>'
    return header + body + footer

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
