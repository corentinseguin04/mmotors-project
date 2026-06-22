from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    email = Column(String, unique=True, index=True)
    mot_de_passe = Column(String)
    role = Column(String)

    dossiers = relationship(
        "Dossier",
        back_populates="user"
    )