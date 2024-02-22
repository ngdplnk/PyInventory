# IMPORTS
import subprocess
import os
from tkinter import messagebox

# APPDATA PATH
APPDATA = os.environ.get("APPDATA")

# MODULE INSTALLER
def install_module(module):
    subprocess.check_call(["pip", "install", __package__])

# CHECK MODULES
def is_module_installed(module_name):
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

# CALL FOR "REQUESTS" MODULE CHECK
if not is_module_installed("requests"):
    install_module("requests")
else:
    pass

# PATH FOR LIBRARY UPDATER LOADER
lib_updater_path = os.path.join(APPDATA, "TLSoftware", "PyInventory", "scripts", "lib.pyw")

# TRY TO RUN LUL
try:
    subprocess.run(["python", lib_updater_path], check=True)
except subprocess.CalledProcessError:
    messagebox.showerror("Error", "No tienes los archivos mínimos necesarios para ejecutar el programa. Contáctate con el desarrollador del programa.")
