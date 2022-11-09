import tkinter as tk


root = tk.Tk()
root.title('Hello_world')

# colocar una etiqueta en la ventana raíz
message = tk.Label(root, text="Hello, World!")
message.pack()
root.geometry('600x400+50+50')


# mantener la ventana mostrando
root.mainloop()