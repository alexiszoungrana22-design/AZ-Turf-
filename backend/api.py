from fastapi import APIRouter
from backend.models import Cheval
from backend.ranking import classer_chevaux
from backend.quinte import generer_ticket

router = APIRouter()

@router.get("/")
def home():
    return {
        "status": "OK",
        "message": "AZ Turf API opérationnelle"
    }

@router.post("/analyse")
def analyser_course(chevaux: list[Cheval]):
    classement = classer_chevaux(chevaux)
    ticket = generer_ticket(chevaux)

    return {
        "classement": classement,
        "ticket": ticket
    }
