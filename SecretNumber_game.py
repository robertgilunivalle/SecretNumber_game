import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def check_guess():
    try:
        guess = int(entry.get())
        global attempts
        attempts += 1
        
        if guess < secret_number:
            result_label.config(text="🔼 Más alto. Inténtalo de nuevo.", foreground="#1E88E5")
        elif guess > secret_number:
            result_label.config(text="🔽 Más bajo. Inténtalo de nuevo.", foreground="#D32F2F")
        else:
            messagebox.showinfo("🎉 ¡Felicidades!", f"Adivinaste el número {secret_number} en {attempts} intentos.")
            root.quit()
        
        if attempts == 2:
            parity = "par" if secret_number % 2 == 0 else "impar"
            hint_label.config(text=f"💡 Pista: El número secreto es {parity}.")
        
    except ValueError:
        result_label.config(text="⚠️ Ingresa un número válido.", foreground="#FF5722")

def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="🔢 He seleccionado un número entre 1 y 100. ¡Intenta adivinarlo!", foreground="black")
    hint_label.config(text="")
    entry.delete(0, tk.END)

# Configuración inicial
root = tk.Tk()
root.title("🎯 Adivina el Número")
#root.geometry("600x450")  
root.resizable(False, False)
root.configure(bg="#E3F2FD")  # Fondo suave azul claro

# Estilos
font_title = ("Arial", 20, "bold")
font_text = ("Arial", 16)

# Título del juego
title_label = tk.Label(root, text="¡Bienvenido al juego de adivinar el número! 🔢", font=font_title, bg="#E3F2FD", fg="#0D47A1")
title_label.pack(pady=15)

# Instrucción
tk.Label(root, text="Ingresa un número entre 1 y 100:", font=font_text, bg="#E3F2FD").pack()

# Entrada de usuario
entry = tk.Entry(root, font=font_text, width=10, justify="center", relief="solid", borderwidth=2)
entry.pack(pady=5)

# Botones en un Frame
button_frame = tk.Frame(root, bg="#E3F2FD")
button_frame.pack(pady=10)

def button_hover(e):
    e.widget.config(bg="#1565C0")

def button_leave(e):
    e.widget.config(bg=e.widget.default_bg)

guess_button = tk.Button(button_frame, text="🎲 Adivinar", command=check_guess, font=font_text, bg="#1976D2", fg="white", width=12)
guess_button.default_bg = "#1976D2"
guess_button.pack(side=tk.LEFT, padx=5)
guess_button.bind("<Enter>", button_hover)
guess_button.bind("<Leave>", button_leave)

restart_button = tk.Button(button_frame, text="🔄 Reiniciar", command=restart_game, font=font_text, bg="#FBC02D", fg="black", width=12)
restart_button.default_bg = "#FBC02D"
restart_button.pack(side=tk.LEFT, padx=5)
restart_button.bind("<Enter>", button_hover)
restart_button.bind("<Leave>", button_leave)

exit_button = tk.Button(button_frame, text="❌ Salir", command=root.quit, font=font_text, bg="#D32F2F", fg="white", width=12)
exit_button.default_bg = "#D32F2F"
exit_button.pack(side=tk.LEFT, padx=5)
exit_button.bind("<Enter>", button_hover)
exit_button.bind("<Leave>", button_leave)

# Etiqueta de resultados
result_label = tk.Label(root, text="🔢 He seleccionado un número entre 1 y 100. ¡Intenta adivinarlo!", font=font_text, bg="#E3F2FD", fg="black")
result_label.pack(pady=15)

# Etiqueta de pistas
hint_label = tk.Label(root, text="", font=font_text, fg="#303F9F", bg="#E3F2FD")
hint_label.pack()

# Inicializar juego
secret_number = random.randint(1, 100)
attempts = 0

root.mainloop()
