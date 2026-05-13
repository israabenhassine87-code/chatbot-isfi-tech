# Chatbot ISFI Tech
Assistant de diagnostic de pannes informatiques — Interface web.
## Groupe
- Israa — Chef de projet & Backend Flask
- A — Configuration API Groq
- B — Logique Chatbot
- C — Interface Web HTML/CSS
## Lancer le projet
```bash
python3 -m venv .venv
source .venv/bin/activate # Windows : .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env # puis remplir GROQ_API_KEY
python app.py
```
Ouvrir http://127.0.0.1:5000 dans le navigateur.
## Evolution
v1 : prototype terminal (boucle console, Groq)
v2 : interface web Flask + HTML + CSS
