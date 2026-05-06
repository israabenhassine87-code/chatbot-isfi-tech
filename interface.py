from chatbot import envoyer_message, initialiser_historique

def lancer_interface():
    initialiser_historique()
    while True:
        saisie = input('Vous : ').strip()
        if not saisie:
            continue
        if saisie.lower() in ('quitter', 'exit', 'q'):
            print('Au revoir !')
            break
        reponse = envoyer_message(saisie)
        print()
        print('Assistant : ' + reponse)
        print('-' * 50)