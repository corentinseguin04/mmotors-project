from pydantic import BaseModel


class DossierCreate(BaseModel):
    vehicle_id: int
    type_demande: str