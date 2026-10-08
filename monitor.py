import time
import urllib.request

URL = "http://app:5000/health"

while True:
    try:
        response = urllib.request.urlopen(URL, timeout=5)
        print(f"MONITORING: Application is HEALTHY - Status {response.status}", flush=True)
    except Exception as e:
        print(f"MONITORING: Application is UNHEALTHY - {e}", flush=True)

    time.sleep(10)