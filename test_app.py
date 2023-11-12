import unittest
from flask import Flask
from app import app
from tokenbucket import Token_Bucket, ips
import time

class TestTokenBucketApp(unittest.TestCase):
    def test_limitedtb_rate_limiting(self):
        res = []
        client = app.test_client()
        ip = "127.0.0.1"  # Replace with a valid IP address.

        for _ in range(11):
            response = client.get('/limitedtb', headers={'x-test-ip': ip})
            res.append(response.status_code)

		ip2 = "128.0.0.1"  # Replace with a valid IP address.

        for _ in range(8):
            response = client.get('/limitedtb', headers={'x-test-ip': ip2})
            res.append(response.status_code)



        response = client.get('/limitedtb', headers={'x-test-ip': ip})
        res.append(response.status_code)

        # Check that 'res' consists of 10 '200' codes and 10 '429' codes.
        self.assertEqual(res.count(200), 10)
        self.assertEqual(res.count(429), 2)
