from flask import Flask, jsonify
from src.repositories import RacaRepository

app = Flask(__name__)



@app.route("/racas", methods=["GET"])
def get_all_racas():
    racas = RacaRepository.find_all()
    return racas

@app.route("/racas_by_name", methods=["GET"])
def get_all_racas_by_name():
    racas = RacaRepository.find_all_names()
    return racas


if __name__ == '__main__':
    app.run(debug=True)