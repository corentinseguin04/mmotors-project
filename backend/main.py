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

@app.post("/dossiers")
def create_dossier(
    dossier: schemas.DossierCreate,
    db: Session = Depends(get_db)
):
    new_dossier = models.Dossier(
        user_email=dossier.user_email,
        vehicle_id=dossier.vehicle_id,
        type_demande=dossier.type_demande,
        statut="en_attente"
    )

    db.add(new_dossier)
    db.commit()
    db.refresh(new_dossier)

    return new_dossier


@app.get("/dossiers")
def get_dossiers(
    db: Session = Depends(get_db)
):
    return db.query(models.Dossier).all()


@app.put("/dossiers/{dossier_id}/validate")
def validate_dossier(
    dossier_id: int,
    db: Session = Depends(get_db)
):
    dossier = db.query(models.Dossier).filter(
        models.Dossier.id == dossier_id
    ).first()

    if not dossier:
        raise HTTPException(status_code=404, detail="Dossier introuvable")

    dossier.statut = "validé"
    db.commit()
    db.refresh(dossier)

    return dossier


@app.put("/dossiers/{dossier_id}/refuse")
def refuse_dossier(
    dossier_id: int,
    db: Session = Depends(get_db)
):
    dossier = db.query(models.Dossier).filter(
        models.Dossier.id == dossier_id
    ).first()

    if not dossier:
        raise HTTPException(status_code=404, detail="Dossier introuvable")

    dossier.statut = "refusé"
    db.commit()
    db.refresh(dossier)

    return dossier

@app.put("/vehicles/{vehicle_id}")
def update_vehicle(
    vehicle_id: int,
    vehicle: schemas.VehicleCreate,
    db: Session = Depends(get_db)
):
    db_vehicle = db.query(models.Vehicle).filter(
        models.Vehicle.id == vehicle_id
    ).first()

    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Véhicule introuvable")

    db_vehicle.marque = vehicle.marque
    db_vehicle.modele = vehicle.modele
    db_vehicle.prix = vehicle.prix
    db_vehicle.type_offre = vehicle.type_offre

    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle


@app.delete("/vehicles/{vehicle_id}")
def delete_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db)
):
    db_vehicle = db.query(models.Vehicle).filter(
        models.Vehicle.id == vehicle_id
    ).first()

    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Véhicule introuvable")

    db.delete(db_vehicle)
    db.commit()

    return {
        "message": "Véhicule supprimé avec succès"
    }