import tkinter as tk
from .datos_acuerdos import lista_acuerdos_default

vars_acuerdos = []

def render_acuerdos_subtab(parent_frame):
    canvas = tk.Canvas(parent_frame, bg="#ecf0f1", highlightthickness=0)
    scrollbar = tk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#ecf0f1")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scroll_frame, text="Incluir", bg="#ecf0f1", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(scroll_frame, text="Cant.", bg="#ecf0f1", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(scroll_frame, text="Descripción", bg="#ecf0f1", font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w", padx=5, pady=5)

    vcmd_int = (parent_frame.register(lambda P: P.isdigit() or P == ""), '%P')

    for i, item in enumerate(lista_acuerdos_default):
        v_chk, v_cant, v_text = tk.BooleanVar(value=True), tk.StringVar(value=str(item["cant"])), tk.StringVar(value=item["texto"])
        tk.Checkbutton(scroll_frame, variable=v_chk, bg="#ecf0f1").grid(row=i+1, column=0)
        tk.Entry(scroll_frame, textvariable=v_cant, width=5, validate="key", validatecommand=vcmd_int, justify="center").grid(row=i+1, column=1)
        tk.Entry(scroll_frame, textvariable=v_text, width=65).grid(row=i+1, column=2, sticky="w", pady=2, padx=5)
        vars_acuerdos.append({"activo": v_chk, "cant": v_cant, "texto": v_text})

def get_acuerdos_seleccionados():
    return [{"cant": i["cant"].get(), "texto": i["texto"].get()} for i in vars_acuerdos if i["activo"].get()]