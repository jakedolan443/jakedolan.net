import flask


app = flask.Flask(__name__, static_url_path='')
accepted_files = []

@app.route("/")
def HOME():
    return app.send_static_file("index.html")

@app.route("/<f>")
def GET(f):
    f = "{}.html".format(f)
    print(f)
    if not f in accepted_files:
        return app.send_static_file('html/{}'.format(f))
    


if __name__ == "__main__":
    app.run(host="0.0.0.0")
