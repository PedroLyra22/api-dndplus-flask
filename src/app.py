from flask import Flask

app = Flask(__name__)



@app.route("/racas", methods=["GET"])
def get_all_racas():
    racas = UserRepository.find_by_id(user_id)

    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    return jsonify({"error": "User not found"}), 404




if __name__ == '__main__':
    app.run(debug=True)