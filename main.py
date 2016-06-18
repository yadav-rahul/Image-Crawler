from flask import Flask, render_template, request, json

ic = Flask(__name__)


@ic.route("/")
def main():
    return render_template("index.html")




if __name__ == "__main__":
    ic.run()
