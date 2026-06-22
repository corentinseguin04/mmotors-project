from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter(
    tags=["Authentification"]
)


@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email déjà utilisé"
        )

    new_user = User(
        nom=user.nom,
        email=user.email,
        mot_de_passe=hash_password(user.mot_de_passe),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Utilisateur créé avec succès"
    }


@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Utilisateur introuvable"
        )

    if not verify_password(
        user.mot_de_passe,
        db_user.mot_de_passe
    ):
        raise HTTPException(
            status_code=401,
            detail="Mot de passe incorrect"
        )

    access_token = create_access_token(
    data={
        "sub": db_user.email,
        "role": db_user.role
    }
)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": 3600
    }