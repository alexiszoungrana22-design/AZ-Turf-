from fastapi import APIRouter

from backend.models import Cheval

from backend.ranking import classer_chevaux

from backend.quinte import generer_ticket

router=APIRouter()

@router.get("/")
def home():

    return{
        "status":"OK",
        "application":"AZ Turf"
    }

@router.post("/analyse")

def analyse(chevaux:list[Cheval]):

    classement=classer_chevaux(chevaux)

    ticket=generer_ticket(chevaux)

    return{

        "classement":classement,

        "ticket":ticket

    }
