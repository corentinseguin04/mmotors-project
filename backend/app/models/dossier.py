from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.session import Base


class Dossier(Base):
    __tablename__ = "dossiers"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    type_demande = Column(String)
    statut = Column(String, default="en_attente")

    user = relationship(
        "User",
        back_populates="dossiers"
    )

    vehicle = relationship(
        "Vehicle",
        back_populates="dossiers"
    )