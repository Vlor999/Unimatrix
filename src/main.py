#!/usr/bin/env python3
import os
import sys
import subprocess
import curses
from terminal import main  # Assurez-vous que cela pointe vers votre fonction main dans terminal.py

# Fonction pour activer l'environnement virtuel
def activate_venv():
    venv_path = "/Users/adnet/Desktop/Projets/Perso/Unimatrix/env/bin"

    if sys.platform == "win32":
        python_exe = os.path.join(venv_path, "Scripts", "python.exe")
    else:
        python_exe = os.path.join(venv_path, "python3")
    
    if os.path.exists(python_exe):
        sys.executable = python_exe
        os.environ["VIRTUAL_ENV"] = venv_path
        os.environ["PATH"] = venv_path + os.pathsep + os.environ["PATH"]
        site_packages = os.path.join(os.path.dirname(venv_path), "lib", f"python{sys.version_info[0]}.{sys.version_info[1]}", "site-packages")
        sys.path.insert(0, site_packages)
    else:
        print("Erreur : l'environnement virtuel n'est pas trouvé.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    try:
        activate_venv()

        curses.wrapper(main)
    except KeyboardInterrupt:
        pass  
