from backend.ranking import classer_chevaux

def generer_ticket(chevaux):

    classement = classer_chevaux(chevaux)

    return {

        "Base 1": classement[0],
        "Base 2": classement[1],

        "Chance 1": classement[2],
        "Chance 2": classement[3],
        "Chance 3": classement[4],

        "Outsider 1": classement[5],
        "Outsider 2": classement[6]

    }
