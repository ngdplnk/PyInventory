# IMPORTS
import subprocess
import os
from tkinter import messagebox
import requests

# APPDATA PATH
APPDATA = os.environ.get("APPDATA")

# CHECK INTERNET CONNECTION
def check_internet_connection():
    try:
        requests.get("http://www.github.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

# DOWNLOAD UPDATED UPDATER FROM GITHUB
def download_file(url, destination):
    try:
        response = requests.get(url)
        with open(destination, 'wb') as file:
            file.write(response.content)
        
        updater_path = os.path.join(APPDATA, "TLSoftware", "PyInventory", "scripts", "updater.pyw")
        if os.path.exists(updater_path):
            subprocess.run(["python", updater_path], check=True, shell=False)
        else:
            main_path = os.path.join(APPDATA, "TLSoftware", "PyInventory", "main.pyw")
            # Verify if the program is installed
            if os.path.exists(main_path):
                # Run the program
                subprocess.run(["python", main_path], check=True, shell=False)
            else:
                # Show error message
                messagebox.showerror("Error", "El programa no está instalado en este equipo. Por favor, conéctate a internet para obtener la última versión disponible.")
    except Exception as e:
        main_path = os.path.join(APPDATA, "TLSoftware", "PyInventory", "main.pyw")
        # Verify if the program is installed
        if os.path.exists(main_path):
            # Run the program
            subprocess.run(["python", main_path], check=True, shell=False)
        else:
            # Show error message
            messagebox.showerror("Error", "El programa no está instalado en este equipo. Por favor, conéctate a internet para obtener la última versión disponible.")


# PATHS
updater_path = os.path.join(APPDATA, "TLSoftware", "PyInventory", "scripts", "updater.pyw")
main_path = os.path.join(APPDATA, "TLSoftware", "PyInventory", "main.pyw")

if check_internet_connection():
    download_file("https://raw.githubusercontent.com/ngdplnk/PyInventory/main/launcher/updater.pyw", updater_path)
else:
     # Verify if the program is installed
        if os.path.exists(main_path):
            # Run the program
            subprocess.run(["python", main_path], check=True, shell=False)
        else:
            # Show error message
            messagebox.showerror("Error", "El programa no está instalado en este equipo. Por favor, conéctate a internet para obtener la última versión disponible.")
