from pydantic import BaseModel


class VehicleCreate(BaseModel):
    marque: str
    modele: str
    prix: int
    type_offre: str