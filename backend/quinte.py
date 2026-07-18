from backend.ranking import classer_chevaux

def generer_ticket(chevaux):

    classement = classer_chevaux(chevaux)

    return {

        "bases": classement[:2],

        "chances": classement[2:5],

        "outsiders": classement[5:7],

        "favori": classement[0],

        "indice_max": classement[0]["indiceAZ"]

    }
