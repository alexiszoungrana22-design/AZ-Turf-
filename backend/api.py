from fastapi import APIRouter
from backend.models import Cheval
from backend.engine import AZEngine

router = APIRouter()

@router.post("/analyse")
def analyse(chevaux: list[Cheval]):
    moteur = AZEngine()
    classement = moteur.analyser(chevaux)

    return {
        "classement": classement
    }
