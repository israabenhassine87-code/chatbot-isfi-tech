# chatbot.py
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = (
    'Tu es un assistant expert en dépannage informatique. '
    'Pose des questions précises pour identifier la panne '
    'et propose des solutions claires étape par étape.'
)

messages = []

def initialiser_historique():
    messages.clear()
    messages.append({'role': 'system', 'content': SYSTEM_PROMPT})

def envoyer_message(texte_utilisateur):
    messages.append({'role': 'user', 'content': texte_utilisateur})
    try:
        reponse = client.chat.completions.create(
            model='llama-3.1-8b-instant',
            messages=messages
        )
        contenu = reponse.choices[0].message.content
        messages.append({'role': 'assistant', 'content': contenu})
        return contenu
    except Exception as e:
        return f'Erreur API : {e}'