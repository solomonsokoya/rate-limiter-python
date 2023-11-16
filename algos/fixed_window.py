from collections import deque, defaultdict

class Fixed_Window_Counter:
	
	def __init__(self, window_size, max_request):
		self.window_size = window_size
		self.max_request = max_request
		self.window = deque()
		self.counter = defaultdict(int)

	def request(self, timestamp, ip_address):
		current_window = timestamp - (timestamp % self.window_size)

		if len(self.window) == 0 or self.window[0] != current_window:
			self.window.appendleft(current_window)
			self.counter[current_window] = defaultdict(int)
			self.counter[current_window][ip_address] = 1

		else:
			self.counter[current_window][ip_address] += 1

		if sum(self.counter[current_window].values()) > self.max_request:
			return False
		return True
		

	def clean_old_windows(self, current_time):
		current_window = current_time - (current_time % self.window_size)
		
		while len(self.window) > 0 and self.window[-1] < current_window:
			self.window.pop()

