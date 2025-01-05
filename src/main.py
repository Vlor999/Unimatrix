#! /usr/bin/env python3
import os
import sys
import subprocess
import curses
from terminal import main  # Assurez-vous que cela pointe vers votre fonction main dans terminal.py

# Chemin vers l'environnement virtuel
def activate_venv():
    # Déterminer si nous sommes sous Windows ou Linux/Mac
    if sys.platform == "win32":
        venv_bin = os.path.join(os.path.dirname(__file__), "../env/Scripts")
        python_exe = os.path.join(venv_bin, "python.exe")
    else:
        venv_bin = os.path.join(os.path.dirname(__file__), "../env/bin")
        python_exe = os.path.join(venv_bin, "python3")
    
    # Modifier les variables d'environnement pour utiliser l'environnement virtuel
    if os.path.exists(python_exe):
        # Modifier le chemin du python
        sys.executable = python_exe
        # Modifier les variables d'environnement pour inclure les binaires et les librairies de l'environnement virtuel
        os.environ["VIRTUAL_ENV"] = os.path.dirname(venv_bin)
        os.environ["PATH"] = venv_bin + os.pathsep + os.environ["PATH"]
        # Ajouter les librairies de l'environnement virtuel à sys.path
        site_packages = os.path.join(os.path.dirname(venv_bin), "lib", f"python{sys.version_info[0]}.{sys.version_info[1]}", "site-packages")
        sys.path.insert(0, site_packages)
    else:
        print("Erreur : l'environnement virtuel n'est pas trouvé.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    try:
        # Activer l'environnement virtuel
        activate_venv()

        # Lancer l'interface curses
        curses.wrapper(main)  # Utilise la fonction 'main' de 'terminal.py'
    except KeyboardInterrupt:
        pass  # Ignorer l'interruption par Ctrl+C pour éviter une fermeture brutale
