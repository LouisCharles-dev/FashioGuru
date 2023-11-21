from flask import Flask, render_template, request, session, redirect, url_for
from fonction import find_size, BERT
from collections.abc import Mapping
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

#-----------------------------------------------Page d'acceuil-----------------------------------------------------------------

@app.route('/', methods=['POST', 'GET'])
def table():

    return render_template('table.html')

#-----------------------------------------------Page de prediction--------------------------------------------------------------

@app.route('/make_prediction', methods=['POST', 'GET'])
def make_prediction():

    return render_template('make_prediction.html')

#-----------------------------------------------Page de prompt--------------------------------------------------------------

@app.route('/prompt_prediction', methods=['POST', 'GET'])
def prompt_prediction():
    sexe = request.form['sexe']
    marque = request.form['marque']
    tour_taille = int(request.form['taille'])
    tour_poitrine = int(request.form['poitrine'])
    tour_hanche = int(request.form['hanche'])

    return render_template('prompt_prediction.html', recherche_taille=find_size(marque, sexe, tour_poitrine, tour_taille, tour_hanche))

#-----------------------------------------------Page de prompt--------------------------------------------------------------

@app.route('/prompt_result', methods=['POST', 'GET'])
def prompt_result():
    f = request.form['camenBert']
    picture_path = BERT(f)
    return render_template('prompt_result.html', picture_prompt=picture_path)
                           
#-----------------------------------------------Page de connection--------------------------------------------------------------

@app.route('/connection', methods=['POST', 'GET'])
def connection():
    return render_template('connection.html')

#------------------------------------------------Page de compte------------------------------------------------------------------

@app.route('/compte', methods=['POST', 'GET'])
def compte():
    if request.method == 'POST':
        session['utilisateur'] = request.form['email']
        session['mdp'] = request.form['mdp']
        session.permanent = True
        
    if 'utilisateur' in session:
        return render_template('compte.html')
    else:
        return redirect(url_for('connection'))
       
#-------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
