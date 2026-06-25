import tkinter as tk
from tkinter import ttk, filedialog
import os

from .tablas.tabla_alcance import render_tablas_alcance, get_tablas_alcance
from .minuta.minuta import render_minuta_gap_tab, get_minuta_gap_data

vars_encabezado_gp = {}
vars_textos_gp = {}

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

def cambiar_logo_gp():
    ruta = filedialog.askopenfilename(title="Seleccionar Logo", filetypes=[("Archivos PNG", "*.png")])
    if ruta:
        vars_encabezado_gp['logo_path_GP'].set(ruta)
        try:
            img = tk.PhotoImage(file=ruta).subsample(3, 3)
            lbl_preview_gp.config(image=img, text="")
            lbl_preview_gp.image = img
        except Exception:
            lbl_preview_gp.config(text="✓ Ruta Guardada")

def render_alcance_tab(parent_frame):
    # HEADER Y BOTONES TOGGLE
    header = tk.Frame(parent_frame, bg="#ecf0f1")
    header.pack(fill="x", pady=10)
    
    tk.Label(header, text="EDICIÓN: 3. Gestión del Alcance", font=("Helvetica", 16, "bold"), bg="#ecf0f1").pack(side="left", padx=10)
    
    tk.Button(header, text="📄 Plantilla", bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=lambda: view_plantilla_gp.tkraise()).pack(side="left", padx=5)
    tk.Button(header, text="📝 Minuta", bg="#9b59b6", fg="white", font=("Arial", 10, "bold"), command=lambda: view_minuta_gp.tkraise()).pack(side="left", padx=5)

    # CONTENEDOR DE VISTAS
    container = tk.Frame(parent_frame, bg="#ecf0f1")
    container.pack(expand=True, fill="both")
    
    global view_plantilla_gp, view_minuta_gp
    view_plantilla_gp = tk.Frame(container, bg="#ecf0f1")
    view_minuta_gp = tk.Frame(container, bg="#ecf0f1")
    view_plantilla_gp.grid(row=0, column=0, sticky="nsew")
    view_minuta_gp.grid(row=0, column=0, sticky="nsew")
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # --- PESTAÑAS PLANTILLA ---
    notebook = ttk.Notebook(view_plantilla_gp)
    t_encab = tk.Frame(notebook, bg="#ecf0f1")
    t_enun = tk.Frame(notebook, bg="#ecf0f1")
    t_tablas = tk.Frame(notebook, bg="#ecf0f1")
    
    notebook.add(t_encab, text="1. Encabezado")
    notebook.add(t_enun, text="2. Descripción")
    notebook.add(t_tablas, text="3. Tablas")
    notebook.pack(expand=True, fill="both", padx=10, pady=5)

    # --- Encabezado ---
    global lbl_preview_gp
    frame_img = tk.Frame(t_encab, bg="#ecf0f1")
    frame_img.grid(row=0, column=0, rowspan=5, padx=20, pady=20)
    lbl_preview_gp = tk.Label(frame_img, text="[ Logo ]", bg="#bdc3c7", width=20, height=10)
    lbl_preview_gp.pack()
    tk.Button(frame_img, text="Cambiar Logo", command=cambiar_logo_gp).pack(pady=5)

    vars_encabezado_gp['logo_path_GP'] = tk.StringVar(value=os.path.abspath(os.path.join("modulos", "img", "logo.png")))
    vars_encabezado_gp.update({
        'numPlan': tk.StringVar(value="7"), 'numET': tk.StringVar(value="1"),
        'titulo': tk.StringVar(value="Testify"), 'id': tk.StringVar(value="ES0DC1E7"),
        'p_etapa': tk.StringVar(value="127,270.79"), 'p_total': tk.StringVar(value="14,462,590.00"),
        'dia': tk.StringVar(value="27"), 'mes': tk.StringVar(value="abril"), 'anio': tk.StringVar(value="2026")
    })

    f_datos = tk.Frame(t_encab, bg="#ecf0f1")
    f_datos.grid(row=0, column=1, sticky="nw", pady=20)

    tk.Label(f_datos, text="Num Plantilla:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=2)
    f_nums = tk.Frame(f_datos, bg="#ecf0f1")
    f_nums.grid(row=0, column=1, sticky="w")
    tk.Entry(f_nums, textvariable=vars_encabezado_gp['numPlan'], width=5).pack(side="left")
    tk.Label(f_nums, text=" Num ET:", bg="#ecf0f1").pack(side="left")
    tk.Entry(f_nums, textvariable=vars_encabezado_gp['numET'], width=5).pack(side="left")

    tk.Label(f_datos, text="Título:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_gp['titulo'], width=30).grid(row=1, column=1, sticky="w")
    tk.Label(f_datos, text="ID:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_gp['id'], width=30).grid(row=2, column=1, sticky="w")
    
    tk.Label(f_datos, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=2)
    e1 = tk.Entry(f_datos, textvariable=vars_encabezado_gp['p_etapa'], width=30)
    e1.grid(row=3, column=1, sticky="w")
    e1.bind("<KeyRelease>", formato_moneda_tiempo_real)
    
    tk.Label(f_datos, text="Presupuesto Total:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=2)
    e2 = tk.Entry(f_datos, textvariable=vars_encabezado_gp['p_total'], width=30)
    e2.grid(row=4, column=1, sticky="w")
    e2.bind("<KeyRelease>", formato_moneda_tiempo_real)

    tk.Label(f_datos, text="Fecha:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=2)
    f_date1 = tk.Frame(f_datos, bg="#ecf0f1")
    f_date1.grid(row=5, column=1, sticky="w")
    ttk.Combobox(f_date1, textvariable=vars_encabezado_gp['dia'], values=[str(i) for i in range(1, 32)], width=3).pack(side="left")
    ttk.Combobox(f_date1, textvariable=vars_encabezado_gp['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date1, textvariable=vars_encabezado_gp['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    # --- Descripción ---
    tk.Label(t_enun, text="1. Descripción del Proyecto:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=(10,0))
    vars_textos_gp['enunciado'] = tk.Text(t_enun, height=8, width=90)
    vars_textos_gp['enunciado'].insert("1.0", "El proyecto consiste en una plataforma web con inteligencia artificial para la generación automatizada de documentación de pruebas de software en empresas de TI. El mercado meta son las alcaldías Cuauhtémoc, Miguel Hidalgo y Benito Juárez en la CDMX, con un presupuesto de $14,462,590 MXN.")
    vars_textos_gp['enunciado'].pack(padx=10, pady=10)

    # --- Tablas ---
    c_tablas = tk.Canvas(t_tablas, bg="#ecf0f1", highlightthickness=0)
    s_tablas = tk.Scrollbar(t_tablas, orient="vertical", command=c_tablas.yview)
    f_scroll_tablas = tk.Frame(c_tablas, bg="#ecf0f1")
    f_scroll_tablas.bind("<Configure>", lambda e: c_tablas.configure(scrollregion=c_tablas.bbox("all")))
    c_tablas.create_window((0, 0), window=f_scroll_tablas, anchor="nw")
    c_tablas.configure(yscrollcommand=s_tablas.set)
    c_tablas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    s_tablas.pack(side="right", fill="y")

    render_tablas_alcance(f_scroll_tablas)

    # ================== VISTA MINUTA ==================
    render_minuta_gap_tab(view_minuta_gp)

    view_plantilla_gp.tkraise()

def get_datos_alcance():
    fecha = f"{vars_encabezado_gp['dia'].get()} de {vars_encabezado_gp['mes'].get()} del {vars_encabezado_gp['anio'].get()}"
    p_plan = f"{float(vars_encabezado_gp['p_etapa'].get().replace(',', '') or 0):,.2f}"
    pt_plan = f"{float(vars_encabezado_gp['p_total'].get().replace(',', '') or 0):,.2f}"

    data = {
        "logo_path_GP": vars_encabezado_gp['logo_path_GP'].get(),
        "numPlantillaGP": vars_encabezado_gp['numPlan'].get(),
        "numETAC": vars_encabezado_gp['numET'].get(),
        "titulo_plantilla_GP": vars_encabezado_gp['titulo'].get(),
        "id_plantilla_GP": vars_encabezado_gp['id'].get(),
        "p_plantilla_GP": p_plan,
        "pP_plantilla_GP": pt_plan,
        "fecha_plantilla_GP": fecha,
        "enunciado_DP_GP": vars_textos_gp['enunciado'].get("1.0", tk.END).strip()
    }
    data.update(get_tablas_alcance())
    data.update(get_minuta_gap_data())
    return data