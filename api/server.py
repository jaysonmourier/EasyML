import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

dataCsv = None
cmdLines = None

# Enregistrer les données csv 
@app.route('/api/save-data', methods=['POST'])
def save_data():
    global dataCsv
    dataCsv = pd.read_csv(request.files['file'])
    print(dataCsv.head)
    return jsonify(dataCsv.head().to_json(orient='records')), 200

# Enregistrer les lignes de commande 
@app.route('/api/save-command', methods=['POST'])
def post_data():
    global cmdLines
    json = request.get_json()
    cmdLines = json['command']
    return jsonify(json['command']), 200

# LANCEMENT DU SERVER 

if __name__ == '__main__':
    app.run(debug=True)
