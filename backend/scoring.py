from backend.config import WEIGHTS

def calcul_indice(cheval):

    score = 0

    score += cheval.forme * WEIGHTS["forme"] / 20
    score += cheval.regularite * WEIGHTS["regularite"] / 15
    score += cheval.distance * WEIGHTS["distance"] / 10
    score += cheval.terrain * WEIGHTS["terrain"] / 10
    score += cheval.jockey * WEIGHTS["jockey"] / 10
    score += cheval.entraineur * WEIGHTS["entraineur"] / 10
    score += cheval.valeur * WEIGHTS["valeur"] / 10
    score += cheval.corde * WEIGHTS["corde"] / 5
    score += cheval.cote * WEIGHTS["cote"] / 10
    score += cheval.musique * WEIGHTS["musique"] / 10

    return round(score,2)
