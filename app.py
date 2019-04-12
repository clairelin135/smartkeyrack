from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit
from firebase import firebase

'''
import eventlet
eventlet.monkey_patch()
'''

app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True)
firebase = firebase.FirebaseApplication('https://smartkeyrack.firebaseio.com/', None)

'''
Payload Structure
key_statuses = {
    'key1': {
        'name': 'Claire Lin',
        'status': 'home'
    }
    ...
}
'''
keys = ['key1', 'key2', 'key3', 'key4']
key_statuses = firebase.get('/keys', None)

@app.route('/')
def index():
    return render_template('index.html', **key_statuses)

@socketio.on('connect')
def on_connect():
    pass

@app.route('/update', methods=['POST'])
def update():
    req_data = request.json
    if request.method == 'POST':
        for k in keys:
            keyAttr = req_data.get(k, None)
            if keyAttr:
                for attr in keyAttr:
                    key_statuses[k][attr] = keyAttr[attr]
            #firebase.patch('/keys/', {k: key_statuses[k]})
        payload = {
            'hi': 'hello'
        }
        socketio.emit('render keys', payload)
        socketio.sleep(0)
    return "None"

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
