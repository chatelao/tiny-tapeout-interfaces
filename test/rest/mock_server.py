from flask import Flask, jsonify, request
import random

app = Flask(__name__)

TARGETS = ["tt01", "tt02", "tt03", "tt04", "tt05", "tt06", "tt07", "tt08", "tt09", "ttihp0p2", "ttihp0p4", "ttihp25a", "ttihp25b", "ttihp26a", "ttgf0p2", "ttsky25a", "ttsky25b", "ttsky26a", "ttgf26a", "ttihp26b", "ttsky26b", "ttsky26c"]

@app.route('/simulation', methods=['POST'])
def simulate():
    data = request.json
    target = data.get('target')
    if not target:
        target = random.choice(TARGETS)

    inputs = data.get('inputs', [])
    flash = data.get('flash')
    outputs = []

    # Simple mock simulation logic: reflect inputs or return constant for now
    for input_state in inputs:
        repeat = input_state.get("repeat", 1)
        # Mocking output logic
        output_state = {
            "uo_out": input_state.get("ui_in", 0),
            "uio_out": input_state.get("uio_in", 0),
            "uio_oe": 0
        }
        for _ in range(repeat):
            outputs.append(output_state)

    response = {
        "target": target,
        "outputs": outputs
    }
    if flash:
        response["flash"] = flash

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5000)
