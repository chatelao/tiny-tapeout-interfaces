from flask import Flask, jsonify, request, abort
import random
import uuid

app = Flask(__name__)

TARGETS = ["tt01", "tt02", "tt03", "tt04", "tt05", "tt06", "tt07", "tt08", "tt09", "ttihp0p2", "ttihp0p4", "ttihp25a", "ttihp25b", "ttihp26a", "ttgf0p2", "ttsky25a", "ttsky25b", "ttsky26a", "ttgf26a", "ttihp26b", "ttsky26b", "ttsky26c"]

# In-memory session store
sessions = {}

def simulate_logic(inputs, flash=None):
    outputs = []
    for input_state in inputs:
        repeat = input_state.get("repeat", 1)
        # Mocking output logic: reflect inputs or return constant
        output_state = {
            "uo_out": input_state.get("ui_in", 0),
            "uio_out": input_state.get("uio_in", 0),
            "uio_oe": 0
        }
        for _ in range(repeat):
            outputs.append(output_state)
    return outputs

@app.route('/simulation', methods=['POST'])
def simulate():
    data = request.json
    target = data.get('target')
    if not target:
        target = random.choice(TARGETS)

    inputs = data.get('inputs', [])
    flash = data.get('flash')

    outputs = simulate_logic(inputs, flash)

    response = {
        "target": target,
        "outputs": outputs
    }
    if flash:
        response["flash"] = flash

    return jsonify(response), 200

@app.route('/sessions', methods=['POST'])
def create_session():
    data = request.json
    target = data.get('tt-delivers')
    address = data.get('address', 0)
    flash = data.get('flash')

    if target not in TARGETS:
        return jsonify({"error": "Invalid target"}), 400

    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "target": target,
        "address": address,
        "flash": flash,
        "state": {
            "ui_in": 0,
            "uio_in": 0,
            "ena": False,
            "rst_n": True
        }
    }

    return jsonify({"session_id": session_id}), 201

@app.route('/sessions/<session_id>/simulation', methods=['POST'])
def session_simulation(session_id):
    if session_id not in sessions:
        abort(404)

    data = request.json
    inputs = data.get('inputs', [])
    flash = data.get('flash')
    if not flash:
        flash = sessions[session_id].get('flash')

    outputs = simulate_logic(inputs, flash)

    # Update current state to the last input state if any
    if inputs:
        last_input = inputs[-1]
        for key in ["ui_in", "uio_in", "ena", "rst_n"]:
            if key in last_input:
                sessions[session_id]["state"][key] = last_input[key]

    response = {
        "target": sessions[session_id]["target"],
        "address": sessions[session_id]["address"],
        "outputs": outputs
    }
    if flash:
        response["flash"] = flash

    return jsonify(response), 200

@app.route('/sessions/<session_id>/set', methods=['POST'])
def session_set(session_id):
    if session_id not in sessions:
        abort(404)

    data = request.json
    state = sessions[session_id]["state"]

    for key in ["ui_in", "uio_in", "ena", "rst_n"]:
        if key in data:
            state[key] = data[key]

    # Mock output based on new state
    output_state = {
        "uo_out": state["ui_in"],
        "uio_out": state["uio_in"],
        "uio_oe": 0
    }

    return jsonify(output_state), 200

@app.route('/sessions/<session_id>/reset', methods=['POST'])
def session_reset(session_id):
    if session_id not in sessions:
        abort(404)

    sessions[session_id]["state"] = {
        "ui_in": 0,
        "uio_in": 0,
        "ena": False,
        "rst_n": True
    }

    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
