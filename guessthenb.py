#TODO: Faire un jeu ou l'ont doit deviner le nombre choisi par l'ordinateur au hasard avec le moin de reponse possible.
import random

def guessthenumber():
    nb = random.randint(1, 20)
    count = 0
    soluce = None

    while soluce != nb:
        try:
            soluce = int(input('trouve le bon nombre entre 1 et 20 : '))
            count += 1

            if soluce == nb:
                print(f"Bravo tu as trouver le bon nombre en {count} fois")
            else:
                if soluce < nb:
                    print('trop petit')
                elif soluce > nb:
                    print('trop grand')
        except ValueError:
            print("Ta reponse est invalide, donne nous un nombre entier.")

guessthenumber()
