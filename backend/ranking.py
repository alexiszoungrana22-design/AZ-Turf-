from backend.scoring import calcul_indice

def classer_chevaux(chevaux):
    classement = []

    for cheval in chevaux:
        classement.append({
            "numero": cheval.numero,
            "nom": cheval.nom,
            "indice": calcul_indice(cheval)
        })

    classement.sort(key=lambda x: x["indice"], reverse=True)

    return classement
