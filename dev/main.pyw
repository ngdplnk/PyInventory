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
import pandas as pd
import os
from tkinter import filedialog

# GLOBAL VARIABLES
global working, working_name

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

# THEME CHANGING FUNCTION
def change_theme():
  global BG_COLOR
  global TXT_COLOR
  global BTNTXT_COLOR
  global BUTTON_COLOR
  if BG_COLOR == "#3F88C5":
    BG_COLOR = "#1A1A1A"
    TXT_COLOR = "#FFFFFF"
    BTNTXT_COLOR = "#000000"
    BUTTON_COLOR = "#FFFFFF"
  else:
    BG_COLOR = "#3F88C5"
    TXT_COLOR = "#FFFFFF"
    BTNTXT_COLOR = "#000000"
    BUTTON_COLOR = "#FFFFFF"
  main()

# CONSULT MENU
def consult_menu():
  global working, working_name, working_sheet, root

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

  # Function to show the search by category menu
  def consult_by_category():
    global working, working_sheet, root

    # Clear elements
    for widget in root.winfo_children():
        widget.destroy()

    # Set window title
    root.title("Librería N-Cosas - Consulta por Categoría")

    # Main frame
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Title
    title_font = ("Arial", 20, "bold")
    title = tk.Label(frame, text="Consulta por Categoría", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
    title.grid(row=0, column=0, columnspan=8, pady=5)

    # Sheet selector dropdown
    sheet_label = tk.Label(frame, text="Estás consultando en la hoja:", font=("Arial", 12), bg=BG_COLOR, fg=TXT_COLOR)
    sheet_label.grid(row=1, column=0, columnspan=8, pady=5)

    # Create a StringVar to hold the selected sheet name
    working_sheet = tk.StringVar()
    working_sheet.set(sheet_names[0])

    # Create the dropdown with the sheet names
    sheet_dropdown = tk.OptionMenu(frame, working_sheet, *sheet_names)
    sheet_dropdown.config(bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    sheet_dropdown.grid(row=2, column=0, columnspan=8, pady=5)

    # Function to search for products by category
    def search():
      # Get the selected category from the entry field
      category = selected_category.get()
      # Get the selected sheet from the dropdown menu
      sheet_name = working_sheet.get()
      # Read the selected sheet into a DataFrame
      df = pd.read_excel(working, sheet_name=sheet_name)
      # Filter the DataFrame by the category column
      result = df[df['COD.'] == category]
      # Sort the results by product name
      result = result.sort_values(by='ART.')
      # Clear previous results
      result_listbox.delete(0, tk.END)
      # Display the filtered results
      for index, row in result.iterrows():
        result_listbox.insert(tk.END, f"{row['ART.']} - {row['DESCRIPCIÓN']} - {row['MARCAS']}")
        # Insert additional columns as needed

    # Get unique categories from the Excel file
    sheet_name = working_sheet.get()
    df = pd.read_excel(working, sheet_name=sheet_name)
    unique_categories = df['COD.'].unique()

    # Category Label
    category_label = tk.Label(frame, text="Seleccione la categoría:", font=("Arial", 12), bg=BG_COLOR, fg=TXT_COLOR)
    category_label.grid(row=3, column=0, columnspan=2, pady=5)

    # Category Dropdown
    selected_category = tk.StringVar()
    selected_category.set(unique_categories[0])
    category_dropdown = tk.OptionMenu(frame, selected_category, *unique_categories)
    category_dropdown.config(bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    category_dropdown.grid(row=3, column=2, columnspan=3, pady=5)

    # Search Button
    search_button = tk.Button(frame, text="Buscar", command=search, height=2, width=10, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    search_button.grid(row=3, column=5, columnspan=2, pady=5, padx=5)

    # Result Listbox and Scrollbar
    result_frame = tk.Frame(frame, bg=BG_COLOR)
    result_frame.grid(row=4, column=0, columnspan=8, pady=5, sticky='nsew')
    scrollbar = tk.Scrollbar(result_frame, orient=tk.VERTICAL)
    result_listbox = tk.Listbox(result_frame, yscrollcommand=scrollbar.set, font=("Arial", 12), bg=BG_COLOR, fg=TXT_COLOR)
    scrollbar.config(command=result_listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    result_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Back Button
    back_button = tk.Button(frame, text="Volver Atrás", command=consult_menu, height=2, width=10, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    back_button.grid(row=5, column=0, columnspan=8, pady=5)

  # "Por Categoría" button
  bycategory_button = tk.Button(frame, text="Consultar por Categoría", command=consult_by_category, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  bycategory_button.grid(row=1, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Por Nombre" button
  byname_button = tk.Button(frame, text="Consultar por Nombre", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  byname_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Por Marca" button
  bycategory_button = tk.Button(frame, text="Consultar por Marca", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  bycategory_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Por Existencia (Unidades)" button
  byunits_button = tk.Button(frame, text="Consultar por Existencia (Unidades)", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  byunits_button.grid(row=4, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Por Existencia" button
  bystock_button = tk.Button(frame, text="Consultar por Existencia (Cajas)", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  bystock_button.grid(row=5, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Por Precio" button
  byprice_button = tk.Button(frame, text="Consultar por Precio", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  byprice_button.grid(row=6, column=1, columnspan=3, pady=5, sticky='nsew')

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
  global xls
  global sheet_names
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

    # "Abrir Archivo" button
    add_button = tk.Button(frame, text="Abrir Archivo", command=openfile_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    add_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')

    # "Cambiar Tema" button
    change_button = tk.Button(frame, text="Cambiar Tema", command=change_theme, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    change_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

    # "Salir" button
    exit_button = tk.Button(frame, text="Salir", command=exit_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    exit_button.grid(row=4, column=1, columnspan=3, pady=5, sticky='nsew')

  else:
    if working == None:
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
      
      # "Abrir Archivo" button
      add_button = tk.Button(frame, text="Abrir Archivo", command=openfile_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
      add_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')
      
      # "Cambiar Tema" button
      change_button = tk.Button(frame, text="Cambiar Tema", command=change_theme, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
      change_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

      # "Salir" button
      exit_button = tk.Button(frame, text="Salir", command=exit_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
      exit_button.grid(row=4, column=1, columnspan=3, pady=5, sticky='nsew')

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
      
      # Load the Excel file
      xls = pd.ExcelFile(working)

      # Get the sheet names
      sheet_names = xls.sheet_names

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

      # "Cambiar Tema" button
      change_button = tk.Button(frame, text="Cambiar Tema", command=change_theme, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
      change_button.grid(row=6, column=1, columnspan=3, pady=5, sticky='nsew')

      # "Salir" button
      exit_button = tk.Button(frame, text="Salir", command=exit_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
      exit_button.grid(row=7, column=1, columnspan=3, pady=5, sticky='nsew')


  root.mainloop()

########################
main()