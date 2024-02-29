# IMPORTS
import subprocess
import os
from tkinter import messagebox

# APPDATA PATH
APPDATA = os.environ.get("APPDATA")

# MODULE INSTALLER
def install_module(module):
    try:
        # Create a STARTUPINFO object
        startupinfo = subprocess.STARTUPINFO()

        # Set the use show window flag
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        # Set the window show state to hidden
        startupinfo.wShowWindow = subprocess.SW_HIDE
        
        # Install module
        subprocess.check_call(["pip", "install", module], startupinfo=startupinfo, shell=False)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Necesitas tener internet al menos por esta vez para instalar los recursos necesarios.")

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
    # Create a STARTUPINFO object
    startupinfo = subprocess.STARTUPINFO()

    # Set the use show window flag
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    # Set the window show state to hidden
    startupinfo.wShowWindow = subprocess.SW_HIDE
    
    # Run the updater updater
    subprocess.run(["python", lib_updater_path], startupinfo=startupinfo, check=True, shell=False)
except subprocess.CalledProcessError:
    messagebox.showerror("Error", "No tienes los archivos mínimos necesarios para ejecutar el programa. Contáctate con el desarrollador del programa.")
