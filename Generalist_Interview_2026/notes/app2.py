#app2/app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "app2 is running"}, 200

@app.route("/upstream-ok")
def upstream_ok():
    return {"status": "upstream ok"}, 200

@app.route("/upstream-fail")
def upstream_fail():
    return {"error": "upstream failure example"}, 503

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)