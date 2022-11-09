import tkinter as tk


root = tk.Tk()

# colocar una etiqueta en la ventana raíz
message = tk.Label(root, text="Hello, World!")
message.pack()

# mantener la ventana mostrando
root.mainloop()