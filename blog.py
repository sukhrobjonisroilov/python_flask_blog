from flask import Flask, render_template

import os

articel = os.listdir("articles")
app = Flask(__name__)


@app.route("/")
def blog():
    return render_template("blog.html", articel=articel)


@app.route('/blog/<slug>')
def arcitel(slug: str):
    return render_template('articel.html')


if __name__ == "__main__":
    app.run(port=4200, debug=True)
