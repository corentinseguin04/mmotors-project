from pydantic import BaseModel


class UserCreate(BaseModel):
    nom: str
    email: str
    mot_de_passe: str
    role: str


class UserLogin(BaseModel):
    email: str
    mot_de_passe: str