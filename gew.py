from gevent.pywsgi import WSGIServer
from main import app

http_server = WSGIServer(('127.0.0.1', 8080), app)
http_server.serve_forever()
