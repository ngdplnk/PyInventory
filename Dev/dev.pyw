# PyInventory - A Python Inventory Manager #
# Version: CI-B.01.24 #

###################################

# IMPORTS
import tkinter as tk
import os
from tkinter import filedialog

# GLOBAL VARIABLES
global RUNNING
global BG_COLOR
global TXT_COLOR
global BTNTXT_COLOR
global BUTTON_COLOR
global APPDATA
global APPFOLDER
global CONFPATH
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

# GET USEFUL PATHS
APPDATA = os.getenv("APPDATA")
APPFOLDER = os.path.join(APPDATA, "PyInventory")
CONFPATH = os.path.join(APPFOLDER, "pyinv.cfg")

# LOAD CONFIG FILE
def load_config_file():
  cfg = {}
  try:
    with open(CONFPATH, 'r') as file:
      for line in file:
        line = line.strip()
        if line and not line.startswith('#'):
          key, value = line.split('=')
          cfg[key.strip()] = value.strip()
  except FileNotFoundError:
    return {}
  return cfg

# SAVE CONFIG FILE
def save_config_file(cfg):
  with open(CONFPATH, 'w') as file:
    for key, value in cfg.items():
      file.write(f'{key}={value}\n')

# CREATE CONFIG FILE
def create_config_file(with_folder=False, parameter="running-file", value=""):
  if with_folder:
    os.makedirs(APPFOLDER)
  with open(CONFPATH, 'w') as file:
    file.write(f'{parameter}={value}\n')

# CHECK CONFIG STATUS
def check_config_status(config="default"):
  global working
  global working_name
  cfg = load_config_file()
  if os.path.exists(APPFOLDER):
    if os.path.exists(CONFPATH):
      if config == "asdasd":
        cfg[""] = "true"
        save_config_file(cfg)
        # Here should be the custom function
      elif config == "running-file":
        try:
          if cfg["running-file"] == "":
            return False
          else:
            try:
              saved = cfg["running-file"]
              working =  saved.strip('"')
              working_name = working.split("/")
              working_name = working_name[-1]
              working_name = working_name.strip('.xlsx')
              return True
            except ValueError:
              saved = cfg["running-file"]
              working = saved.strip('"')
              working_name = working.split("/")
              working_name = working_name[-1]
              working_name = working_name.strip('.xlsx')
              return True
        except KeyError:
          return False
      else:
        main()
    else:
      create_config_file()
      main()
  else:
    create_config_file(True)
    main()

# CHANGE FILE MENU
def change_file_menu():
  global working
  global working_name
  

  def openfile_menu():
    global working
    global working_name
    # Create a file dialog to select an existing .xlsx file
    file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
      
    if file_path:
      # Update the 'running-file' config parameter
      cfg = load_config_file()
      cfg["running-file"] = file_path
      save_config_file(cfg)
      working_name = file_path.split('/')
      working_name = working_name[-1]
      working_name = working_name.strip('.xlsx')
      working = file_path
      main()

  openfile_menu()

# MAIN MENU
def main():
  # Global variables
  global root
  global working
  global working_name
  global RUNNING
  global JUST_STARTED
  
  # Check if the user is running the menu for the first time
  if not RUNNING:
    RUNNING = True
    JUST_STARTED = True
    root = tk.Tk()
    root.state("zoomed")
    try:
      root.iconbitmap("assets\\icon.ico")
    except tk.TclError:
      pass
    root.minsize(850, 500)
  else:
    pass

  # Set window title
  root.title("PyInventory - Main Menu")

  # Clear window
  for widget in root.winfo_children():
    widget.destroy()

  # Set BG
  root.configure(bg=BG_COLOR)

  # Main frame
  frame = tk.Frame(root, bg=BG_COLOR)
  frame.place(relx=0.5, rely=0.5, anchor='center')

  # Title
  title_font = ("Arial", 30, "bold")
  title = tk.Label(frame, text="PyInventory - A Python Inventory Manager", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
  title.grid(row=0, column=0, columnspan=5, pady=5)

  if not check_config_status("running-file"):
    #Subtitle
    subtitle_text = "Welcome to PyInventory!\n Let's open a file to work with it"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
    subtitle.grid(row=1, column=0, columnspan=5, pady=5)

    def openfile_menu():
      global JUST_STARTED
      # Create a file dialog to select an existing .xlsx file
      file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
      
      if file_path:
        # Update the 'running-file' config parameter
        cfg = load_config_file()
        cfg["running-file"] = file_path
        save_config_file(cfg)
        JUST_STARTED = False
        main()

    # "Add file" button
    add_button = tk.Button(frame, text="Open file", command=openfile_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    add_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')
  
  else:
    if JUST_STARTED:
      JUST_STARTED = False
      #Subtitle
      subtitle_text = f"You were working with {working_name} the last time you used PyInventory"
      subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
      subtitle.grid(row=1, column=0, columnspan=5, pady=5)
    else:
      #Subtitle
      subtitle_text = f"You are working with {working_name}"
      subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
      subtitle.grid(row=1, column=0, columnspan=5, pady=5)
    
    # "Change file" button
    change_button = tk.Button(frame, text="Change file", command=change_file_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    change_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')

    # "Exit" button
    exit_button = tk.Button(frame, text="Exit", command=root.destroy, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    exit_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

  root.mainloop()

########################
check_config_status()