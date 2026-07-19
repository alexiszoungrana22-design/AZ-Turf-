from backend.engine import AZEngine
from fastapi import APIRouter
from backend.models import Cheval
from backend.ranking import classer_chevaux
from backend.quinte import generer_ticket


@router.post("/analyse")
def analyse(chevaux: list[Cheval]):

    moteur = AZEngine()

    classement = moteur.analyser(chevaux)

    return {
        "classement": classement
    }
