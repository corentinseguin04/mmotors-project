# 🚗 M-Motors API

## 📖 Présentation

M-Motors API est une application backend développée avec FastAPI permettant la gestion des utilisateurs, des véhicules et des dossiers clients.

Le projet a été réalisé dans le cadre de ma formation en développement informatique afin de mettre en pratique le développement d'une API REST sécurisée, l'utilisation d'une base de données relationnelle et le déploiement d'une application dans le cloud.

---

## 🎯 Objectifs du projet

L'application permet :

- l'inscription et la connexion des utilisateurs ;
- la gestion des véhicules ;
- la gestion des dossiers clients ;
- la gestion des rôles utilisateurs ;
- l'administration de l'application ;
- le déploiement d'une API sécurisée en production.

---

## 🛠️ Technologies utilisées

### Backend
- Python 3
- FastAPI
- SQLAlchemy
- Pydantic

### Base de données
- PostgreSQL

### Sécurité
- JWT (JSON Web Token)
- Passlib (bcrypt)

### Déploiement
- Render
- GitHub

### Documentation
- Swagger UI

---

## 📁 Architecture du projet

```text
MMOTORS-PROJECT
├── backend
│   ├── app
│   │   ├── core
│   │   ├── database
│   │   ├── models
│   │   ├── routes
│   │   ├── schemas
│   │   └── services
│   ├── tests
│   ├── main.py
│   ├── requirements.txt
│   └── .env
├── frontend
└── README.md
```

### Description des dossiers

- core : configuration et sécurité JWT
- database : connexion PostgreSQL et gestion des sessions
- models : modèles SQLAlchemy
- schemas : validation des données avec Pydantic
- routes : endpoints de l'API
- services : logique métier
- tests : tests de l'application

---

## ✅ Fonctionnalités

### Authentification
- Inscription d'un utilisateur
- Connexion avec JWT
- Gestion des rôles

### Gestion des véhicules
- Création d'un véhicule
- Consultation des véhicules
- Modification d'un véhicule
- Suppression d'un véhicule

### Gestion des dossiers
- Création d'un dossier
- Validation d'un dossier
- Refus d'un dossier

### Utilisateurs
- Consultation du profil utilisateur
- Consultation des dossiers de l'utilisateur

### Administration
- Liste des utilisateurs
- Statistiques de l'application

---

## 🌐 Principales routes

### Authentification
- POST /register
- POST /login

### Véhicules
- GET /vehicles
- POST /vehicles
- PUT /vehicles/{vehicle_id}
- DELETE /vehicles/{vehicle_id}

### Dossiers
- GET /dossiers
- POST /dossiers
- PUT /dossiers/{dossier_id}/validate
- PUT /dossiers/{dossier_id}/refuse

### Utilisateurs
- GET /me
- GET /me/dossiers

### Administration
- GET /admin/users
- GET /admin/stats

---

## 🚀 Déploiement

API déployée sur Render :

https://mmotors-project.onrender.com

Documentation Swagger :

https://mmotors-project.onrender.com/docs

---

## 💻 Installation locale

Cloner le projet :

```bash
git clone https://github.com/corentinseguin04/mmotors-project.git
```

Entrer dans le dossier :

```bash
cd backend
```

Créer l'environnement virtuel :

```bash
python -m venv venv
```

Activer l'environnement :

```bash
venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer le serveur :

```bash
python -m uvicorn main:app --reload
```

---

## 🔐 Variables d'environnement

Créer un fichier `.env` :

```env
SECRET_KEY=VotreCleSecrete
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=postgresql+psycopg2://...
```

---

## 👤 Compte de démonstration

Administrateur :

Email : admin@mmotors.fr

Mot de passe : admin123

---

## 📚 Conclusion

Ce projet m'a permis de mettre en pratique :

- le développement d'une API REST avec FastAPI ;
- la conception d'une architecture backend modulaire ;
- la sécurisation d'une application avec JWT ;
- l'utilisation de PostgreSQL avec SQLAlchemy ;
- le déploiement d'une application sur le cloud avec Render ;
- l'utilisation de Git et GitHub pour le versionnement.

Ce projet représente une application backend complète, sécurisée et déployée en production.