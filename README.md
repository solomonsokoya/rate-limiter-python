# Rate Limiter - Token Bucket (`tokenbucket.py`)
This Python code provides an implementation of a token bucket algorithm for rate limiting. The token bucket algorithm is used to control the rate at which requests can be made to a service or resource, ensuring that requests do not exceed a specified rate.

The code includes a `TokenBucket` class that allows you to create and manage a token bucket with the following features:

- Add tokens to the bucket at a fixed rate over time.
- Handle incoming requests by checking token availability and allowing or declining requests based on the available tokens.

# Rate Limiter - Fixed Window Counter (`fixedwindow.py`)
This Python code offers an implementation of a Fixed Window Counter algorithm for rate limiting purposes. The Fixed Window Counter algorithm tracks incoming requests within predefined time windows to manage and control the rate at which requests are processed, ensuring that the request rate does not exceed a specified threshold within each window.

The code includes a `FixedWindowCounter` class that facilitates the following functionalities:

- Tracking Request Rate: It maintains a counter for each time window, incrementing the counter for incoming requests within the window.
- Threshold Management: Discards requests that surpass the defined threshold for the respective time window.
- Window Definition: Uses the floor of the current timestamp to determine windows, ensuring requests fall within their respective timeframes.

### Features
- Process Requests: Accepts incoming requests with timestamps and IP addresses, managing their allowance or rejection based on the defined threshold within each time window.
- Clean Old Windows: Provides functionality to remove old windows that are no longer relevant based on the current time.
