######################################## PyInventory Launcher #######################################
################ This script is the main program loader and updater for PyInventory. ################
############# It will update the program from GitHub if there is an internet connection. ############
### If there is no internet connection, it will run the program with the latest version available. ##
################## If the program is not installed, it will show an error message. ##################
#####################################################################################################

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
            # Run the program
            subprocess.run(["python", file_name], check=True)
        else:
            # Show error message
            messagebox.showerror("Error", "El programa no está instalado en este equipo. Por favor, conéctate a internet para obtener la última versión disponible.")


# Main function
def main():
    # Call check_internet_connection function
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
        
        # Run the program
        subprocess.run(["python", file_name], check=True)
    else:
        # Get the program files path
        program_files_path = os.environ.get("APPDATA")

        # File path
        file_name = os.path.join(APPDATA, "TLSoftware", "PyInventory", "main.pyw")

        # Verify if the program is installed
        if os.path.exists(file_name):
            # Run the program
            subprocess.run(["python", file_name], check=True)
        else:
            # Show error message
            messagebox.showerror("Error", "El programa no está instalado en este equipo. Por favor, conéctate a internet para obtener la última versión disponible.")

if __name__ == "__main__":
    main()