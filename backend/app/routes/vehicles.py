from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate
from app.core.security import require_admin

router = APIRouter(
    tags=["Véhicules"]
)


@router.get("/vehicles")
def get_vehicles(db: Session = Depends(get_db)):
    return db.query(Vehicle).all()


@router.post("/vehicles")
def create_vehicle(
    vehicle: VehicleCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    new_vehicle = Vehicle(
        marque=vehicle.marque,
        modele=vehicle.modele,
        prix=vehicle.prix,
        type_offre=vehicle.type_offre
    )

    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)

    return new_vehicle


@router.put("/vehicles/{vehicle_id}")
def update_vehicle(
    vehicle_id: int,
    vehicle: VehicleCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    db_vehicle = db.query(Vehicle).filter(
        Vehicle.id == vehicle_id
    ).first()

    if not db_vehicle:
        raise HTTPException(
            status_code=404,
            detail="Véhicule introuvable"
        )

    db_vehicle.marque = vehicle.marque
    db_vehicle.modele = vehicle.modele
    db_vehicle.prix = vehicle.prix
    db_vehicle.type_offre = vehicle.type_offre

    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle


@router.delete("/vehicles/{vehicle_id}")
def delete_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    db_vehicle = db.query(Vehicle).filter(
        Vehicle.id == vehicle_id
    ).first()

    if not db_vehicle:
        raise HTTPException(
            status_code=404,
            detail="Véhicule introuvable"
        )

    db.delete(db_vehicle)
    db.commit()

    return {
        "message": "Véhicule supprimé avec succès"
    }