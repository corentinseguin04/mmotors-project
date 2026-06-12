from sqlalchemy import Column, Integer, String
from database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    marque = Column(String)
    modele = Column(String)
    prix = Column(Integer)
    type_offre = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    email = Column(String, unique=True, index=True)
    mot_de_passe = Column(String)
    role = Column(String)

class Dossier(Base):
    __tablename__ = "dossiers"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String)
    vehicle_id = Column(Integer)
    type_demande = Column(String)
    statut = Column(String, default="en_attente")