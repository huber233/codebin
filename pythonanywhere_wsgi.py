"""
Configuration WSGI pour PythonAnywhere
"""
import os
import sys
from pathlib import Path

# Chemin vers le projet sur PythonAnywhere
path = '/home/codingsite/codebin'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'codebin.settings'

# Lecture des variables d'environnement depuis .env
from dotenv import load_dotenv
env_path = Path(path) / '.env'
load_dotenv(env_path)

application = get_wsgi_application()
