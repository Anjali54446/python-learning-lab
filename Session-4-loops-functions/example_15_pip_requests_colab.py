# PACKAGE INSTALLATION DEMO — Google Colab
# In a Google Colab code cell, run this line separately:
# !pip install requests
#
# Then run the Python code below in a normal Python code cell.

import requests

response = requests.get("https://httpbin.org/get", timeout=10)
print("HTTP status:", response.status_code)
print("Response is JSON:", response.headers.get("content-type", "").startswith("application/json"))

# If internet access is unavailable in your environment, skip this live request.
