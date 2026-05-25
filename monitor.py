import os
import time

while True:

    if os.path.exists("model.pkl"):
        print("Model file exists and system is healthy")
    else:
        print("Model file missing")

    time.sleep(10)