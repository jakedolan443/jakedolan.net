from flask import Flask
from sites.www_redir.main import www_redir
from sites.www.main import www
from sites.apt.main import apt

app = Flask(__name__, static_url_path='')
app.url_map.host_matching = True

app.register_blueprint(www_redir)
app.register_blueprint(www)
app.register_blueprint(apt)



