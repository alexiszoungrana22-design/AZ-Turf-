from backend.scoring import calcul_indice, calcul_valeur_az

def niveau_confiance(indice):

    if indice >= 90:
        return "★★★★★"
    elif indice >= 80:
        return "★★★★☆"
    elif indice >= 70:
        return "★★★☆☆"
    elif indice >= 60:
        return "★★☆☆☆"
    else:
        return "★☆☆☆☆"


def classer_chevaux(chevaux):

    classement = []

    for cheval in chevaux:

        indice = calcul_indice(cheval)

        valeur = calcul_valeur_az(indice, cheval.cote)

        classement.append({

            "numero": cheval.numero,
            "nom": cheval.nom,
            "indiceAZ": indice,
            "valeurAZ": valeur,
            "confiance": niveau_confiance(indice)

        })

    classement.sort(
        key=lambda x: x["indiceAZ"],
        reverse=True
    )

    return classement
    classement.sort(
        key=lambda x: x["indiceAZ"],
        reverse=True
    )

    return classement
