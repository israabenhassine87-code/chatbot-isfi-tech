# chatbot.py — commit B1 : historique uniquement
from openai import OpenAI
from config import OPENAI_API_KEY
messages = []
SYSTEM_PROMPT = (
    'Tu es un assistant expert en dépannage informatique. '
    'Pose des questions précises pour identifier la panne '
    'et propose des solutions claires étape par étape.'
)


def initialiser_historique():
    messages.clear()
    messages.append({'role': 'system', 'content': SYSTEM_PROMPT})


client = OpenAI(api_key=OPENAI_API_KEY)

def envoyer_message(texte_utilisateur):
    messages.append({'role': 'user', 'content': texte_utilisateur})
    try:
        reponse = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        contenu = reponse.choices[0].message.content
        messages.append({'role': 'assistant', 'content': contenu})
        return contenu
    except Exception as e:
        return f'Erreur API : {e}'
