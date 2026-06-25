import tkinter as tk
from tkinter import ttk, filedialog
import os

from .acuerdos.acuerdos import render_acuerdos_subtab, get_acuerdos_seleccionados
from .hitos.hitos import render_hitos_subtab, get_hitos_seleccionados
from .objetivos.objetivosProducto.obj_producto import render_obj_producto, get_obj_producto
from .objetivos.objetivosProyecto.obj_proyecto import render_obj_proyecto, get_obj_proyecto
from .exclusiones.exclusiones import render_exclusiones, get_exclusiones
from .presupuesto.presupuesto import render_presupuesto, get_presupuesto_data
from .minuta.minuta import render_minuta_tab, get_minuta_data

vars_encabezado = {}
vars_textos = {}

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

def cambiar_logo():
    ruta = filedialog.askopenfilename(title="Seleccionar Logo", filetypes=[("Archivos PNG", "*.png")])
    if ruta:
        vars_encabezado['logo_path'].set(ruta)
        try:
            img = tk.PhotoImage(file=ruta).subsample(3, 3)
            lbl_preview.config(image=img, text="")
            lbl_preview.image = img
        except Exception:
            lbl_preview.config(text="✓ Ruta Guardada")

def get_datos_acta():
    fecha_plant = f"{vars_encabezado['dia'].get()} de {vars_encabezado['mes'].get()} del {vars_encabezado['anio'].get()}"

    payload = {
        "logo_path": vars_encabezado['logo_path'].get(),
        "numPlantillaAC": vars_encabezado['numPlan'].get(),
        "numETAC": vars_encabezado['numET'].get(),
        "titulo_plantilla_AC": vars_encabezado['titulo'].get(),
        "id_plantilla_AC": vars_encabezado['id'].get(),
        "p_plantilla_AC": vars_encabezado['p_etapa'].get(),
        "pP_plantilla_ACl": vars_encabezado['p_total'].get(),
        "fecha_plantilla_AC": fecha_plant,
        "enunciado": vars_textos['enunciado'].get("1.0", tk.END).strip(),
        "caso": vars_textos['caso'].get("1.0", tk.END).strip(),
        "lista_obj_producto": get_obj_producto(),
        "lista_obj_proyecto": get_obj_proyecto(),
        "lista_exclusiones": get_exclusiones(),
        "lista_acuerdos": get_acuerdos_seleccionados(),
        "lista_hitos": get_hitos_seleccionados(),
    }
    
    payload.update(get_presupuesto_data())
    payload.update(get_minuta_data())
    return payload
 
def render_acta_tab(parent_frame):
    header = tk.Frame(parent_frame, bg="#ecf0f1")
    header.pack(fill="x", pady=10)
    tk.Label(header, text="EDICIÓN: 1. Acta Constitución", font=("Helvetica", 16, "bold"), bg="#ecf0f1").pack(side="left", padx=10)
    
    tk.Button(header, text="📄 Plantilla", bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=lambda: view_plantilla.tkraise()).pack(side="left", padx=5)
    tk.Button(header, text="📝 Minuta", bg="#9b59b6", fg="white", font=("Arial", 10, "bold"), command=lambda: view_minuta.tkraise()).pack(side="left", padx=5)

    container = tk.Frame(parent_frame, bg="#ecf0f1")
    container.pack(expand=True, fill="both")
    
    global view_plantilla, view_minuta
    view_plantilla = tk.Frame(container, bg="#ecf0f1")
    view_minuta = tk.Frame(container, bg="#ecf0f1")
    view_plantilla.grid(row=0, column=0, sticky="nsew")
    view_minuta.grid(row=0, column=0, sticky="nsew")
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    note_plant = ttk.Notebook(view_plantilla)
    t_encab, t_datos, t_acuerdos, t_hitos, t_presupuesto = tk.Frame(note_plant, bg="#ecf0f1"), tk.Frame(note_plant, bg="#ecf0f1"), tk.Frame(note_plant, bg="#ecf0f1"), tk.Frame(note_plant, bg="#ecf0f1"), tk.Frame(note_plant, bg="#ecf0f1")
    note_plant.add(t_encab, text="1. Encabezado"); note_plant.add(t_datos, text="2. Datos Generales"); note_plant.add(t_acuerdos, text="3. Acuerdos")
    note_plant.add(t_hitos, text="4. Hitos"); note_plant.add(t_presupuesto, text="5. Presupuesto")
    note_plant.pack(expand=True, fill="both", padx=10, pady=5)

    # --- Pestaña 1: Encabezado ---
    global lbl_preview
    frame_img = tk.Frame(t_encab, bg="#ecf0f1")
    frame_img.grid(row=0, column=0, rowspan=5, padx=20, pady=20)
    lbl_preview = tk.Label(frame_img, text="[ Logo ]", bg="#bdc3c7", width=20, height=10)
    lbl_preview.pack()
    tk.Button(frame_img, text="Cambiar Logo", command=cambiar_logo).pack(pady=5)
    
    vars_encabezado['logo_path'] = tk.StringVar(value=os.path.abspath(os.path.join("modulos", "img", "logo.png")))
    vars_encabezado.update({'numPlan': tk.StringVar(value="5"), 'numET': tk.StringVar(value="1"), 'titulo': tk.StringVar(value="Testify"), 'id': tk.StringVar(value="ES0DC1E5"), 'p_etapa': tk.StringVar(value="13,236,817.00"), 'p_total': tk.StringVar(value="14,462,590.00"), 'dia': tk.StringVar(value="25"), 'mes': tk.StringVar(value="junio"), 'anio': tk.StringVar(value="2026")})

    f_datos = tk.Frame(t_encab, bg="#ecf0f1")
    f_datos.grid(row=0, column=1, sticky="nw", pady=20)

    tk.Label(f_datos, text="Num Plantilla:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado['numPlan'], width=5).grid(row=0, column=1, sticky="w")
    tk.Label(f_datos, text="Num ET:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado['numET'], width=5).grid(row=1, column=1, sticky="w")
    tk.Label(f_datos, text="Título:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado['titulo'], width=30).grid(row=2, column=1, sticky="w")
    tk.Label(f_datos, text="ID:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado['id'], width=30).grid(row=3, column=1, sticky="w")
    
    tk.Label(f_datos, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=2)
    e1 = tk.Entry(f_datos, textvariable=vars_encabezado['p_etapa'], width=30)
    e1.grid(row=4, column=1, sticky="w")
    e1.bind("<KeyRelease>", formato_moneda_tiempo_real)
    
    tk.Label(f_datos, text="Presupuesto Total:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=2)
    e2 = tk.Entry(f_datos, textvariable=vars_encabezado['p_total'], width=30)
    e2.grid(row=5, column=1, sticky="w")
    e2.bind("<KeyRelease>", formato_moneda_tiempo_real)

    tk.Label(f_datos, text="Fecha:", bg="#ecf0f1").grid(row=6, column=0, sticky="e", pady=2)
    f_date1 = tk.Frame(f_datos, bg="#ecf0f1")
    f_date1.grid(row=6, column=1, sticky="w")
    ttk.Combobox(f_date1, textvariable=vars_encabezado['dia'], values=[str(i) for i in range(1, 32)], width=3).pack(side="left")
    ttk.Combobox(f_date1, textvariable=vars_encabezado['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date1, textvariable=vars_encabezado['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    # --- Pestaña 2: Datos Generales ---
    c_datos = tk.Canvas(t_datos, bg="#ecf0f1", highlightthickness=0)
    s_datos = tk.Scrollbar(t_datos, orient="vertical", command=c_datos.yview)
    f_scroll_datos = tk.Frame(c_datos, bg="#ecf0f1")
    f_scroll_datos.bind("<Configure>", lambda e: c_datos.configure(scrollregion=c_datos.bbox("all")))
    c_datos.create_window((0, 0), window=f_scroll_datos, anchor="nw")
    c_datos.configure(yscrollcommand=s_datos.set)
    c_datos.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    s_datos.pack(side="right", fill="y")

    tk.Label(f_scroll_datos, text="Enunciado Trabajo:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", pady=(5,0))
    vars_textos['enunciado'] = tk.Text(f_scroll_datos, height=6, width=90)
    vars_textos['enunciado'].insert("1.0", "El proyecto es una plataforma de automatización impulsada por Inteligencia Artificial que transforma datos técnicos en reportes ejecutivos. Este se desea realizar en un año con el fin de detectar una problemática crítica en las empresas de TI en de la CDMX por la excesiva carga de trabajo manual y la falta de estandarización en la documentación de pruebas de software, esto genera retrasos en las entregas y posibles errores humanos. Es fundamental para la dirección por que representa una oportunidad estratégica de ser líderes en el sector tecnológico con un presupuesto de $13,236,817 pesos mexicanos.")
    vars_textos['enunciado'].pack(pady=5)

    tk.Label(f_scroll_datos, text="Caso de Negocio:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w")
    vars_textos['caso'] = tk.Text(f_scroll_datos, height=6, width=90)
    vars_textos['caso'].insert("1.0", "El proyecto es rentable debido a que el 73.33% de los clientes potenciales encuestados muestran disposición de compra. En la proyección de ventas nos indica que anualmente tenemos una venta de más de 22 millones de pesos el primer año, lo que representa un margen de utilidad significativo frente al costo de desarrollo. Estratégicamente, posiciona a la organización como líder en el uso de IA aplicada a la documentación de QA en el mercado local.")
    vars_textos['caso'].pack(pady=5)

    ttk.Separator(f_scroll_datos, orient='horizontal').pack(fill='x', pady=10)

    tk.Label(f_scroll_datos, text="Objetivos del Producto:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w")
    f_obj_prod = tk.Frame(f_scroll_datos, bg="#ecf0f1")
    f_obj_prod.pack(fill="x")
    render_obj_producto(f_obj_prod)

    tk.Label(f_scroll_datos, text="Objetivos del Proyecto:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10,0))
    f_obj_proy = tk.Frame(f_scroll_datos, bg="#ecf0f1")
    f_obj_proy.pack(fill="x")
    render_obj_proyecto(f_obj_proy)

    tk.Label(f_scroll_datos, text="Exclusiones:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10,0))
    f_exclu = tk.Frame(f_scroll_datos, bg="#ecf0f1")
    f_exclu.pack(fill="x")
    render_exclusiones(f_exclu)

    render_acuerdos_subtab(t_acuerdos)
    render_hitos_subtab(t_hitos)
    render_presupuesto(t_presupuesto)

    # Invocación limpia al renderizado de la Minuta
    render_minuta_tab(view_minuta)

    view_plantilla.tkraise()