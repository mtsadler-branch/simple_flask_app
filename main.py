from flask import *

app = Flask(__name__, template_folder="templates")

@app.route("/")
def homePage():
    return render_template("home.html", name="Mike", age=27)


@app.route("/second")
def secondPage():
    return render_template("secondPage.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
