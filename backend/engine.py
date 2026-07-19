from backend.scoring import calcul_indice, calcul_valeur_az

class AZEngine:

    def analyser(self, chevaux):

        resultat = []

        for cheval in chevaux:

            indice = calcul_indice(cheval)
            valeur = calcul_valeur_az(indice, cheval.cote)

            resultat.append({
                "numero": cheval.numero,
                "nom": cheval.nom,
                "indiceAZ": indice,
                "valeurAZ": valeur
            })

        resultat.sort(
            key=lambda x: x["indiceAZ"],
            reverse=True
        )

        return resultat
