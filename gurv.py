from gevent.pywsgi import WSGIServer
from main import app

http_server = WSGIServer(('', 8080))
http_server.serve_forever()
