import tkinter as tk
from tkinter import ttk

vars_minuta_pdp = {}
vars_textos_minuta_pdp = {}

def formato_moneda_tiempo_real(event):
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

def render_minuta_pdp_tab(parent_frame):
    note_min = ttk.Notebook(parent_frame)
    t_min_encab, t_min_enun = tk.Frame(note_min, bg="#ecf0f1"), tk.Frame(note_min, bg="#ecf0f1")
    note_min.add(t_min_encab, text="1. Encabezado Minuta")
    note_min.add(t_min_enun, text="2. Enunciados Minuta")
    note_min.pack(expand=True, fill="both", padx=10, pady=5)

    vars_minuta_pdp.update({
        'numMin': tk.StringVar(value="G"), 'numMPDP': tk.StringVar(value="1"),
        'titulo': tk.StringVar(value="Testify"), 'id': tk.StringVar(value="ES0DC4EM9"),
        'p_etapa': tk.StringVar(value="127,270.79"), 'p_total': tk.StringVar(value="14,462,590.00"),
        'dia': tk.StringVar(value="27"), 'mes': tk.StringVar(value="abril"), 'anio': tk.StringVar(value="2026"),
        'min_tiempo': tk.StringVar(value="4 días")
    })

    tk.Label(t_min_encab, text="Num Minuta:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=5, padx=10)
    f_nums = tk.Frame(t_min_encab, bg="#ecf0f1")
    f_nums.grid(row=0, column=1, sticky="w")
    tk.Entry(f_nums, textvariable=vars_minuta_pdp['numMin'], width=5).pack(side="left")
    tk.Label(f_nums, text=" Num ET:", bg="#ecf0f1").pack(side="left")
    tk.Entry(f_nums, textvariable=vars_minuta_pdp['numMPDP'], width=5).pack(side="left")
    
    tk.Label(t_min_encab, text="Título:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=5, padx=10)
    tk.Entry(t_min_encab, textvariable=vars_minuta_pdp['titulo'], width=30).grid(row=1, column=1, sticky="w")
    tk.Label(t_min_encab, text="ID:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=5, padx=10)
    tk.Entry(t_min_encab, textvariable=vars_minuta_pdp['id'], width=30).grid(row=2, column=1, sticky="w")
    
    tk.Label(t_min_encab, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=5, padx=10)
    e1 = tk.Entry(t_min_encab, textvariable=vars_minuta_pdp['p_etapa'], width=30)
    e1.grid(row=3, column=1, sticky="w")
    e1.bind("<KeyRelease>", formato_moneda_tiempo_real)
    
    tk.Label(t_min_encab, text="Presupuesto Total:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=5, padx=10)
    e2 = tk.Entry(t_min_encab, textvariable=vars_minuta_pdp['p_total'], width=30)
    e2.grid(row=4, column=1, sticky="w")
    e2.bind("<KeyRelease>", formato_moneda_tiempo_real)

    tk.Label(t_min_encab, text="Fecha:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=5, padx=10)
    f_date = tk.Frame(t_min_encab, bg="#ecf0f1")
    f_date.grid(row=5, column=1, sticky="w")
    ttk.Combobox(f_date, textvariable=vars_minuta_pdp['dia'], values=[str(i) for i in range(1,32)], width=3).pack(side="left")
    ttk.Combobox(f_date, textvariable=vars_minuta_pdp['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date, textvariable=vars_minuta_pdp['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    tk.Label(t_min_enun, text="Minuta Actividad:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=(10,0))
    vars_textos_minuta_pdp['min_act'] = tk.Text(t_min_enun, height=4, width=90)
    vars_textos_minuta_pdp['min_act'].insert("1.0", "Elaboración del Plan para la Dirección del Proyecto, incluyendo ciclo de vida, procesos de gestión, enfoque de trabajo, gestión de líneas base, revisiones de gestión y planes adjuntos.")
    vars_textos_minuta_pdp['min_act'].pack(padx=10, pady=5)

    tk.Label(t_min_enun, text="Minuta Acuerdos:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", padx=10)
    vars_textos_minuta_pdp['min_acu'] = tk.Text(t_min_enun, height=6, width=90)
    vars_textos_minuta_pdp['min_acu'].insert("1.0", "El líder de proyecto Daniel Romero fue responsable de desarrollar el Plan para la Dirección del Proyecto. Se acordó estructurar el documento conforme a los lineamientos de gestión de proyectos, integrando todos los componentes necesarios todas las etapas correctas. El equipo validó que el contenido estuviera alineado con los objetivos, alcance, cronograma y presupuesto establecidos.")
    vars_textos_minuta_pdp['min_acu'].pack(padx=10, pady=5)

    f_tiempo = tk.Frame(t_min_enun, bg="#ecf0f1")
    f_tiempo.pack(anchor="w", padx=10, pady=10)
    tk.Label(f_tiempo, text="Tiempo Minuta:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(side="left", padx=(0,10))
    tk.Entry(f_tiempo, textvariable=vars_minuta_pdp['min_tiempo'], width=20).pack(side="left")

def get_minuta_pdp_data():
    return {
        "numMinutaPDP": vars_minuta_pdp['numMin'].get(), "numMPDP": vars_minuta_pdp['numMPDP'].get(),
        "titulo_minuta_PDP": vars_minuta_pdp['titulo'].get(), "id_minuta_PDP": vars_minuta_pdp['id'].get(),
        "p_minuta_PDP": vars_minuta_pdp['p_etapa'].get().replace(',', ''), "pP_minuta_PDP": vars_minuta_pdp['p_total'].get().replace(',', ''),
        "fecha_minuta_PDP": f"{vars_minuta_pdp['dia'].get()} de {vars_minuta_pdp['mes'].get()} del {vars_minuta_pdp['anio'].get()}",
        "minuta_actividad_PDP": vars_textos_minuta_pdp['min_act'].get("1.0", tk.END).strip(),
        "minuta_acuerdos_PDP": vars_textos_minuta_pdp['min_acu'].get("1.0", tk.END).strip(),
        "minuta_tiempo_PDP": vars_minuta_pdp['min_tiempo'].get()
    }