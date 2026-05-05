# chatbot.py — commit B1 : historique uniquement
messages = []
SYSTEM_PROMPT = (
    'Tu es un assistant expert en dépannage informatique. '
    'Pose des questions précises pour identifier la panne '
    'et propose des solutions claires étape par étape.'
)
def initialiser_historique():
    messages.clear()
    messages.append({'role': 'system', 'content': SYSTEM_PROMPT})
