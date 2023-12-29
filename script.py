import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from customtkinter import *

class ImageMirrorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Espejar Imagen")

        self.image_path = None
        self.original_image = None
        self.mirrored_image = None
        self.tk_image = None  # Mantenemos una referencia al objeto PhotoImage
        self.image_is_mirrored = False  # Bandera para controlar si la imagen actual es la original o espejada

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        # Crear un contenedor Frame para los botones
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=3.3)

        self.select_button = CTkButton(button_frame, text="Seleccionar Imagen", font=("Helvetica", 12, "bold"), command=self.select_image)
        self.select_button.pack(side=tk.LEFT, padx=5)

        self.mirror_button = CTkButton(button_frame, text="Espejar Imagen", font=("Helvetica", 12, "bold"), command=self.mirror_image)
        self.mirror_button.pack(side=tk.LEFT, padx=5)

        self.save_button = CTkButton(button_frame, text="Guardar Imagen", font=("Helvetica", 12, "bold"), command=self.save_image)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = CTkButton(button_frame, text="Borrar Imagen", font=("Helvetica", 12, "bold"), command=self.delete_image)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.root.geometry("800x600")

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

        if file_path:
            self.image_path = file_path
            self.original_image = Image.open(self.image_path)
            self.image_is_mirrored = False
            self.display_image(self.original_image)

    def mirror_image(self):
        if self.original_image:
            if not self.image_is_mirrored:
                self.mirrored_image = self.original_image.transpose(Image.FLIP_LEFT_RIGHT)
                self.image_is_mirrored = True
            else:
                self.mirrored_image = self.original_image.copy()
                self.image_is_mirrored = False

            self.display_image(self.mirrored_image)

    def save_image(self):
        if self.mirrored_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                self.mirrored_image.save(save_path)

    def delete_image(self):
        if self.tk_image:
            self.tk_image = None
            self.image_label.configure(image=None)
            self.image_label.image = None
            self.image_label.pack_forget()

            self.image_path = None
            self.original_image = None
            self.mirrored_image = None
            self.image_is_mirrored = None
        

    def display_image(self, image):
        width, height = 760, 480 
        image.thumbnail((width, height))
        self.tk_image = ImageTk.PhotoImage(image)
        self.image_label.configure(image=self.tk_image)
        self.image_label.image = self.tk_image

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageMirrorApp(root)
    root.mainloop()
    