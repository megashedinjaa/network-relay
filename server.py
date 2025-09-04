from flask import Flask, request

app = Flask(__name__)
latest_message = None

@app.route('/notify', methods=['POST'])
def notify():
    global latest_message
    data = request.get_json()
    latest_message = f"Machine {data.get('machine', 'Unknown')} has been connected to the network."
    return {'status': 'ok'}

@app.route('/get', methods=['GET'])
def get_message():
    return {'message': latest_message}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)