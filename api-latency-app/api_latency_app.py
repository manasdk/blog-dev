import json
import math
import time
from flask import Flask

app = Flask(__name__)
sleep_for = 0

@app.route('/bad/<int:response_latency>', methods=['POST'])
def be_bad(response_latency=20):
    print "Setting up for bad behavior %s" % response_latency
    global sleep_for
    sleep_for = response_latency
    return json.dumps({})

@app.route('/good', methods=['POST'])
def be_good():
    print "Setting up for good behavior"
    global sleep_for
    sleep_for = 0
    return json.dumps({})

@app.route('/square/<int:num>', methods=['GET', 'POST'])
def get_square(num):
    print "Called with num : %s" % num
    time.sleep(sleep_for)
    return json.dumps({"square": math.pow(num, 2)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')
