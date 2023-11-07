import threading
import time

# There is a ‘bucket’ that has capacity for N tokens. A bucket per user or IP address
BUCKET_CAP = 10
REQUEST_PER_SEC = 20
ips = {}


# Refill tokens every second
def refill_tokens_interval():
    while True:
        time.sleep(1)
        for bucket in ips.values():
            bucket.fill_bucket()

# Start the token refill process in the background
refill_thread = threading.Thread(target=refill_tokens_interval)
refill_thread.daemon = True
refill_thread.start()

class Token_Bucket: 
	def __init__(self):
		self.bucket = [1] * BUCKET_CAP
		self.last_check = time.time()
	def fill_bucket(self):
		if len(self.bucket) == 10:
			return
		now = time.time()
		time_between = now - self.last_check
		
		if time_between > 1:
			self.bucket = [1] * min(len(self.bucket) + 1, 10) 
	def allow_request(self):
		if len(self.bucket) <= 0:
			return False
		self.bucket.pop()
		return True
