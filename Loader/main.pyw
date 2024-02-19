### PyInventory Program Loader and Updater ###
# This script is the main program loader and updater for PyInventory.
# It will check for updates and download them if needed.

# MODULES
import os
import sys
import requests
import subprocess
from tkinter import messagebox

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
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "Error al actualizar. Intentando usar versión local del programa.")
        # Get the program files path
        program_files_path = os.environ.get("APPDATA")

        # Install path
        install_path = os.path.join(program_files_path, "TLSoftware")
        
        # File name
        file_name = os.path.join(install_path, "main.pyw")
        
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
        file_url = "https://raw.githubusercontent.com/ngdplnk/PyInventory/main/Release/main.pyw"
        
        # Get the program files path
        program_files_path = os.environ.get("APPDATA")

        # Install path
        install_path = os.path.join(program_files_path, "TLSoftware")
        os.makedirs(install_path, exist_ok=True)
        
        # File name
        file_name = os.path.join(install_path, "main.pyw")
        
        # Download file from GitHub
        download_file(file_url, file_name)
        
        # Run the program
        subprocess.run(["python", file_name], check=True)
    else:
        # Get the program files path
        program_files_path = os.environ.get("APPDATA")

        # Install path
        install_path = os.path.join(program_files_path, "TLSoftware")
        
        # File name
        file_name = os.path.join(install_path, "main.pyw")

        # Verify if the program is installed
        if os.path.exists(file_name):
            # Run the program
            subprocess.run(["python", file_name], check=True)
        else:
            # Show error message
            messagebox.showerror("Error", "El programa no está instalado en este equipo. Por favor, conéctate a internet para obtener la última versión disponible.")

if __name__ == "__main__":
    main()