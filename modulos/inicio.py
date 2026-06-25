import tkinter as tk

def render_inicio_tab(parent_frame):
    tk.Label(parent_frame, text="Inicio", font=("Helvetica", 28, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=30)
    tk.Label(parent_frame, text="Plantilla Maestra Activa:", font=("Arial", 14), bg="#ecf0f1", fg="#34495e").pack()

    card = tk.Frame(parent_frame, bg="white", bd=1, relief="ridge")
    card.pack(pady=20, ipadx=60, ipady=40)

    tk.Label(card, text="📄", font=("Arial", 50), bg="white", fg="#2b579a").pack()
    tk.Label(card, text="ETAPA_1.docx", font=("Arial", 18, "bold"), bg="white", fg="#333").pack(pady=10)
    
    tk.Label(card, text="Tamaño: 33 Páginas", font=("Arial", 11), bg="white", fg="#666").pack()
    tk.Label(card, text="Módulos: Acta, Interesados, Alcance, EDT, Dirección, Requerimientos", font=("Arial", 10, "italic"), bg="white", fg="#666").pack(pady=5)
    tk.Label(card, text="Directorio: /templates/ETAPA_1.docx", font=("Arial", 10), bg="white", fg="#999").pack(pady=10)

    tk.Label(parent_frame, text="👈 Selecciona un módulo en el menú lateral para comenzar a editar.", font=("Arial", 12, "italic"), bg="#ecf0f1", fg="#7f8c8d").pack(pady=30)