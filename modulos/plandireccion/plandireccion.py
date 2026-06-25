import tkinter as tk
from tkinter import ttk, filedialog
import os
from .tablas.tablas_pdp import render_tablas_pdp, get_tablas_pdp_data
from .minuta.minuta import render_minuta_pdp_tab, get_minuta_pdp_data

vars_encabezado_pdp = {}
vars_textos_pdp = {}

def formato_moneda(event):
    widget = event.widget
    if event.keysym in ("Left", "Right", "Up", "Down", "Home", "End", "Shift_L", "Shift_R", "BackSpace", "Delete"): return
    pos, texto = widget.index(tk.INSERT), widget.get()
    filtrado = "".join([c for c in texto if c.isdigit() or c == "."])
    if filtrado.count(".") > 1:
        partes = filtrado.split(".")
        filtrado = partes[0] + "." + "".join(partes[1:])
    if not filtrado: return
    try:
        if "." in filtrado:
            entera, decimal = filtrado.split(".", 1)
            formateado = f"{int(entera):,}.{decimal[:2]}" if entera else f"0.{decimal[:2]}"
        else: formateado = f"{int(filtrado):,}"
        widget.delete(0, tk.END)
        widget.insert(0, formateado)
        widget.icursor(pos + (len(formateado) - len(texto)))
    except ValueError: pass

def cambiar_logo_pdp():
    ruta = filedialog.askopenfilename(title="Seleccionar Logo", filetypes=[("Archivos PNG", "*.png")])
    if ruta:
        vars_encabezado_pdp['logo_path_PDP'].set(ruta)
        try:
            img = tk.PhotoImage(file=ruta).subsample(3, 3)
            lbl_preview_pdp.config(image=img, text="")
            lbl_preview_pdp.image = img
        except Exception:
            lbl_preview_pdp.config(text="✓ Ruta Guardada")

def render_pdp_tab(parent_frame):
    header = tk.Frame(parent_frame, bg="#ecf0f1")
    header.pack(fill="x", pady=10)
    tk.Label(header, text="EDICIÓN: 5. Plan Dirección de Proyectos", font=("Helvetica", 16, "bold"), bg="#ecf0f1").pack(side="left", padx=10)
    
    tk.Button(header, text="📄 Plantilla", bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=lambda: view_plantilla.tkraise()).pack(side="left", padx=5)
    tk.Button(header, text="📝 Minuta", bg="#9b59b6", fg="white", font=("Arial", 10, "bold"), command=lambda: view_minuta.tkraise()).pack(side="left", padx=5)

    container = tk.Frame(parent_frame, bg="#ecf0f1")
    container.pack(expand=True, fill="both")
    
    global view_plantilla, view_minuta
    view_plantilla, view_minuta = tk.Frame(container, bg="#ecf0f1"), tk.Frame(container, bg="#ecf0f1")
    view_plantilla.grid(row=0, column=0, sticky="nsew")
    view_minuta.grid(row=0, column=0, sticky="nsew")
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # --- PLANTILLA ---
    note_plant = ttk.Notebook(view_plantilla)
    t_encab, t_enun, t_tablas = tk.Frame(note_plant, bg="#ecf0f1"), tk.Frame(note_plant, bg="#ecf0f1"), tk.Frame(note_plant, bg="#ecf0f1")
    note_plant.add(t_encab, text="1. Encabezado"); note_plant.add(t_enun, text="2. Enunciados"); note_plant.add(t_tablas, text="3. Tablas")
    note_plant.pack(expand=True, fill="both", padx=10, pady=5)

    # 1. Encabezado
    global lbl_preview_pdp
    frame_img = tk.Frame(t_encab, bg="#ecf0f1")
    frame_img.grid(row=0, column=0, rowspan=5, padx=20, pady=20)
    lbl_preview_pdp = tk.Label(frame_img, text="[ Logo ]", bg="#bdc3c7", width=20, height=10)
    lbl_preview_pdp.pack()
    tk.Button(frame_img, text="Cambiar Logo", command=cambiar_logo_pdp).pack(pady=5)

    vars_encabezado_pdp['logo_path_PDP'] = tk.StringVar(value=os.path.abspath(os.path.join("modulos", "img", "logo.png")))
    vars_encabezado_pdp.update({
        'numPlan': tk.StringVar(value="G"), 'numET': tk.StringVar(value="1"),
        'titulo': tk.StringVar(value="Testify"), 'id': tk.StringVar(value="ES0DC1E9"),
        'p_etapa': tk.StringVar(value="127,270.79"), 'p_total': tk.StringVar(value="14,462,590.00"),
        'dia': tk.StringVar(value="25"), 'mes': tk.StringVar(value="abril"), 'anio': tk.StringVar(value="2026")
    })

    f_datos = tk.Frame(t_encab, bg="#ecf0f1")
    f_datos.grid(row=0, column=1, sticky="nw", pady=20)
    tk.Label(f_datos, text="Num Plantilla:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=2)
    f_nums = tk.Frame(f_datos, bg="#ecf0f1")
    f_nums.grid(row=0, column=1, sticky="w")
    tk.Entry(f_nums, textvariable=vars_encabezado_pdp['numPlan'], width=5).pack(side="left")
    tk.Label(f_nums, text=" Num ET:", bg="#ecf0f1").pack(side="left")
    tk.Entry(f_nums, textvariable=vars_encabezado_pdp['numET'], width=5).pack(side="left")

    tk.Label(f_datos, text="Título:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_pdp['titulo'], width=30).grid(row=1, column=1, sticky="w")
    tk.Label(f_datos, text="ID:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_pdp['id'], width=30).grid(row=2, column=1, sticky="w")
    
    tk.Label(f_datos, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=2)
    e1 = tk.Entry(f_datos, textvariable=vars_encabezado_pdp['p_etapa'], width=30)
    e1.grid(row=3, column=1, sticky="w")
    e1.bind("<KeyRelease>", formato_moneda)
    
    tk.Label(f_datos, text="Presupuesto Total:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=2)
    e2 = tk.Entry(f_datos, textvariable=vars_encabezado_pdp['p_total'], width=30)
    e2.grid(row=4, column=1, sticky="w")
    e2.bind("<KeyRelease>", formato_moneda)

    tk.Label(f_datos, text="Fecha:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=2)
    f_date = tk.Frame(f_datos, bg="#ecf0f1")
    f_date.grid(row=5, column=1, sticky="w")
    ttk.Combobox(f_date, textvariable=vars_encabezado_pdp['dia'], values=[str(i) for i in range(1, 32)], width=3).pack(side="left")
    ttk.Combobox(f_date, textvariable=vars_encabezado_pdp['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date, textvariable=vars_encabezado_pdp['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    # 2. Enunciados (Scrollable)
    c_enun = tk.Canvas(t_enun, bg="#ecf0f1", highlightthickness=0)
    s_enun = tk.Scrollbar(t_enun, orient="vertical", command=c_enun.yview)
    f_scroll_enun = tk.Frame(c_enun, bg="#ecf0f1")
    f_scroll_enun.bind("<Configure>", lambda e: c_enun.configure(scrollregion=c_enun.bbox("all")))
    c_enun.create_window((0, 0), window=f_scroll_enun, anchor="nw")
    c_enun.configure(yscrollcommand=s_enun.set)
    c_enun.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    s_enun.pack(side="right", fill="y")

    titulos = ["ENFOQUE DE TRABAJO", "GESTIÓN DE LÍNEAS BASE", "Estado actual del proyecto", "Reporte de progreso", "Pronósticos:", "Otros:"]
    claves = ['ENFOQUE_TRABAJO_PDP', 'GESTION_PDP', 'estadoACtual_PDP', 'reporteProgresol_PDP', 'pronosticol_PDP', 'otroos_PDP']
    textos_def = [
        "El proyecto Testify se desarrollará bajo un enfoque estructurado con apoyo de metodologías ágiles (Cascada), permitiendo una ejecución organizada, iterativa y con mejora continua. El equipo de proyecto trabajará de manera colaborativa, asegurando el cumplimiento de los objetivos en términos de alcance, tiempo, costo y calidad.\n1. Inicialmente en equipo se establecen objetivos, entregables, restricciones y supuestos para delimitar el proyecto.\n2. Se elaboran los documentos clave como plan del proyecto, cronograma, presupuesto y riesgos.\n3. Se definen responsabilidades del equipo para cada entregable.\n4. El proyecto se desarrolla mediante sprints, generando entregables parciales.\n5. Se realizan reuniones periódicas para evaluar avances y tomar acciones correctivas.\n6. Se identifican riesgos y se controlan los cambios mediante un proceso formal.\n7. Se revisa que cada entregable cumpla con los criterios establecidos.\n8. Se entrega el producto final y se realiza el cierre formal.",
        "La gestión de líneas base del proyecto Testify permitirá mantener el control del desempeño en términos de alcance, tiempo y costo. Estas líneas base serán utilizadas como referencia para medir el avance real del proyecto y detectar desviaciones.\nEl informe de desempeño del proyecto será presentado de forma semanal en reuniones de seguimiento y contendrá la siguiente información:",
        "1. Situación del alcance: comparación entre avance real y planificado.\n2. Eficiencia del cronograma: SV (Variación del Cronograma) y SPI (Índice de Desempeño del Cronograma).\n3. Eficiencia del costo: CV (Variación del Costo) y CPI (Índice de Desempeño del Costo).\n4. Cumplimiento de objetivos de calidad.",
        "1. Avance del periodo: porcentaje planificado vs real.\n2. Valor ganado del periodo: valor planificado y real.\n3. Costos del periodo: costo planificado vs real.\n4. Indicadores del cronograma: SV y SPI del periodo.\n5. Indicadores de costo: CV y CPI del periodo.",
        "1. Pronóstico de costos: EAC, ETC y VAC.\n2. Pronóstico de tiempo: fecha planificada vs estimada de finalización.",
        "1. Problemas y pendientes del proyecto.\n2. Acciones correctivas.\n3. Curva S del proyecto."
    ]

    for i in range(6):
        tk.Label(f_scroll_enun, text=titulos[i], bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10,0))
        vars_textos_pdp[claves[i]] = tk.Text(f_scroll_enun, height=6, width=100)
        vars_textos_pdp[claves[i]].insert("1.0", textos_def[i])
        vars_textos_pdp[claves[i]].pack(pady=5)

    # 3. Tablas
    c_tab = tk.Canvas(t_tablas, bg="#ecf0f1", highlightthickness=0)
    s_tab = tk.Scrollbar(t_tablas, orient="vertical", command=c_tab.yview)
    f_scroll_tab = tk.Frame(c_tab, bg="#ecf0f1")
    f_scroll_tab.bind("<Configure>", lambda e: c_tab.configure(scrollregion=c_tab.bbox("all")))
    c_tab.create_window((0, 0), window=f_scroll_tab, anchor="nw")
    c_tab.configure(yscrollcommand=s_tab.set)
    c_tab.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    s_tab.pack(side="right", fill="y")
    
    render_tablas_pdp(f_scroll_tab)

    # --- MINUTA ---
    render_minuta_pdp_tab(view_minuta)
    view_plantilla.tkraise()

def get_datos_pdp():
    data = {
        "logo_path_PDP": vars_encabezado_pdp['logo_path_PDP'].get(),
        "numPlantillaPDP": vars_encabezado_pdp['numPlan'].get(), "numET_PDP": vars_encabezado_pdp['numET'].get(),
        "titulo_plantilla_PDP": vars_encabezado_pdp['titulo'].get(), "id_plantilla_PDP": vars_encabezado_pdp['id'].get(),
        "p_plantilla_PDP": vars_encabezado_pdp['p_etapa'].get().replace(',', ''), "pP_plantilla_PDP": vars_encabezado_pdp['p_total'].get().replace(',', ''),
        "fecha_plantilla_PDP": f"{vars_encabezado_pdp['dia'].get()} de {vars_encabezado_pdp['mes'].get()} del {vars_encabezado_pdp['anio'].get()}"
    }
    for clave in vars_textos_pdp:
        data[clave] = vars_textos_pdp[clave].get("1.0", tk.END).strip()
        
    data.update(get_tablas_pdp_data())
    data.update(get_minuta_pdp_data())
    return data