import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    try:
        guess = int(entry.get())
        global attempts
        attempts += 1
        
        if guess < secret_number:
            result_label.config(text="Más alto. Inténtalo de nuevo.")
        elif guess > secret_number:
            result_label.config(text="Más bajo. Inténtalo de nuevo.")
        else:
            messagebox.showinfo("¡Felicidades!", f"Adivinaste el número {secret_number} en {attempts} intentos.")
            root.quit()
        
        if attempts == 2:
            parity = "par" if secret_number % 2 == 0 else "impar"
            hint_label.config(text=f"Pista: El número secreto es {parity}.")
        
    except ValueError:
        result_label.config(text="Por favor, ingresa un número válido.")

def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="He seleccionado un número entre 1 y 100. ¡Intenta adivinarlo!")
    hint_label.config(text="")
    entry.delete(0, tk.END)

# Configuración inicial
root = tk.Tk()
root.title("Adivina el Número")
root.geometry("400x300")  # Tamaño fijo de la ventana
root.resizable(False, False)  # Evitar que cambie de tamaño

secret_number = random.randint(1, 100)
attempts = 0

tk.Label(root, text="¡Bienvenido al juego de adivinar el número!").pack()
tk.Label(root, text="Ingresa un número entre 1 y 100:").pack()
entry = tk.Entry(root)
entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

guess_button = tk.Button(button_frame, text="Adivinar", command=check_guess)
guess_button.pack(side=tk.LEFT, padx=5)

restart_button = tk.Button(button_frame, text="Reiniciar", command=restart_game)
restart_button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="He seleccionado un número entre 1 y 100. ¡Intenta adivinarlo!")
result_label.pack()

hint_label = tk.Label(root, text="", fg="blue")
hint_label.pack()

root.mainloop()