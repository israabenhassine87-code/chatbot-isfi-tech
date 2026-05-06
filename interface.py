# interface.py — commit C1
def lancer_interface():
    while True:
        saisie = input('Vous : ').strip()
        if saisie.lower() in ('quitter', 'exit', 'q'):
            print('Au revoir !')
            break