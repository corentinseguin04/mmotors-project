from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.session import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    marque = Column(String)
    modele = Column(String)
    prix = Column(Integer)
    type_offre = Column(String)

    dossiers = relationship(
        "Dossier",
        back_populates="vehicle"
    )