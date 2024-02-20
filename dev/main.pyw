############################################
# PyInventory - A Python Inventory Manager #
############################################
############ Version: CI-C.02.24 ###########
############################################


## ATTRIBUTIONS ##
# Icon made by Vectorslab from www.flaticon.com
"https://www.flaticon.es/icono-gratis/aglutinante_5953385"


# IMPORTS
import tkinter as tk
import os
from tkinter import filedialog

# GLOBAL VARIABLES
global working
global working_name

# VARIABLES
RUNNING = False
BG_COLOR = "#3F88C5"
TXT_COLOR = "#FFFFFF"
BTNTXT_COLOR = "#000000"
BUTTON_COLOR = "#FFFFFF"
working = None
working_name = None

# GET APP PATH
APPPATH = os.path.join(os.getenv("APPDATA"), "TLSoftware", "PyInventory")

# CONSULT MENU
def consult_menu():
  global working
  global working_name
  global root

  # Clear elements
  for widget in root.winfo_children():
    widget.destroy()

  # Set window title
  root.title("Librería N-Cosas - Consulta de Productos")

  # Set BG
  root.configure(bg=BG_COLOR)

  # Main frame
  frame = tk.Frame(root, bg=BG_COLOR)
  frame.place(relx=0.5, rely=0.5, anchor='center')

  # Title
  title_font = ("Arial", 20, "bold")
  title = tk.Label(frame, text="Consulta de Productos", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
  title.grid(row=0, column=0, columnspan=5, pady=5)

  #Subtitle
  subtitle_text = f"Elije una opción para consultar productos en el archivo {working_name}"
  subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
  subtitle.grid(row=1, column=0, columnspan=5, pady=5)

  # "Por ID" button
  byid_button = tk.Button(frame, text="Por ID", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  byid_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Por Nombre" button
  byname_button = tk.Button(frame, text="Por Nombre", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  byname_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Por Categoría" button
  bycategory_button = tk.Button(frame, text="Por Categoría", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  bycategory_button.grid(row=4, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Por Precio" button
  byprice_button = tk.Button(frame, text="Por Precio", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  byprice_button.grid(row=5, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Por Existencia" button
  bystock_button = tk.Button(frame, text="Por Existencia", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  bystock_button.grid(row=6, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Volver Atrás" button
  back_button = tk.Button(frame, text="Volver Atrás", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  back_button.grid(row=7, column=1, columnspan=3, pady=5, sticky='nsew')

  root.mainloop()

# ADD MENU
def add_menu():
  global working
  global working_name
  global root

  # Clear elements
  for widget in root.winfo_children():
    widget.destroy()

  # Set window title
  root.title("Librería N-Cosas - Agregar Productos")

  # Set BG
  root.configure(bg=BG_COLOR)

  # Main frame
  frame = tk.Frame(root, bg=BG_COLOR)
  frame.place(relx=0.5, rely=0.5, anchor='center')

  # Title
  title_font = ("Arial", 20, "bold")
  title = tk.Label(frame, text="Agregar Productos", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
  title.grid(row=0, column=0, columnspan=5, pady=5)

  #Subtitle
  subtitle_text = f"Elije una opción para agregar productos al archivo {working_name}"
  subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
  subtitle.grid(row=1, column=0, columnspan=5, pady=5)

  # "Agregar existencias" button
  addstock_button = tk.Button(frame, text="Agregar existencias", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  addstock_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Agregar productos nuevos" button
  addnew_button = tk.Button(frame, text="Agregar productos nuevos", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  addnew_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Volver Atrás" button
  back_button = tk.Button(frame, text="Volver Atrás", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  back_button.grid(row=4, column=1, columnspan=3, pady=5, sticky='nsew')

  root.mainloop()

# DELETE MENU
def delete_menu():
  global working
  global working_name
  global root

  # Clear elements
  for widget in root.winfo_children():
    widget.destroy()

  # Set window title
  root.title("Librería N-Cosas - Eliminar Productos")

  # Set BG
  root.configure(bg=BG_COLOR)

  # Main frame
  frame = tk.Frame(root, bg=BG_COLOR)
  frame.place(relx=0.5, rely=0.5, anchor='center')

  # Title
  title_font = ("Arial", 20, "bold")
  title = tk.Label(frame, text="Eliminar Productos", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
  title.grid(row=0, column=0, columnspan=5, pady=5)

  #Subtitle
  subtitle_text = f"Elije una opción para eliminar productos del archivo {working_name}"
  subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
  subtitle.grid(row=1, column=0, columnspan=5, pady=5)

  # "Eliminar existencias" button
  deletestock_button = tk.Button(frame, text="Eliminar existencias", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  deletestock_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Eliminar productos" button
  deletenew_button = tk.Button(frame, text="Eliminar productos", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  deletenew_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Volver Atrás" button
  back_button = tk.Button(frame, text="Volver Atrás", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  back_button.grid(row=4, column=1, columnspan=3, pady=5, sticky='nsew')

  root.mainloop()

# EXIT MENU
def exit_menu():
  global root
  root.destroy()

# MAIN MENU
def main():
  # Global variables
  global root
  global working
  global working_name
  global RUNNING
  
  # Check if the user is running the menu for the first time
  if not RUNNING:
    RUNNING = True
    root = tk.Tk()
    root.state("zoomed")
    try:
      root.iconbitmap(os.path.join(APPPATH, "assets", "icon.ico"))
    except tk.TclError:
      pass
    root.minsize(850, 500)

    # Set window title
    root.title("Librería N-Cosas - Menú Principal")

    # Set BG
    root.configure(bg=BG_COLOR)

    # Main frame
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Title
    title_font = ("Arial", 20, "bold")
    title = tk.Label(frame, text="Librería N-Cosas", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
    title.grid(row=0, column=0, columnspan=5, pady=5)

    #Subtitle
    subtitle_text = "Hola! Abre un archivo de Excel para comenzar"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
    subtitle.grid(row=1, column=0, columnspan=5, pady=5)

    def openfile_menu():
      global working
      global working_name
      # Create a file dialog to select an existing .xlsx file
      file_path = filedialog.askopenfilename(filetypes=[('Archivos Excel', '*.xlsx')])
      
      if file_path:
        working = file_path
        working_name = os.path.basename(working)
        main()

    # "Add file" button
    add_button = tk.Button(frame, text="Abrir Archivo", command=openfile_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    add_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')
  else:
    # Clear elements
    for widget in root.winfo_children():
      widget.destroy()
    
    # Set window title
    root.title("Librería N-Cosas - Menú Principal")

    # Set BG
    root.configure(bg=BG_COLOR)

    # Main frame
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Title
    title_font = ("Arial", 20, "bold")
    title = tk.Label(frame, text="Librería N-Cosas", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
    title.grid(row=0, column=0, columnspan=5, pady=5)

    #Subtitle
    subtitle_text = f"Estás trabajando con: {working_name}"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
    subtitle.grid(row=1, column=0, columnspan=5, pady=5)
    
    def changefile_menu():
      global working
      global working_name
      # Create a file dialog to select an existing .xlsx file
      file_path = filedialog.askopenfilename(filetypes=[('Archivos Excel', '*.xlsx')])
      
      if file_path:
        working = file_path
        working_name = os.path.basename(working)
        main()

    # "Consulta de productos" button
    consult_button = tk.Button(frame, text="Consulta de productos", command=consult_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    consult_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')

    # "Agregar productos" button
    add_button = tk.Button(frame, text="Agregar productos", command=add_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    add_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

    # "Eliminar productos" button
    delete_button = tk.Button(frame, text="Eliminar productos", command=delete_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    delete_button.grid(row=4, column=1, columnspan=3, pady=5, sticky='nsew')

    # "Abrir otro archivo" button
    change_button = tk.Button(frame, text="Abrir otro archivo", command=changefile_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    change_button.grid(row=5, column=1, columnspan=3, pady=5, sticky='nsew')

    # "Salir" button
    exit_button = tk.Button(frame, text="Salir", command=exit_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    exit_button.grid(row=6, column=1, columnspan=3, pady=5, sticky='nsew')


  root.mainloop()

########################
main()