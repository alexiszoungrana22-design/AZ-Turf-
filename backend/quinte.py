from backend.ranking import classer_chevaux

def generer_ticket(chevaux):
    classement = classer_chevaux(chevaux)

    return {
        "bases": classement[:2],
        "chances": classement[2:5],
        "outsiders": classement[5:7]
    }
