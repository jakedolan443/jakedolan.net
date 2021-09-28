from flask import Blueprint, render_template
import os


apt = Blueprint('apt', __name__, static_folder="static/", template_folder="templates/")
run_path = "{}/sites/apt".format(os.getcwd())
print(run_path)

@apt.route('/', defaults={'path': ''}, host="apt.jakedolan.net")
@apt.route('/<path:path>', host="apt.jakedolan.net")
def catch_all(path):
    full_path = "{}/static/{}".format(run_path, path)
    if os.path.isdir(full_path):
        files = os.listdir(full_path)
        data = [path,[]]
        for f in files:
            data[1].append({"path":"{}/{}".format(path, f), "end":f, "size":os.path.getsize("{}/{}".format(full_path, f))})
            if os.path.isdir("{}/{}".format(full_path, f)):
                data[1][-1]['size'] = "-"
        return render_template('index.html', data=data)
    return apt.send_static_file(path)
