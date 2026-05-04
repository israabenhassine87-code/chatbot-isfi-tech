# Chatbot ISFI Tech
Assistant de diagnostic de pannes informatiques en ligne de commande.
## Groupe
- Israa — Chef de projet & intégration
- A — Configuration API
- B — Logique chatbot
- C — Interface console
## Lancer le projet
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env # puis remplir avec votre clé OpenAI
python main.py
```