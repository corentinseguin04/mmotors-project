from fastapi import FastAPI

from app.database.session import engine, Base
from app.models import User, Vehicle, Dossier

from app.routes.auth import router as auth_router
from app.routes.vehicles import router as vehicle_router
from app.routes.dossiers import router as dossier_router
from app.routes.users import router as user_router
from app.routes.admin import router as admin_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API M-Motors",
    description="API de gestion des véhicules, utilisateurs et dossiers M-Motors",
    version="2.0.0"
)

app.include_router(auth_router)
app.include_router(vehicle_router)
app.include_router(dossier_router)
app.include_router(user_router)
app.include_router(admin_router)


@app.get("/", tags=["Accueil"])
def home():
    return {
        "message": "Bienvenue sur l'API M-Motors"
    }