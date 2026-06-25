import tkinter as tk

def_limitaciones = [
    "Tiempo de desarrollo estrictamente vinculado al calendario empresarial de 12 meses",
    "El proyecto debe ejecutarse estrictamente con el presupuesto del proyecto que es de $13,236,817 mxn"
]
def_supuestos = [
    "Se contará con acceso ininterrumpido a las API de IA y servicios de AWS",
    "Las empresas de TI encuestadas brindarán facilidades para el periodo de pruebas.",
    "Se cuenta con la participación de los 5 integrantes de cada área"
]
def_riesgos = [
    "Inestabilidad en la integración de la IA con el formato de archivos CSV durante el desarrollo",
    "Cambios imprevistos en las leyes de protección de datos personales en la CDMX que afecten el almacenamiento en la nube.",
    "No se puede iniciar la comercialización sin el acta constitutiva de la empresa y los registros de marca."
]

vars_presupuesto = {}
vars_lim, vars_sup, vars_rie = [], [], []
frame_lim, frame_sup, frame_rie = None, None, None

def formato_moneda_tiempo_real(event):
    widget = event.widget
    if event.keysym in ("Left", "Right", "Up", "Down", "Home", "End", "Shift_L", "Shift_R", "BackSpace", "Delete"):
        return
    
    pos = widget.index(tk.INSERT)
    texto = widget.get()
    
    filtrado = "".join([c for c in texto if c.isdigit() or c == "."])
    if filtrado.count(".") > 1:
        partes = filtrado.split(".")
        filtrado = partes[0] + "." + "".join(partes[1:])
        
    if not filtrado:
        return
        
    try:
        if "." in filtrado:
            entera, decimal = filtrado.split(".", 1)
            decimal = decimal[:2]
            entera_fmt = f"{int(entera):,}" if entera else "0"
            formateado = f"{entera_fmt}.{decimal}"
        else:
            formateado = f"{int(filtrado):,}"
            
        widget.delete(0, tk.END)
        widget.insert(0, formateado)
        
        diff = len(formateado) - len(texto)
        widget.icursor(pos + diff)
    except ValueError:
        pass

def agregar_fila(lista_vars, parent_frame, txt=""):
    row = len(lista_vars)
    v_chk = tk.BooleanVar(value=True)
    v_txt = tk.StringVar(value=txt)
    tk.Checkbutton(parent_frame, variable=v_chk, bg="#ecf0f1").grid(row=row, column=0, sticky="w")
    tk.Entry(parent_frame, textvariable=v_txt, width=85).grid(row=row, column=1, pady=2, sticky="w")
    lista_vars.append({"activo": v_chk, "texto": v_txt})

def render_presupuesto(parent_frame):
    global frame_lim, frame_sup, frame_rie, vars_lim, vars_sup, vars_rie
    vars_lim, vars_sup, vars_rie = [], [], []

    canvas = tk.Canvas(parent_frame, bg="#ecf0f1", highlightthickness=0)
    scrollbar = tk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#ecf0f1")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    scrollbar.pack(side="right", fill="y")

    f_dinero = tk.Frame(scroll_frame, bg="#ecf0f1")
    f_dinero.pack(fill="x", pady=10)
    tk.Label(f_dinero, text="Presupuesto del Proyecto ($):", bg="#ecf0f1", font=("Arial", 11, "bold")).pack(side="left", padx=5)
    
    vars_presupuesto['presupuesto_AC'] = tk.StringVar(value="14,462,590.00")
    e_pres = tk.Entry(f_dinero, textvariable=vars_presupuesto['presupuesto_AC'], width=25)
    e_pres.pack(side="left")
    e_pres.bind("<KeyRelease>", formato_moneda_tiempo_real)

    tk.Label(scroll_frame, text="Limitaciones:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10,0))
    frame_lim = tk.Frame(scroll_frame, bg="#ecf0f1")
    frame_lim.pack(fill="x")
    for txt in def_limitaciones: agregar_fila(vars_lim, frame_lim, txt)
    tk.Button(scroll_frame, text="➕ Agregar Limitación", bg="#34495e", fg="white", command=lambda: agregar_fila(vars_lim, frame_lim, "")).pack(anchor="w", pady=5)

    tk.Label(scroll_frame, text="Supuestos:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10,0))
    frame_sup = tk.Frame(scroll_frame, bg="#ecf0f1")
    frame_sup.pack(fill="x")
    for txt in def_supuestos: agregar_fila(vars_sup, frame_sup, txt)
    tk.Button(scroll_frame, text="➕ Agregar Supuesto", bg="#34495e", fg="white", command=lambda: agregar_fila(vars_sup, frame_sup, "")).pack(anchor="w", pady=5)

    tk.Label(scroll_frame, text="Riesgos y Dependencias:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10,0))
    frame_rie = tk.Frame(scroll_frame, bg="#ecf0f1")
    frame_rie.pack(fill="x")
    for txt in def_riesgos: agregar_fila(vars_rie, frame_rie, txt)
    tk.Button(scroll_frame, text="➕ Agregar Riesgo", bg="#34495e", fg="white", command=lambda: agregar_fila(vars_rie, frame_rie, "")).pack(anchor="w", pady=5)

def get_presupuesto_data():
    return {
        "presupuesto_AC": vars_presupuesto['presupuesto_AC'].get(),
        "lista_limitaciones": [{"texto": i["texto"].get()} for i in vars_lim if i["activo"].get()],
        "lista_supuestos": [{"texto": i["texto"].get()} for i in vars_sup if i["activo"].get()],
        "lista_riesgos": [{"texto": i["texto"].get()} for i in vars_rie if i["activo"].get()]
    }