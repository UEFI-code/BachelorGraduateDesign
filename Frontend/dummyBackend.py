from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat_test', methods=['POST'])
def chat_test():
    data = json.loads(request.get_data())
    print(data)
    print('Model: ' + data['model'])
    print('Prompt: ' + data['prompt'])
    response = {'status': input('type status: '), 'message': input('type response: ')}
    response = json.dumps(response)
    return response, 200

if __name__ == '__main__':
    app.run()
