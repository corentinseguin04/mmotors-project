from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.models.dossier import Dossier
from app.core.security import get_current_user

router = APIRouter(
    tags=["Utilisateurs"]
)


@router.get("/me")
def get_me(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    user = db.query(User).filter(
        User.email == current_user["email"]
    ).first()

    return user


@router.get("/me/dossiers")
def get_my_dossiers(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    user = db.query(User).filter(
        User.email == current_user["email"]
    ).first()

    dossiers = db.query(Dossier).filter(
        Dossier.user_id == user.id
    ).all()

    return dossiers