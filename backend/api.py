from backend.engine import AZEngine
from fastapi import APIRouter
from backend.models import Cheval
from backend.ranking import classer_chevaux
from backend.quinte import generer_ticket

router = APIRouter()

@router.get("/")
def accueil():
    return {
        "message": "Bienvenue sur AZ Turf",
        "version": "2.0"
    }

@router.post("/analyse")
def analyse(chevaux: list[Cheval]):

    classement = classer_chevaux(chevaux)

    ticket = generer_ticket(chevaux)

    return {

        "classement": classement,

        "ticketAZ": ticket

    }
