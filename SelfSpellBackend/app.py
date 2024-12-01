from flask import Flask, jsonify, request
from firebase import initialize_firebase
from models import Hobby

app = Flask(__name__)

# Initialize Firebase
initialize_firebase()

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_ref = Hobby.add_task(data)
    return jsonify({'id': task_ref.id, **data}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Hobby.get_all_tasks()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
