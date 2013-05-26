from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/<path:directory_path>")
def directory(directory_path):
    files = os.listdir(directory_path)
    breadcrumbs = str(directory_path).split("/")
    return render_template('file_list.html',
        files = files, breadcrumbs = breadcrumbs)


if __name__ == "__main__":
    app.run(debug=True)