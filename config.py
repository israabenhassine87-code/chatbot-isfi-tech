# config.py
import os
from dotenv import load_dotenv
load_dotenv()  # charge les variables depuis .env
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError('Clé API manquante. Vérifie ton fichier .env')
