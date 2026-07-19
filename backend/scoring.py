from backend.config import WEIGHTS

def calcul_forme(musique: float):

    return round(musique * 10, 2)


def calcul_indice(cheval):

    score = (
        cheval.forme * WEIGHTS["forme"] / 20
        + cheval.regularite * WEIGHTS["regularite"] / 15
        + cheval.distance * WEIGHTS["distance"] / 10
        + cheval.terrain * WEIGHTS["terrain"] / 10
        + cheval.jockey * WEIGHTS["jockey"] / 10
        + cheval.entraineur * WEIGHTS["entraineur"] / 10
        + cheval.valeur * WEIGHTS["valeur"] / 10
        + cheval.corde * WEIGHTS["corde"] / 5
        + cheval.cote * WEIGHTS["cote"] / 10
        + calcul_forme(cheval.musique)
    )

    return round(score, 2)


def calcul_valeur_az(indice, cote):

    if cote <= 0:
        return indice

    return round(indice / cote, 2)
