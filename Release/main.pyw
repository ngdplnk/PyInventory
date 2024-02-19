import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Configurar el título de la ventana
root.title("¡Hola Mundo!")

# Crear una etiqueta con el mensaje
label = tk.Label(root, text="¡Hello world :)", padx=20, pady=20)

# Empaquetar la etiqueta en la ventana
label.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
