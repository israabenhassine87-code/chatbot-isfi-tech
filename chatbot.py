# chatbot.py
import anthropic
from config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = (
    'Tu es un assistant expert en dépannage informatique. '
    'Pose des questions précises pour identifier la panne '
    'et propose des solutions claires étape par étape.'
)

messages = []

def initialiser_historique():
    messages.clear()

def envoyer_message(texte_utilisateur):
    messages.append({'role': 'user', 'content': texte_utilisateur})
    try:
        reponse = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=messages
        )
        contenu = reponse.content[0].text
        messages.append({'role': 'assistant', 'content': contenu})
        return contenu
    except Exception as e:
        return f'Erreur API : {e}'