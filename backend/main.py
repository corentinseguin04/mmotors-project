from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas

from database import engine
from database import SessionLocal
from fastapi import FastAPI, Depends, HTTPException
import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "Bienvenue sur l'API M-Motors"
    }


@app.post("/vehicles")
def create_vehicle(
    vehicle: schemas.VehicleCreate,
    db: Session = Depends(get_db)
):
    new_vehicle = models.Vehicle(
        marque=vehicle.marque,
        modele=vehicle.modele,
        prix=vehicle.prix,
        type_offre=vehicle.type_offre
    )

    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)

    return new_vehicle


@app.get("/vehicles")
def get_vehicles(
    db: Session = Depends(get_db)
):
    return db.query(models.Vehicle).all()

@app.post("/register")
def register_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")

    new_user = models.User(
        nom=user.nom,
        email=user.email,
        mot_de_passe=auth.hash_password(user.mot_de_passe),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Utilisateur créé avec succès",
        "user": {
            "id": new_user.id,
            "nom": new_user.nom,
            "email": new_user.email,
            "role": new_user.role
        }
    }


@app.post("/login")
def login_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Utilisateur introuvable")

    if not auth.verify_password(user.mot_de_passe, db_user.mot_de_passe):
        raise HTTPException(status_code=401, detail="Mot de passe incorrect")

    return {
        "message": "Connexion réussie",
        "user": {
            "id": db_user.id,
            "nom": db_user.nom,
            "email": db_user.email,
            "role": db_user.role
        }
    }