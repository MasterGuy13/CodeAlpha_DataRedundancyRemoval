import json
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE_FILE = 'database.json'

# Load or initialize database
def load_database():
    try:
        with open(DATABASE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_database(data):
    with open(DATABASE_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Check if entry is redundant
def is_redundant(entry, database):
    return entry in database

@app.route('/add', methods=['POST'])
def add_entry():
    new_entry = request.json
    database = load_database()

    if is_redundant(new_entry, database):
        return jsonify({'message': 'Redundant data. Entry not added.'}), 200
    else:
        database.append(new_entry)
        save_database(database)
        return jsonify({'message': 'Data added successfully!'}), 201

@app.route('/data', methods=['GET'])
def get_data():
    database = load_database()
    return jsonify(database)

if __name__ == '__main__':
    app.run(debug=True)
