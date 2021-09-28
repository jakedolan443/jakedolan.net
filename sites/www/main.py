from flask import Blueprint


www = Blueprint('www', __name__, static_folder='static/')
@www.route("/", host="www.jakedolan.net")
def HOME():
    return www.send_static_file("index.html")

@www.route("/<f>", host="www.jakedolan.net")
def GET(f):
    f = "{}.html".format(f)
    print(f)
    return www.send_static_file('html/{}'.format(f))

@www.route("/<f1>/<f2>", host="www.jakedolan.net")
def GET2(f1, f2):
    return www.send_static_file("{}/{}".format(f1, f2))

@www.route("/<f1>/<f2>/<f3>", host="www.jakedolan.net")
def GET3(f1, f2, f3):
    return www.send_static_file("{}/{}/{}".format(f1, f2, f3))



