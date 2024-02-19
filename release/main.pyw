# PyInventory - A Python Inventory Manager #
# Version: CI-A.02.24 #

###################################

# IMPORTS
import tkinter as tk
import os
from tkinter import filedialog

# GLOBAL VARIABLES
global working
global working_name
global APPPATH

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

# MAIN MENU
def main():
  # Global variables
  global root
  global working
  global working_name
  global RUNNING
  global APPPATH
  
  # Check if the user is running the menu for the first time
  if not RUNNING:
    RUNNING = True
    root = tk.Tk()
    root.state("zoomed")
    try:
      root.iconbitmap(os.path.join(APPPATH, "assets", "icon.ico"))
    except tk.TclError:
      print("Icon not found")
    root.minsize(850, 500)

    # Set window title
    root.title("PyInventory - Main Menu")

    # Set BG
    root.configure(bg=BG_COLOR)

    # Main frame
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Title
    title_font = ("Arial", 20, "bold")
    title = tk.Label(frame, text="PyInventory", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
    title.grid(row=0, column=0, columnspan=5, pady=5)

    #Subtitle
    subtitle_text = "Welcome! Let's open an Excel file to start"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
    subtitle.grid(row=1, column=0, columnspan=5, pady=5)

    def openfile_menu():
      global working
      global working_name
      # Create a file dialog to select an existing .xlsx file
      file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
      
      if file_path:
        working = file_path
        working_name = os.path.basename(working)
        main()

    # "Add file" button
    add_button = tk.Button(frame, text="Open file", command=openfile_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    add_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')
  else:
    # Clear elements
    for widget in root.winfo_children():
      widget.destroy()
    
    # Set window title
    root.title("PyInventory - Main Menu")

    # Set BG
    root.configure(bg=BG_COLOR)

    # Main frame
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Title
    title_font = ("Arial", 20, "bold")
    title = tk.Label(frame, text="PyInventory", font=title_font, bg=BG_COLOR, fg=TXT_COLOR)
    title.grid(row=0, column=0, columnspan=5, pady=5)

    #Subtitle
    subtitle_text = f"You are working with {working_name}"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=BG_COLOR, fg=TXT_COLOR)
    subtitle.grid(row=1, column=0, columnspan=5, pady=5)
    
    def changefile_menu():
      global working
      global working_name
      # Create a file dialog to select an existing .xlsx file
      file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
      
      if file_path:
        working = file_path
        working_name = os.path.basename(working)
        main()

    # "Change file" button
    change_button = tk.Button(frame, text="Change file", command= changefile_menu, height=3, width=20, bg=BUTTON_COLOR, fg=BTNTXT_COLOR)
    change_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')

  root.mainloop()

########################
main()