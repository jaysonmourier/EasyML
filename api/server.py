from flask import Flask, jsonify, request, make_response
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
    result = ''
    suite = False

    file_content = 'USE ./api/data/data.' + key + '.csv\n'

    if key is not None and cmd_lines is not None:  
        suite  = True
        file_content += cmd_lines
       
        with open('./commands/cmd.' + key + '.dsl', 'w') as f:
            f.write(file_content)
      
        input = './commands/cmd.' + key + '.dsl'
        output = "./models/model." + key + ".csv"

        try:
            args = ['python', main_app, "-f", input, "-o", output] # TODO: Ajouter les lignes de commande 
            subprocess.run(args)
        except Exception as e:
            # suite = False
            result = str(e)
            

    response = make_response(jsonify(result), 200) if suite else make_response('', 500)
    response.headers['Content-Type'] = 'application/json'
    return response
    

# LANCEMENT DU SERVER 
if __name__ == '__main__':
    app.run(debug=True)
