import tkinter as tk

lista_default = [
    "No incluye la provisión de hardware físico para los clientes",
    "No incluye el pago de servicios en la nube por parte de los clientes finales",
    "No incluye cambios en el sistema"
]

vars_exclusiones = []
frame_exclusiones = None

def agregar_fila_exclusion(txt=""):
    row = len(vars_exclusiones)
    v_chk = tk.BooleanVar(value=True)
    v_txt = tk.StringVar(value=txt)
    tk.Checkbutton(frame_exclusiones, variable=v_chk, bg="#ecf0f1").grid(row=row, column=0, sticky="w")
    tk.Entry(frame_exclusiones, textvariable=v_txt, width=80).grid(row=row, column=1, pady=2, sticky="w")
    vars_exclusiones.append({"activo": v_chk, "texto": v_txt})

def render_exclusiones(parent_frame):
    global vars_exclusiones, frame_exclusiones
    vars_exclusiones = []
    
    frame_exclusiones = tk.Frame(parent_frame, bg="#ecf0f1")
    frame_exclusiones.pack(fill="x")
    
    for txt in lista_default:
        agregar_fila_exclusion(txt)
        
    tk.Button(parent_frame, text="➕ Agregar Exclusión", bg="#34495e", fg="white", command=lambda: agregar_fila_exclusion("")).pack(anchor="w", pady=5)

def get_exclusiones():
    return [{"texto": i["texto"].get()} for i in vars_exclusiones if i["activo"].get()]