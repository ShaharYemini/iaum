import datetime
import time
from automate import use

# exaple time
times = [(11, 0)]

while True:
    t = datetime.datetime.now()
    h = t.hour
    m = t.minute
    if (h, m) in times:
        use()
        time.sleep(60)
    time.sleep(10)
