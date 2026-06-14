from flask import Flask, render_template, request, jsonify, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)


MONGO_URI = "mongodb+srv://tewarysoham_db_user:tewarysoham_db_user@sohammongo.ri8ohfw.mongodb.net/?appName=sohammongo"
client = MongoClient(MONGO_URI)


#new
#f1 changes
db = client['tutedude']
users_collection = db['tdmongo']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')

        if not username or not email:
            return jsonify({"message": "Missing username or email fields."}), 400

        user_data = {"username": username, "email": email}
        users_collection.insert_one(user_data)

    
        return jsonify({"redirect": url_for('success')}), 200

    except PyMongoError as e:
        
        return jsonify({"message": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
