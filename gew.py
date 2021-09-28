from gevent.pywsgi import WSGIServer
from main import app

http_server = WSGIServer(('127.0.0.1', 8080), app, keyfile='/etc/letsencrypt/live/jakedolan.net/privkey.pem', certfile='/etc/letsencrypt/live/jakedolan.net/cert.pem')
http_server.serve_forever()
