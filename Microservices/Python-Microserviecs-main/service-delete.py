from flask import Flask, request, jsonify
import datetime

import data_user as us

app = Flask(__name__)

@app.route('/delete', methods=['POST'])

def login():
    try:
        username = request.form.get('username')
        _user = us.find_username(username)

        if _user:
            us.delete_user(username)
            return jsonify({'message': 'Username deleted successfully'}), 200
        else: 
            return jsonify({'message': 'Username Not Found'}), 404
    except:
        return jsonify({'message': 'Username not found.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1