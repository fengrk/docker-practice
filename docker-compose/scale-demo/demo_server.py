import os
import time


host_name = os.environ.get("HOSTNAME")

with open("/app/demo.log", "a") as f:
    f.write("{}\n".format(host_name))


while True:
    time.sleep(60)

