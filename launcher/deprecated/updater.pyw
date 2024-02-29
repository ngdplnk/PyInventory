# MODULES
import os
import requests
import subprocess
from tkinter import messagebox

# APPDATA PATH
APPDATA = os.environ.get("APPDATA")

# Check internet connection
def check_internet_connection():
    try:
        requests.get("http://www.github.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False
    
# MODULE INSTALLER
def install_module(module):
    # Create a STARTUPINFO object
    startupinfo = subprocess.STARTUPINFO()

    # Set the use show window flag
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    # Set the window show state to hidden
    startupinfo.wShowWindow = subprocess.SW_HIDE
    try:
        subprocess.run(["pip", "install", module], startupinfo=startupinfo, shell=False)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Error al instalar módulo. Intentando usar módulo ya instalado.")

# CHECK MODULES
def is_module_installed(module_name):
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

# Update program from GitHub
def download_file(url, destination):
    try:
        response = requests.get(url)
        with open(destination, 'wb') as file:
            file.write(response.content)
        
        response = requests.get("https://raw.githubusercontent.com/ngdplnk/PyInventory/main/icon.ico")
        with open(os.path.join(APPDATA, "TLSoftware", "PyInventory", "assets", "icon.ico"), 'wb') as file:
            file.write(response.content)
    except Exception as e:
        messagebox.showerror("Error", "Error al actualizar. Intentando usar versión local del programa.")

        # File path
        file_name = os.path.join(APPDATA, "TLSoftware", "PyInventory", "main.pyw")
        
        # Verify if the program is installed
        if os.path.exists(file_name):
            # Create a STARTUPINFO object
            startupinfo = subprocess.STARTUPINFO()

            # Set the use show window flag
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            # Set the window show state to hidden
            startupinfo.wShowWindow = subprocess.SW_HIDE

            # Run the program
            subprocess.run(["python", file_name], startupinfo=startupinfo, check=True, shell=False)
        else:
            # Show error message
            messagebox.showerror("Error", "El programa no está instalado en este equipo. Por favor, conéctate a internet para obtener la última versión disponible.")

# Check modules
if not is_module_installed("openpyxl"):
    openpyxl_module = False
else:
    openpyxl_module = True
if not is_module_installed("pandas"):
    pandas_module = False
else:
    pandas_module = True
# What to do if theres internet connection or not
if check_internet_connection():
    # GitHub URL
    file_url = "https://raw.githubusercontent.com/ngdplnk/PyInventory/main/release/main.pyw"

    # Install path and file name
    install_name = os.path.join(APPDATA, "TLSoftware", "PyInventory")
    assets_folder = os.path.join(install_name, "assets")
    os.makedirs(assets_folder, exist_ok=True)
        
    file_name = os.path.join(install_name, "main.pyw")

    # Download file from GitHub
    download_file(file_url, file_name)

    # Install modules
    if not openpyxl_module:
        install_module("openpyxl")
    if not pandas_module:
        install_module("pandas")
    
    # Create a STARTUPINFO object
    startupinfo = subprocess.STARTUPINFO()

    # Set the use show window flag
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    # Set the window show state to hidden
    startupinfo.wShowWindow = subprocess.SW_HIDE

    # Run the program
    subprocess.run(["python", file_name], startupinfo=startupinfo, check=True, shell=False)
else:
    # Check if all the modules are installed
    if not openpyxl_module or not pandas_module:
        messagebox.showerror("Error", "No tienes acceso a internet y no tienes instalados los módulos necesarios. Por favor, conéctate a internet y reinicia el programa.")
    else:
        # File path
        file_name = os.path.join(APPDATA, "TLSoftware", "PyInventory", "main.pyw")

        # Verify if the program is installed
        if os.path.exists(file_name):
            # Create a STARTUPINFO object
            startupinfo = subprocess.STARTUPINFO()

            # Set the use show window flag
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            # Set the window show state to hidden
            startupinfo.wShowWindow = subprocess.SW_HIDE

            # Run the program
            subprocess.run(["python", file_name], startupinfo=startupinfo, check=True, shell=False)
        else:
            # Show error message
            messagebox.showerror("Error", "El programa no está instalado en este equipo. Por favor, conéctate a internet para obtener la última versión disponible.")
