from flask import Flask, render_template, redirect

from utils import render_md

app = Flask(__name__)


@app.get("/")
def root():
    return redirect("/resume/fr/")


@app.get("/resume/<lang>/")
def resume(lang):
    meta, content = render_md(f"resume/{lang}.md")
    return render_template("resume.html", content=content, **meta)


@app.get("/projects/")
def projects():
    return "projects"


@app.get("/guides/")
def guides():
    return "guides"


if __name__ == '__main__':
    app.run()
