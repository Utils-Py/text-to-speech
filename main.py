import tkinter as tk
from tkinter import ttk
from gtts import gTTS
import pygame
from tkinter import messagebox
from tkinter import filedialog

# Funció per convertir text a veu i desar-lo en un fitxer MP3
def convertir_a_veu():
    if texto := texto_entrada.get():
        try:
            tts = gTTS(texto, lang='ca')
            if ruta_desti := filedialog.asksaveasfilename(
                defaultextension=".mp3", filetypes=[("Arxius MP3", "*.mp3")]
            ):
            
                if ruta_desti:
                    tts.save(ruta_desti)
                    messagebox.showinfo("Èxit", f"El text s'ha convertit a veu i s'ha desat com a {ruta_desti}.")
                else:
                    messagebox.showinfo("Cancel·lat", "La conversió ha estat cancel·lada.")
        except Exception as e:
            messagebox.showerror("Error", f"S'ha produït un error: {str(e)}")
    else:
        messagebox.showerror("Error", "Introdueix un text per convertir a veu.")

# Crear la finestra principal
finestra = tk.Tk()
finestra.title("Convertir Text a Veu")

# Crear una etiqueta
etiqueta = ttk.Label(finestra, text="Introdueix el text:")
etiqueta.pack(pady=10)

# Crear una caixa d'entrada de text
texto_entrada = ttk.Entry(finestra, width=40)
texto_entrada.pack(pady=10)

# Crear un botó per iniciar la conversió
boton_convertir = ttk.Button(finestra, text="Convertir a Veu", command=convertir_a_veu)
boton_convertir.pack(pady=10)

# Iniciar el bucle principal de l'aplicació
finestra.mainloop()
