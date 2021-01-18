from flask import Flask, jsonify, request
import json
app = Flask(__name__)

# headers = {'Content-Type': 'application/json'; charset=utf-8'}
# data = {'flags':'data'}
# requests.post('ip_address', headers = headers, data = json.dumps(data))
value = 'False'
gesture_msg = 'Init'
action_msg = 'Init'
head_msg = 'Init'

######## gesture_data ########
@app.route("/gesture", methods=['POST'])
def receive_gesture():
    global gesture_msg
    g_msg = request.get_json()
    gesture_msg = g_msg['flags']
    return 'received'

@app.route("/get_gesture")
def send_gesture():
    global gesture_msg
    return str(gesture_msg)


######## action_data ########
@app.route("/action", methods=['POST'])
def receive_action():
    global action_msg
    a_msg = request.get_json()
    action_msg = a_msg['flags']
    return 'received'

@app.route("/get_action")
def send_action():
    global action_msg
    return str(action_msg)


######## head_data ########
@app.route("/head", methods=['POST'])
def receive_head():
    global head_msg
    h_msg = request.get_json()
    head_msg = h_msg['flags']
    return 'received'

@app.route("/get_head")
def send_head():
    global head_msg
    return str(head_msg)


######## web_open_signal ########
@app.route("/sub", methods=['POST'])
def receive_value():
    global value
    msg = request.get_json()
    value = msg['flags']
    return 'received'

@app.route("/get_value")
def send_value():
    global value
    return str(value)


if __name__ == '__main__':
    app.debug = False
    app.run(host="192.168.0.5", port = "59099", threaded = True)