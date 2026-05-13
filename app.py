# app.py — créer ce fichier
from flask import Flask, render_template, request, jsonify
from chatbot import envoyer_message, initialiser_historique

app = Flask(__name__)
@app.route('/')
def index():
    initialiser_historique()
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message_utilisateur = data.get('message', '')
    if not message_utilisateur:
        return jsonify({'reply': 'Message vide.'}), 400
    reponse = envoyer_message(message_utilisateur)
    return jsonify({'reply': reponse})

if __name__ == '__main__':
    app.run(debug=True)
