from flask import Flask, jsonify, request
import pandas as pd
import uuid
import subprocess

app = Flask(__name__)

main_app = "../app.py"
data_csv = None
cmd_lines = None
key = None

# Enregistrer les données csv 
@app.route('/api/save-data', methods=['POST'])
def save_data():
    global data_csv, key
    suite = False

    if 'file' in request.files:
        suite = True
        key = str(uuid.uuid4())
        file = request.files['file']
        file.save('./data/data.' + key + '.csv')
    
    return jsonify({"key": key}) if suite else ('', 500)


# Enregistrer les lignes de 
# Récupérer les résultats 
@app.route('/api/save-command', methods=['POST'])
def post_data():
    global main_app, cmd_lines, key

    key = request.get_json()['key']
    cmd_lines = request.get_json()['command']
    result = None
    suite = False

    if key is not None and cmd_lines is not None:  
        suite  = True
        output = "./data/models/model." + key + ".csv"
        try:
            args = [main_app, "-f", cmd_lines, "-o", output] # TODO: Ajouter les lignes de commande 
        except Exception:
            suite = False

    return jsonify(result), 200 if suite else ('', 500)

# Récupérer les résultats 
# @app.route('api/get-results')
# def get_results(): 
#     return None

# # Récupérer le rapport Pdf 
# def get_report():
#     return None



# LANCEMENT DU SERVER 
if __name__ == '__main__':
    app.run(debug=True)
