import tkinter as tk
from tkinter import ttk, filedialog
import os
from .tablas.tablas_gr import render_tablas_gr, get_tablas_gr_data
from .minuta.minuta import render_minuta_gr_tab, get_minuta_gr_data

vars_encabezado_gr = {}
vars_textos_gr = {}

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

def cambiar_logo_gr():
    ruta = filedialog.askopenfilename(title="Seleccionar Logo", filetypes=[("Archivos PNG", "*.png")])
    if ruta:
        vars_encabezado_gr['logo_path_GR'].set(ruta)
        try:
            img = tk.PhotoImage(file=ruta).subsample(3, 3)
            lbl_preview_gr.config(image=img, text="")
            lbl_preview_gr.image = img
        except Exception:
            lbl_preview_gr.config(text="✓ Ruta Guardada")

def render_gr_tab(parent_frame):
    header = tk.Frame(parent_frame, bg="#ecf0f1")
    header.pack(fill="x", pady=10)
    tk.Label(header, text="EDICIÓN: 6. Gestión de Requerimientos", font=("Helvetica", 16, "bold"), bg="#ecf0f1").pack(side="left", padx=10)
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

    note_plant = ttk.Notebook(view_plantilla)
    t_encab, t_enun, t_tablas = tk.Frame(note_plant, bg="#ecf0f1"), tk.Frame(note_plant, bg="#ecf0f1"), tk.Frame(note_plant, bg="#ecf0f1")
    note_plant.add(t_encab, text="1. Encabezado"); note_plant.add(t_enun, text="2. Observaciones"); note_plant.add(t_tablas, text="3. Tablas")
    note_plant.pack(expand=True, fill="both", padx=10, pady=5)

    global lbl_preview_gr
    frame_img = tk.Frame(t_encab, bg="#ecf0f1")
    frame_img.grid(row=0, column=0, rowspan=5, padx=20, pady=20)
    lbl_preview_gr = tk.Label(frame_img, text="[ Logo ]", bg="#bdc3c7", width=20, height=10)
    lbl_preview_gr.pack()
    tk.Button(frame_img, text="Cambiar Logo", command=cambiar_logo_gr).pack(pady=5)

    vars_encabezado_gr['logo_path_GR'] = tk.StringVar(value=os.path.abspath(os.path.join("modulos", "img", "logo.png")))
    vars_encabezado_gr.update({
        'numPlan': tk.StringVar(value="10"), 'numET': tk.StringVar(value="1"),
        'titulo': tk.StringVar(value="Testify"), 'id': tk.StringVar(value="ES0DC1E10"),
        'p_etapa': tk.StringVar(value="127,270.79"), 'p_total': tk.StringVar(value="14,462,590.00"),
        'dia': tk.StringVar(value="27"), 'mes': tk.StringVar(value="abril"), 'anio': tk.StringVar(value="2026")
    })

    f_datos = tk.Frame(t_encab, bg="#ecf0f1")
    f_datos.grid(row=0, column=1, sticky="nw", pady=20)
    tk.Label(f_datos, text="Num Plantilla:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=2)
    f_nums = tk.Frame(f_datos, bg="#ecf0f1")
    f_nums.grid(row=0, column=1, sticky="w")
    tk.Entry(f_nums, textvariable=vars_encabezado_gr['numPlan'], width=5).pack(side="left")
    tk.Label(f_nums, text=" Num ET:", bg="#ecf0f1").pack(side="left")
    tk.Entry(f_nums, textvariable=vars_encabezado_gr['numET'], width=5).pack(side="left")

    tk.Label(f_datos, text="Título:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_gr['titulo'], width=30).grid(row=1, column=1, sticky="w")
    tk.Label(f_datos, text="ID:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_gr['id'], width=30).grid(row=2, column=1, sticky="w")
    
    tk.Label(f_datos, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=2)
    e1 = tk.Entry(f_datos, textvariable=vars_encabezado_gr['p_etapa'], width=30)
    e1.grid(row=3, column=1, sticky="w")
    e1.bind("<KeyRelease>", formato_moneda)
    
    tk.Label(f_datos, text="Presupuesto Total:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=2)
    e2 = tk.Entry(f_datos, textvariable=vars_encabezado_gr['p_total'], width=30)
    e2.grid(row=4, column=1, sticky="w")
    e2.bind("<KeyRelease>", formato_moneda)

    tk.Label(f_datos, text="Fecha:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=2)
    f_date = tk.Frame(f_datos, bg="#ecf0f1")
    f_date.grid(row=5, column=1, sticky="w")
    ttk.Combobox(f_date, textvariable=vars_encabezado_gr['dia'], values=[str(i) for i in range(1, 32)], width=3).pack(side="left")
    ttk.Combobox(f_date, textvariable=vars_encabezado_gr['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date, textvariable=vars_encabezado_gr['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    # Observaciones
    tk.Label(t_enun, text="5. Observaciones", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=(10,0))
    vars_textos_gr['lasObervacioneeees_GR'] = tk.Text(t_enun, height=12, width=90)
    txt_obs = "• Priorización de la Ruta Crítica: Se ha dado prioridad absoluta a los requerimientos RQ-03 (IA) y RQ-08 (Base de Datos), ya que cualquier retraso en estos módulos compromete el cronograma de 12 meses planeado para el desarrollo.\n• Ajustes de Infraestructura: La migración a AWS RDS (Control de Cambio V1.2) asegura el cumplimiento del requerimiento no funcional de disponibilidad del 99.5%, aunque represente un incremento operativo mensual de $4,500 MXN.\n• Gestión de Talento Operativo: La carga de trabajo detectada en el rediseño de la interfaz móvil sugiere que el equipo operativo deberá optimizar los sprints de Scrum para no exceder el presupuesto de horas hombre previsto.\n• Seguridad y Cumplimiento: Con la implementación del cifrado AES-256 y la validación por token, el proyecto se alinea preventivamente con las normas ISO/IEC 27001 antes de pasar a la fase de pruebas con clientes piloto."
    vars_textos_gr['lasObervacioneeees_GR'].insert("1.0", txt_obs)
    vars_textos_gr['lasObervacioneeees_GR'].pack(padx=10, pady=5)

    # Tablas con Scroll
    c_tab = tk.Canvas(t_tablas, bg="#ecf0f1", highlightthickness=0)
    s_tab = tk.Scrollbar(t_tablas, orient="vertical", command=c_tab.yview)
    f_scroll_tab = tk.Frame(c_tab, bg="#ecf0f1")
    f_scroll_tab.bind("<Configure>", lambda e: c_tab.configure(scrollregion=c_tab.bbox("all")))
    c_tab.create_window((0, 0), window=f_scroll_tab, anchor="nw")
    c_tab.configure(yscrollcommand=s_tab.set)
    c_tab.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    s_tab.pack(side="right", fill="y")
    
    render_tablas_gr(f_scroll_tab)
    render_minuta_gr_tab(view_minuta)
    view_plantilla.tkraise()

def get_datos_gr():
    data = {
        "logo_path_GR": vars_encabezado_gr['logo_path_GR'].get(),
        "numPlantillaGR": vars_encabezado_gr['numPlan'].get(), "numET_GR": vars_encabezado_gr['numET'].get(),
        "titulo_plantilla_GR": vars_encabezado_gr['titulo'].get(), "id_plantilla_GR": vars_encabezado_gr['id'].get(),
        "p_plantilla_GR": vars_encabezado_gr['p_etapa'].get().replace(',', ''), "pP_plantilla_GR": vars_encabezado_gr['p_total'].get().replace(',', ''),
        "fecha_plantilla_GR": f"{vars_encabezado_gr['dia'].get()} de {vars_encabezado_gr['mes'].get()} del {vars_encabezado_gr['anio'].get()}"
    }
    data["lasObervacioneeees_GR"] = vars_textos_gr['lasObervacioneeees_GR'].get("1.0", tk.END).strip()
    data.update(get_tablas_gr_data())
    data.update(get_minuta_gr_data())
    return data