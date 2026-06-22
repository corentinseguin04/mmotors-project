from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.models.vehicle import Vehicle
from app.models.dossier import Dossier
from app.core.security import require_admin

router = APIRouter(
    prefix="/admin",
    tags=["Administration"]
)


@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    return db.query(User).all()


@router.get("/stats")
def get_stats(
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    return {
        "utilisateurs": db.query(User).count(),
        "vehicules": db.query(Vehicle).count(),
        "dossiers": db.query(Dossier).count(),
        "dossiers_en_attente":
            db.query(Dossier)
            .filter(Dossier.statut == "en_attente")
            .count(),
        "dossiers_valides":
            db.query(Dossier)
            .filter(Dossier.statut == "validé")
            .count(),
        "dossiers_refuses":
            db.query(Dossier)
            .filter(Dossier.statut == "refusé")
            .count()
    }