#!/usr/bin/env python3
"""
Script de déploiement pour PythonAnywhere
À exécuter sur votre compte PythonAnywhere après avoir cloné le projet
"""
import os
import sys
import subprocess

def run_command(command):
    print(f"Executing: {command}")
    subprocess.run(command, shell=True, check=True)

def main():
    # Configuration des informations utilisateur
    os.environ['GIT_COMMITTER_NAME'] = 'huber233'
    os.environ['GIT_COMMITTER_EMAIL'] = 'maxvignon195@gmail.com'
    
    # 1. Création et activation de l'environnement virtuel
    run_command("python3 -m venv venv")
    run_command("source venv/bin/activate")
    
    # 2. Installation des dépendances
    run_command("pip install -r requirements.txt")
    
    # 3. Configuration des variables d'environnement
    with open('.env') as f:
        env_vars = dict(
            line.strip().split('=', 1)
            for line in f
            if line.strip() and not line.startswith('#')
        )
    
    for key, value in env_vars.items():
        os.environ[key] = value
    
    # 4. Collecte des fichiers statiques
    run_command("python manage.py collectstatic --noinput")
    
    # 5. Application des migrations
    run_command("python manage.py migrate")
    
    # 6. Initialisation de la base de données
    run_command("python initialize_db.py")
    
    print("\nDéploiement terminé !")
    print("\nÉtapes suivantes :")
    print("1. Configurez votre application web dans l'interface PythonAnywhere")
    print("2. Définissez le chemin du virtualenv dans la configuration")
    print("3. Configurez le fichier WSGI")
    print("4. Redémarrez l'application web")

if __name__ == "__main__":
    main()
