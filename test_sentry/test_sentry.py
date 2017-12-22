'''
This is NOT an unit test.  Has to perform manually
'''
import threading
import datetime
import time
from raven import Client

# create Sentry client
CLIENT = Client(
    'http://95298c03b81841698587dfbaa1b3cba4:c4f5e7b76c264bbd858a721cfecc68fd@sentry-dev-2.mia.ucloud.int:9000/2'
)


def do_every(interval_sec, iterations, log_sentry_func, batch_size, message):
    if iterations != 1:
        threading.Timer(interval_sec, do_every, [
            interval_sec, 0 if iterations == 0 else iterations - 1,
            log_sentry_func, batch_size, message
        ]).start()
    log_sentry_func(batch_size, message)


# send the same event message to the Sentry server multiple times
def log_sentry(batch_size, message):
    print "Test: " + str(datetime.datetime.now())
    for _ in range(batch_size):
        CLIENT.captureMessage(message)


# start testing here
# repetitively send event clusters to the Sentry server
CONDITION = 'normal'  # test condition
INTERVAL_SEC = 1  # interval between clusters
ITERATIONS = 10  # #clusters
BATCH_SIZE = 1  # #events in each cluster
MESSAGE = "%d events per %s second, %d iterations, %s, %s" % (
    BATCH_SIZE, INTERVAL_SEC, ITERATIONS, CONDITION,
    str(datetime.datetime.now()))
do_every(INTERVAL_SEC, ITERATIONS, log_sentry, BATCH_SIZE, MESSAGE)

# wait until pending events sent out
while True:
    time.sleep(1)
