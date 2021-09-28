from flask import Blueprint, request, redirect


www_redir = Blueprint('www_redir', __name__)
@www_redir.route('/', defaults={'path': ''}, host="jakedolan.net")
@www_redir.route('/<path:path>', host="jakedolan.net")
def redir(path):
    url = request.url.replace('jakedolan.net', 'www.jakedolan.net', 1)
    code = 301
    return redirect(url, code=code)

