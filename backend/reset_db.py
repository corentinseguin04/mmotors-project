from app.database.session import Base, engine
from app.models import User, Vehicle, Dossier

print("Suppression des tables...")
Base.metadata.drop_all(bind=engine)

print("Création des tables...")
Base.metadata.create_all(bind=engine)

print("Base de données réinitialisée avec succès.")