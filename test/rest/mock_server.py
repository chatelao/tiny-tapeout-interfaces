from flask import Flask, jsonify, request

app = Flask(__name__)

pins = {
    "ui_in": 0,
    "uo_out": 0,
    "uio": 0
}

@app.route('/pins', methods=['GET'])
def get_pins():
    target = request.args.get('target')
    address = request.args.get('address')
    # For mock purposes, we just return the pins regardless of target/address
    return jsonify(pins)

@app.route('/pins/<pin_name>', methods=['PUT'])
def set_pin(pin_name):
    if pin_name not in pins:
        return "Not Found", 404
    target = request.args.get('target')
    address = request.args.get('address')
    data = request.json
    pins[pin_name] = data.get('state', pins[pin_name])
    return "OK", 200

if __name__ == '__main__':
    app.run(port=5000)
