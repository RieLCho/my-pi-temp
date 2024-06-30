from flask import Flask, request, jsonify

app = Flask(__name__)
data = []

@app.route('/log', methods=['POST'])
def log_temp():
    entry = request.get_json()
    if entry:
        data.append(entry)
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "failure", "reason": "Invalid JSON"}), 400

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data), 200

@app.route('/')
def index():
    return '''
    <html>
    <head><title>Flask Server</title></head>
    <body>
        <h1>Welcome to Flask Server</h1>
        <p>Use <a href="/data">/data</a> to view logged data.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
