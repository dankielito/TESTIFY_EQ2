import tkinter as tk

lista_default = [
    "Finalizar el desarrollo y pruebas en un periodo de 12 meses.",
    "Entregar el sistema funcional a las empresas.",
    "Entregar documentación técnica y manuales de usuario."
]

vars_obj_proyecto = []
frame_obj_proy = None

def agregar_fila_proy(txt=""):
    row = len(vars_obj_proyecto)
    v_chk = tk.BooleanVar(value=True)
    v_txt = tk.StringVar(value=txt)
    tk.Checkbutton(frame_obj_proy, variable=v_chk, bg="#ecf0f1").grid(row=row, column=0, sticky="w")
    tk.Entry(frame_obj_proy, textvariable=v_txt, width=80).grid(row=row, column=1, pady=2, sticky="w")
    vars_obj_proyecto.append({"activo": v_chk, "texto": v_txt})

def render_obj_proyecto(parent_frame):
    global vars_obj_proyecto, frame_obj_proy
    vars_obj_proyecto = []
    frame_obj_proy = tk.Frame(parent_frame, bg="#ecf0f1")
    frame_obj_proy.pack(fill="x")
    for txt in lista_default: agregar_fila_proy(txt)
    tk.Button(parent_frame, text="➕ Agregar Objetivo", bg="#34495e", fg="white", command=lambda: agregar_fila_proy("")).pack(anchor="w", pady=5)

def get_obj_proyecto():
    return [{"texto": i["texto"].get()} for i in vars_obj_proyecto if i["activo"].get()]