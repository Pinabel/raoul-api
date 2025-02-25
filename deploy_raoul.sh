#!/bin/bash

# Vérification des dépendances
echo "🔍 Vérification des dépendances..."
if ! command -v git &> /dev/null; then
    echo "❌ Git n'est pas installé. Installe-le et relance ce script."
    exit 1
fi
if ! command -v pip &> /dev/null; then
    echo "❌ Pip n'est pas installé. Installe-le et relance ce script."
    exit 1
fi
if ! command -v gunicorn &> /dev/null; then
    echo "❌ Gunicorn n'est pas installé. Installation en cours..."
    pip install gunicorn
fi

echo "🚀 Préparation du projet pour Render..."

# Clonage du repo ou initialisation
if [ ! -d "raoul-api" ]; then
    git clone https://github.com/ton-utilisateur/raoul-api.git
    cd raoul-api
else
    cd raoul-api
    git pull origin main
fi

# Création du fichier requirements.txt
echo "Flask\ngunicorn\nnumpy" > requirements.txt

# Création du fichier Procfile
echo "web: gunicorn -w 4 -b 0.0.0.0:10000 app:app" > Procfile

# Initialisation du dépôt Git
if [ ! -d ".git" ]; then
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/ton-utilisateur/raoul-api.git
fi

# Push des fichiers
git add .
git commit -m "Mise à jour automatique par script"
git push -u origin main

echo "✅ Projet mis à jour sur GitHub. Maintenant, va sur Render et déploie ton app en 2 clics !"
