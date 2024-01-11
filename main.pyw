# PyInventory - A Python Inventory Manager #
# Version: CI-A.01.24 #

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
def create_config_file(with_folder=False, parameter="saved-files", value=""):
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
      elif config == "saved-files":
        try:
          if cfg["saved-files"] == "":
            return False
          else:
            try:
              saved = cfg["saved-files"]
              saved = saved.split("<:>")
              working =  saved[-1].strip('"')
              working_name = working.split("/")
              working_name = working_name[-1]
              working_name = working_name.strip('.xlsx')
              return True
            except ValueError:
              saved = cfg["saved-files"]
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
  # Set window title
  root.title("PyInventory - Change file")

  # Clear window
  for widget in root.winfo_children():
    widget.destroy()
  
  # Main frame
  frame = tk.Frame(root, bg=BG_COLOR)
  frame.place(relx=0.5, rely=0.5, anchor='center')

  # Title
  title_font = ("Arial", 30, "bold")
  title = tk.Label(frame, text="Change file", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
  title.grid(row=0, column=0, columnspan=5, pady=5)

  # Subtitle
  subtitle_text = f"You are working with {working_name}"
  subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
  subtitle.grid(row=1, column=0, columnspan=5, pady=5)

  # Load config file
  cfg = load_config_file()

  # Select file function
  def select_file(event):
    global working
    global working_name
    # Get selected line index
    index = listbox.curselection()[0]
    # Get the line's text
    selected_file = listbox.get(index)
    # Update working file and name
    working_name = selected_file
    working = cfg["saved-files"].split('<:>')[index]
    change_file_menu()

  # Create listbox
  listbox = tk.Listbox(frame)
  listbox.grid(row=2, column=0, columnspan=5, pady=5)

  # Populate listbox with files
  for file in cfg["saved-files"].split('<:>'):
    file = file.split('/')
    file = file[-1]
    file = file.strip('.xlsx')
    listbox.insert(tk.END, file.strip())

  # Bind select event
  listbox.bind('<<ListboxSelect>>', select_file)

  def addfile_menu():
    global working
    global working_name
    # Create a file dialog to select an existing .xlsx file
    file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
      
    if file_path:
      # Update the 'saved-files' config parameter
      cfg = load_config_file()
      cfg["saved-files"] = f"{cfg['saved-files']}<:>{file_path}"
      save_config_file(cfg)
      working_name = file_path.split('/')
      working_name = working_name[-1]
      working_name = working_name.strip('.xlsx')
      working = file_path
      change_file_menu()

  # "Add file" button
  add_button = tk.Button(frame, text="Add file", command=addfile_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  add_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Back" button
  back_button = tk.Button(frame, text="Back", command=main, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
  back_button.grid(row=4, column=1, columnspan=3, pady=5, sticky='nsew')


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

  if not check_config_status("saved-files"):
    #Subtitle
    subtitle_text = "No files saved, you need to add at least one file to work with"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
    subtitle.grid(row=1, column=0, columnspan=5, pady=5)

    def addfile_menu():
      global JUST_STARTED
      # Create a file dialog to select an existing .xlsx file
      file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
      
      if file_path:
        # Update the 'saved-files' config parameter
        cfg = load_config_file()
        cfg["saved-files"] = file_path
        save_config_file(cfg)
        JUST_STARTED = False
        main()

    # "Add file" button
    add_button = tk.Button(frame, text="Add file", command=addfile_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
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