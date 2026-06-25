import tkinter as tk
from .datos_hitos import lista_hitos_default

vars_hitos = []

def render_hitos_subtab(parent_frame):
    canvas = tk.Canvas(parent_frame, bg="#ecf0f1", highlightthickness=0)
    scrollbar = tk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#ecf0f1")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scroll_frame, text="Incluir", bg="#ecf0f1", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(scroll_frame, text="Descripción del Hito", bg="#ecf0f1", font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w", padx=5, pady=5)

    global vars_hitos
    vars_hitos = [] # Reset al renderizar
    for i, texto in enumerate(lista_hitos_default):
        v_chk = tk.BooleanVar(value=True)
        v_text = tk.StringVar(value=texto)
        tk.Checkbutton(scroll_frame, variable=v_chk, bg="#ecf0f1").grid(row=i+1, column=0)
        tk.Entry(scroll_frame, textvariable=v_text, width=80).grid(row=i+1, column=1, sticky="w", pady=2, padx=5)
        vars_hitos.append({"activo": v_chk, "texto": v_text})

def get_hitos_seleccionados():
    return [{"texto": i["texto"].get()} for i in vars_hitos if i["activo"].get()]