from flask import Flask, request

from tokenbucket import Token_Bucket, ips
app = Flask(__name__)

@app.route("/unlimited")
def unlimited():
    return "Unlimited! Let's Go!"

@app.route("/limitedtb")
def limitedtb():
    ip = request.headers.get("x-test-ip") or request.remote_addr

    if ip not in ips:
        ips[ip] = Token_Bucket()

    if ips[ip].allow_request():
        return "Limited Access"
    else:
        return "Too many requests", 429
