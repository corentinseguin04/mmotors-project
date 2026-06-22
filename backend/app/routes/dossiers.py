from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.dossier import Dossier
from app.models.user import User
from app.models.vehicle import Vehicle
from app.schemas.dossier import DossierCreate
from app.core.security import (
    get_current_user,
    require_admin
)

router = APIRouter(
    tags=["Dossiers"]
)


@router.get("/dossiers")
def get_dossiers(
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    return db.query(Dossier).all()


@router.post("/dossiers")
def create_dossier(
    dossier: DossierCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    user = db.query(User).filter(
        User.email == current_user["email"]
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur introuvable"
        )

    vehicle = db.query(Vehicle).filter(
        Vehicle.id == dossier.vehicle_id
    ).first()

    if not vehicle:
        raise HTTPException(
            status_code=404,
            detail="Véhicule introuvable"
        )

    new_dossier = Dossier(
        user_id=user.id,
        vehicle_id=dossier.vehicle_id,
        type_demande=dossier.type_demande,
        statut="en_attente"
    )

    db.add(new_dossier)
    db.commit()
    db.refresh(new_dossier)

    return new_dossier


@router.put("/dossiers/{dossier_id}/validate")
def validate_dossier(
    dossier_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    dossier = db.query(Dossier).filter(
        Dossier.id == dossier_id
    ).first()

    if not dossier:
        raise HTTPException(
            status_code=404,
            detail="Dossier introuvable"
        )

    dossier.statut = "validé"

    db.commit()
    db.refresh(dossier)

    return dossier


@router.put("/dossiers/{dossier_id}/refuse")
def refuse_dossier(
    dossier_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    dossier = db.query(Dossier).filter(
        Dossier.id == dossier_id
    ).first()

    if not dossier:
        raise HTTPException(
            status_code=404,
            detail="Dossier introuvable"
        )

    dossier.statut = "refusé"

    db.commit()
    db.refresh(dossier)

    return dossier