from backend.models import Cheval
from backend.ranking import classer_chevaux

chevaux = [
    Cheval(
        numero=1,
        nom="Alpha",
        forme=9,
        regularite=8,
        distance=9,
        terrain=8,
        jockey=8,
        entraineur=8,
        valeur=9,
        corde=4,
        cote=7
    ),
    Cheval(
        numero=2,
        nom="Bravo",
        forme=8,
        regularite=8,
        distance=8,
        terrain=9,
        jockey=9,
        entraineur=8,
        valeur=8,
        corde=5,
        cote=8
    )
]

print(classer_chevaux(chevaux))
