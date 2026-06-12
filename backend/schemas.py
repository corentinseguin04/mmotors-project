from pydantic import BaseModel


class VehicleBase(BaseModel):
    marque: str
    modele: str
    prix: int
    type_offre: str


class VehicleCreate(VehicleBase):
    pass


class Vehicle(VehicleBase):
    id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    nom: str
    email: str
    mot_de_passe: str
    role: str


class User(BaseModel):
    id: int
    nom: str
    email: str
    role: str

    class Config:
        from_attributes = True

        