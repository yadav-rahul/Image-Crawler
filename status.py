from flask import Flask, render_template, request, json,requests

ic = Flask(__name__)


@ic.route("/")
def main():
    return render_template("index.html")
