from flask import Flask

app = Flask(__name__)

@app.route("/staff", methods=["POST"])
def staff():
    return "Staff!"

if __name__ == "__main__":
    app.run()