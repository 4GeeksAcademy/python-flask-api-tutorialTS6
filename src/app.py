from flask import flask, jsonify
app = Flask (__name__)
from flask import request

todos = [
    {"label":"myFirstTask","done":False},
    {"label":"mySecondTask","done":False}
]

@app.route ('/todos',methods=['GET'])
def Hello_World():
    json_text=jsonify(todos)
    return json_text

@app.route ('/todos',methods=['GET'])
def add_new_todo():
    request_body=request.json
    print("incomingRequest",request_body)
    return "responseForPostTODO"

@app.route ('/todos/<int:postion>',methods=['GET'])
def delete_todo(postion):
    print('deleteingThisPostion',postion)
    todos.pop((postion-1))
    return jsonify(todos)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)