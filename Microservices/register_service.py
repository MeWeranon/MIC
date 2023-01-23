from  flask import Flask,request,jsonify
import user_data as us

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    user = request.form.get('username')
    passwd = request.form.get('password')

    if (us._find_user(user)):
        return ({"Msg": "Username does exist!"}),401
    else:
        new_data = {"user": user, "passwd":passwd}
        us._add_user(new_data)
        return ({"Msg": "Your can register"}), 200


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)