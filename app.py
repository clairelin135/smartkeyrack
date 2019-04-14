from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit
from firebase import firebase

'''
import eventlet
eventlet.monkey_patch()
'''
from gevent.pywsgi import WSGIServer
from gevent import monkey

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

clients = []

@app.route('/')
def index():
    return render_template('index.html', **key_statuses)

@socketio.on('connected')
def connected():
    print('connected' + request.namespace)
    clients.append(request.namespace)

@socketio.on('disconnect')
def disconnect():
    print('disconnected' + request.namespace)
    clients.remove(request.namespace)

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
        # for i in range(len(clients)):
        #     clients[i].emit('render keys', payload)
        socketio.emit('render keys', payload)
    return "None"

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
