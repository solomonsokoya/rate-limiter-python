import unittest
from datetime import datetime, timedelta
from flask import Flask
from algos.fixed_window import Fixed_Window_Counter 

class TestFixedWindowRoute(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        self.counter = Fixed_Window_Counter(window_size=60, max_request=5)

    def test_fixed_window_route_within_limit(self):
        @self.app.route('/test-fixed-window')
        def test_fixed_window():
            ip_address = '127.0.0.1'
            timestamp = int(datetime.now().timestamp())

            allow_request = self.counter.request(timestamp, ip_address)

            if allow_request:
                return "Allowed"
            else:
                return "Too many requests", 429

        for _ in range(5):
            response = self.client.get('/test-fixed-window')
            self.assertEqual(response.status_code, 200)

        # 6th request should exceed the limit
        response = self.client.get('/test-fixed-window')
        self.assertEqual(response.status_code, 429)

if __name__ == '__main__':
    unittest.main()
