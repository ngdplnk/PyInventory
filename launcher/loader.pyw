import requests
import os
import subprocess
from tkinter import messagebox

APPDATA = os.environ.get("APPDATA")
PROGRAM_PATH = os.path.join(APPDATA, "TLSoftware", "PyInventory")
FILE_PATH = os.path.join(PROGRAM_PATH, "main.pyw")

os.makedirs(PROGRAM_PATH, exist_ok=True)
try:
    response = requests.get("https://raw.githubusercontent.com/ngdplnk/PyInventory/main/release/main.pyw")
    with open(FILE_PATH, 'wb') as file:
        file.write(response.content)
    subprocess.run(["python", FILE_PATH], shell=False)
except Exception:
    if os.path.isfile(FILE_PATH):
        subprocess.run(["python", FILE_PATH], shell=False)
    else:
        messagebox.showerror("Error", "Conéctate a internet para obtener la última versión del programa.")