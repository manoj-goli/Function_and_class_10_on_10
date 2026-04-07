#app1/app.py

from flask import Flask, request, make_response, jsonify
import time
import requests

app = Flask(__name__)

@app.route("/cache-demo")
def cache_demo():
    resp = make_response({
        "message": "cache demo",
        "timestamp": time.time()
    })
    resp.headers["Cache-Control"] = "public, max-age=60"
    return resp


@app.route("/")
def home():
    return {
        "message": "app1 is running",
        "path": request.path
    }, 200

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/badrequest")
def badrequest():
    return {"error": "bad request example"}, 400

@app.route("/error")
def error():
    return {"error": "internal server error example"}, 500

@app.route("/slow")
def slow():
    time.sleep(5)
    return {"status": "slow response complete"}, 200

@app.route("/auth")
def auth():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return {"error": "missing authorization header"}, 401
    return {"message": "authorized", "authorization": auth_header}, 200

@app.route("/forbidden")
def forbidden():
    return {"error": "forbidden"}, 403

@app.route("/cookie-set")
def cookie_set():
    resp = make_response({"message": "cookie set"})
    resp.set_cookie("session_id", "abc123", max_age=300)
    return resp

@app.route("/cookie-check")
def cookie_check():
    session_id = request.cookies.get("session_id")
    if not session_id:
        return {"error": "no session cookie found"}, 400
    return {"message": "cookie received", "session_id": session_id}, 200

@app.route("/headers")
def headers():
    return jsonify(dict(request.headers)), 200

@app.route("/proxy-dep")
def proxy_dep():
    url = request.args.get("url", "http://127.0.0.1:5001/upstream-ok")
    try:
        r = requests.get(url, timeout=2)
        return {
            "upstream_url": url,
            "status_code": r.status_code,
            "body": r.text
        }, 200
    except requests.exceptions.RequestException as e:
        return {
            "upstream_url": url,
            "error": str(e)
        }, 502

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)