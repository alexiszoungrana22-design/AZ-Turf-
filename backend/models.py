from pydantic import BaseModel

class Cheval(BaseModel):
    numero: int
    nom: str
    forme: float
    regularite: float
    distance: float
    terrain: float
    jockey: float
    entraineur: float
    valeur: float
    corde: float
    cote: float
