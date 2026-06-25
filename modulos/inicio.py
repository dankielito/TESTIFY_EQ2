import tkinter as tk

def render_inicio_tab(parent_frame):
    # Título principal
    tk.Label(parent_frame, text="Inicio", font=("Helvetica", 28, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=30)
    
    # Instrucciones de inicio, si lees esto ola pero no ola de mar, ola de saludo
    tk.Label(parent_frame, text="👈 Selecciona un módulo en el menú lateral para comenzar a editar.", font=("Arial", 12, "italic"), bg="#ecf0f1", fg="#7f8c8d").pack(pady=30)