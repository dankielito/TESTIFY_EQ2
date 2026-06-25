import tkinter as tk

lista_default = [
    "Automatización de reportes en formatos Word y ODF a partir de archivos CSV.",
    "Integración de un asistente de contenido basado en IA para resúmenes narrativos.",
    "Interfaz de usuario intuitiva con dashboards de trazabilidad.",
    "Compatibilidad con estándares de seguridad AES-256 y PostgreSQL.",
    "Disponibilidad de la plataforma del 99.5%"
]

vars_obj_producto = []
frame_obj_prod = None

def agregar_fila_prod(txt=""):
    row = len(vars_obj_producto)
    v_chk = tk.BooleanVar(value=True)
    v_txt = tk.StringVar(value=txt)
    tk.Checkbutton(frame_obj_prod, variable=v_chk, bg="#ecf0f1").grid(row=row, column=0, sticky="w")
    tk.Entry(frame_obj_prod, textvariable=v_txt, width=80).grid(row=row, column=1, pady=2, sticky="w")
    vars_obj_producto.append({"activo": v_chk, "texto": v_txt})

def render_obj_producto(parent_frame):
    global vars_obj_producto, frame_obj_prod
    vars_obj_producto = []
    frame_obj_prod = tk.Frame(parent_frame, bg="#ecf0f1")
    frame_obj_prod.pack(fill="x")
    for txt in lista_default: agregar_fila_prod(txt)
    tk.Button(parent_frame, text="➕ Agregar Objetivo", bg="#34495e", fg="white", command=lambda: agregar_fila_prod("")).pack(anchor="w", pady=5)

def get_obj_producto():
    return [{"texto": i["texto"].get()} for i in vars_obj_producto if i["activo"].get()]