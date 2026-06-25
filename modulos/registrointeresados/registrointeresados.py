import tkinter as tk
from tkinter import ttk, filedialog
import os

from .tabla.tabla import render_tabla_interesados, get_tabla_data
from .minuta.minuta import render_minuta_ri_tab, get_minuta_ri_data

vars_encabezado_ri = {}

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
        
    if not filtrado: return
        
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
    except ValueError: pass

def cambiar_logo():
    ruta = filedialog.askopenfilename(title="Seleccionar Logo", filetypes=[("Archivos PNG", "*.png")])
    if ruta:
        vars_encabezado_ri['logo_path_RI'].set(ruta)
        try:
            img = tk.PhotoImage(file=ruta).subsample(3, 3)
            lbl_preview_ri.config(image=img, text="")
            lbl_preview_ri.image = img
        except Exception:
            lbl_preview_ri.config(text="✓ Ruta Guardada")

def get_datos_interesados():
    fecha_plant = f"{vars_encabezado_ri['dia'].get()} de {vars_encabezado_ri['mes'].get()} del {vars_encabezado_ri['anio'].get()}"
    p_plan = f"{float(vars_encabezado_ri['p_etapa'].get().replace(',', '') or 0):,.2f}"
    pt_plan = f"{float(vars_encabezado_ri['p_total'].get().replace(',', '') or 0):,.2f}"

    payload = {
        "logo_path_RI": vars_encabezado_ri['logo_path_RI'].get(),
        "numPlantillaRI": vars_encabezado_ri['numPlan'].get(),
        "numETRI": vars_encabezado_ri['numET'].get(),
        "titulo_plantilla_RI": vars_encabezado_ri['titulo'].get(),
        "id_plantilla_RI": vars_encabezado_ri['id'].get(),
        "p_plantilla_RI": p_plan,
        "pP_plantilla_RI": pt_plan,
        "fecha_plantilla_RI": fecha_plant,
    }
    
    # Unimos la tabla y la minuta
    payload.update(get_tabla_data())
    payload.update(get_minuta_ri_data())
    
    return payload

def render_interesados_tab(parent_frame):
    # HEADER Y BOTONES TOGGLE
    header = tk.Frame(parent_frame, bg="#ecf0f1")
    header.pack(fill="x", pady=10)
    
    tk.Label(header, text="EDICIÓN: 2. Registro de Interesados", font=("Helvetica", 16, "bold"), bg="#ecf0f1").pack(side="left", padx=10)
    
    tk.Button(header, text="📄 Plantilla", bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=lambda: view_plantilla_ri.tkraise()).pack(side="left", padx=5)
    tk.Button(header, text="📝 Minuta", bg="#9b59b6", fg="white", font=("Arial", 10, "bold"), command=lambda: view_minuta_ri.tkraise()).pack(side="left", padx=5)

    # CONTENEDOR DE VISTAS
    container = tk.Frame(parent_frame, bg="#ecf0f1")
    container.pack(expand=True, fill="both")
    
    global view_plantilla_ri, view_minuta_ri
    view_plantilla_ri = tk.Frame(container, bg="#ecf0f1")
    view_minuta_ri = tk.Frame(container, bg="#ecf0f1")
    view_plantilla_ri.grid(row=0, column=0, sticky="nsew")
    view_minuta_ri.grid(row=0, column=0, sticky="nsew")
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # ================== VISTA PLANTILLA (2 Pestañas) ==================
    note_plant = ttk.Notebook(view_plantilla_ri)
    t_encab = tk.Frame(note_plant, bg="#ecf0f1")
    t_tabla = tk.Frame(note_plant, bg="#ecf0f1")
    
    note_plant.add(t_encab, text="1. Encabezado")
    note_plant.add(t_tabla, text="2. Matriz de Interesados")
    note_plant.pack(expand=True, fill="both", padx=10, pady=5)

    # --- Pestaña 1: Encabezado ---
    global lbl_preview_ri
    frame_img = tk.Frame(t_encab, bg="#ecf0f1")
    frame_img.grid(row=0, column=0, rowspan=5, padx=20, pady=20)
    lbl_preview_ri = tk.Label(frame_img, text="[ Logo ]", bg="#bdc3c7", width=20, height=10)
    lbl_preview_ri.pack()
    tk.Button(frame_img, text="Cambiar Logo", command=cambiar_logo).pack(pady=5)
    
    vars_encabezado_ri['logo_path_RI'] = tk.StringVar(value=os.path.abspath(os.path.join("modulos", "img", "logo.png")))
    
    vars_encabezado_ri.update({
        'numPlan': tk.StringVar(value="6"), 'numET': tk.StringVar(value="1"),
        'titulo': tk.StringVar(value="Testify"), 'id': tk.StringVar(value="ES0DC1E6"),
        'p_etapa': tk.StringVar(value="127,270.79"), 'p_total': tk.StringVar(value="14,462,590.00"),
        'dia': tk.StringVar(value="30"), 'mes': tk.StringVar(value="marzo"), 'anio': tk.StringVar(value="2026")
    })

    f_datos = tk.Frame(t_encab, bg="#ecf0f1")
    f_datos.grid(row=0, column=1, sticky="nw", pady=20)

    tk.Label(f_datos, text="Num Plantilla:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=2)
    f_nums = tk.Frame(f_datos, bg="#ecf0f1")
    f_nums.grid(row=0, column=1, sticky="w")
    tk.Entry(f_nums, textvariable=vars_encabezado_ri['numPlan'], width=5).pack(side="left")
    tk.Label(f_nums, text=" Num ET:", bg="#ecf0f1").pack(side="left")
    tk.Entry(f_nums, textvariable=vars_encabezado_ri['numET'], width=5).pack(side="left")
    
    tk.Label(f_datos, text="Título:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_ri['titulo'], width=30).grid(row=1, column=1, sticky="w")
    tk.Label(f_datos, text="ID:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_ri['id'], width=30).grid(row=2, column=1, sticky="w")
    
    tk.Label(f_datos, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=2)
    e1 = tk.Entry(f_datos, textvariable=vars_encabezado_ri['p_etapa'], width=30)
    e1.grid(row=3, column=1, sticky="w")
    e1.bind("<KeyRelease>", formato_moneda_tiempo_real)
    
    tk.Label(f_datos, text="Presupuesto Total:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=2)
    e2 = tk.Entry(f_datos, textvariable=vars_encabezado_ri['p_total'], width=30)
    e2.grid(row=4, column=1, sticky="w")
    e2.bind("<KeyRelease>", formato_moneda_tiempo_real)

    tk.Label(f_datos, text="Fecha:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=2)
    f_date1 = tk.Frame(f_datos, bg="#ecf0f1")
    f_date1.grid(row=5, column=1, sticky="w")
    ttk.Combobox(f_date1, textvariable=vars_encabezado_ri['dia'], values=[str(i) for i in range(1, 32)], width=3).pack(side="left")
    ttk.Combobox(f_date1, textvariable=vars_encabezado_ri['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date1, textvariable=vars_encabezado_ri['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    # --- Pestaña 2: Matriz ---
    render_tabla_interesados(t_tabla)

    # ================== VISTA MINUTA (Llamada al módulo) ==================
    render_minuta_ri_tab(view_minuta_ri)

    # Iniciar mostrando la plantilla
    view_plantilla_ri.tkraise()