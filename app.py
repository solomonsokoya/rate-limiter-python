from flask import Flask, request
import time
from algos.token_bucket import Token_Bucket, ips
from algos.fixed_window import Fixed_Window_Counter
app = Flask(__name__)

@app.route("/unlimited")
def unlimited():
    return "Unlimited! Let's Go!"

@app.route("/token-bucket")
def token_bucket():
    ip = request.headers.get("x-test-ip") or request.remote_addr

    if ip not in ips:
        ips[ip] = Token_Bucket()

    if ips[ip].allow_request():
        return "Limited Access"
    else:
        return "Too many requests", 429

counter = Fixed_Window_Counter(60, 60)

@app.route("/fixed-window")
def fixed_window():
	ip_address = request.headers.get("x-test-ip") or request.remote_addr
	timestamp = int(time.time())

	allow_request = counter.request(timestamp, ip_address)
	
	if allow_request:
		return "Limited Access"
	else:
		return "Too man request", 429

