import tkinter as tk
from tkinter import ttk

vars_minuta = {}
vars_textos_minuta = {}

def formato_moneda_tiempo_real(event):
    widget = event.widget
    if event.keysym in ("Left", "Right", "Up", "Down", "Home", "End", "Shift_L", "Shift_R", "BackSpace", "Delete"):
        return
    
    pos = widget.index(tk.INSERT)
    texto = widget.get()
    
    # Filtrar caracteres no numéricos dejando solo dígitos y un punto
    filtrado = ""
    puntos = 0
    for c in texto:
        if c.isdigit():
            filtrado += c
        elif c == "." and puntos == 0:
            filtrado += c
            puntos += 1
            
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
        
        # Ajuste inteligente de la posición del cursor
        diff = len(formateado) - len(texto)
        widget.icursor(pos + diff)
    except ValueError:
        pass

def render_minuta_tab(parent_frame):
    note_min = ttk.Notebook(parent_frame)
    t_min_encab = tk.Frame(note_min, bg="#ecf0f1")
    t_min_enun = tk.Frame(note_min, bg="#ecf0f1")
    note_min.add(t_min_encab, text="1. Encabezado Minuta")
    note_min.add(t_min_enun, text="2. Enunciados Minuta")
    note_min.pack(expand=True, fill="both", padx=10, pady=5)

    vars_minuta.update({
        'numMin': tk.StringVar(value="5"), 
        'titulo': tk.StringVar(value="Testify"), 
        'id': tk.StringVar(value="ES0DC4EM5"),
        'p_etapa': tk.StringVar(value="127,270.79"), 
        'p_total': tk.StringVar(value="14,462,590.00"),
        'dia': tk.StringVar(value="25"), 
        'mes': tk.StringVar(value="marzo"), 
        'anio': tk.StringVar(value="2026"),
        'min_tiempo': tk.StringVar(value="3 días")
    })

    # --- PESTAÑA 1: ENCABEZADO ---
    tk.Label(t_min_encab, text="Num Minuta:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=5, padx=10)
    tk.Entry(t_min_encab, textvariable=vars_minuta['numMin'], width=5).grid(row=0, column=1, sticky="w")
    
    tk.Label(t_min_encab, text="Título:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=5, padx=10)
    tk.Entry(t_min_encab, textvariable=vars_minuta['titulo'], width=30).grid(row=1, column=1, sticky="w")
    
    tk.Label(t_min_encab, text="ID:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=5, padx=10)
    tk.Entry(t_min_encab, textvariable=vars_minuta['id'], width=30).grid(row=2, column=1, sticky="w")
    
    tk.Label(t_min_encab, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=5, padx=10)
    e_etapa = tk.Entry(t_min_encab, textvariable=vars_minuta['p_etapa'], width=30)
    e_etapa.grid(row=3, column=1, sticky="w")
    e_etapa.bind("<KeyRelease>", formato_moneda_tiempo_real)
    
    tk.Label(t_min_encab, text="Presupuesto Total:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=5, padx=10)
    e_total = tk.Entry(t_min_encab, textvariable=vars_minuta['p_total'], width=30)
    e_total.grid(row=4, column=1, sticky="w")
    e_total.bind("<KeyRelease>", formato_moneda_tiempo_real)

    tk.Label(t_min_encab, text="Fecha:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=5, padx=10)
    f_date2 = tk.Frame(t_min_encab, bg="#ecf0f1")
    f_date2.grid(row=5, column=1, sticky="w")
    ttk.Combobox(f_date2, textvariable=vars_minuta['dia'], values=[str(i) for i in range(1, 32)], width=3).pack(side="left")
    ttk.Combobox(f_date2, textvariable=vars_minuta['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date2, textvariable=vars_minuta['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    # --- PESTAÑA 2: ENUNCIADOS ---
    tk.Label(t_min_enun, text="Minuta Actividad:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=(10,0))
    vars_textos_minuta['min_act'] = tk.Text(t_min_enun, height=4, width=90)
    txt_act_def = "Elaboración del Acta de Constitución del Proyecto, definiendo el alcance general, objetivos, stakeholders principales, presupuesto estimado y la autorización formal del proyecto Testify."
    vars_textos_minuta['min_act'].insert("1.0", txt_act_def)
    vars_textos_minuta['min_act'].pack(padx=10, pady=5)

    tk.Label(t_min_enun, text="Minuta Acuerdos:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", padx=10)
    vars_textos_minuta['min_acu'] = tk.Text(t_min_enun, height=5, width=90)
    txt_acu_def = "La integrante Angela Martínez fue responsable de redactar el Acta de Constitución del Proyecto, integrando la información proporcionada por el equipo. Se acordó que el documento incluiría los objetivos, justificación, alcance, entregables principales, presupuesto estimado y roles del equipo. Asimismo, todos los integrantes revisaron el contenido y aprobaron el documento final."
    vars_textos_minuta['min_acu'].insert("1.0", txt_acu_def)
    vars_textos_minuta['min_acu'].pack(padx=10, pady=5)

    # Nuevo bloque de Tiempo solicitado
    f_tiempo = tk.Frame(t_min_enun, bg="#ecf0f1")
    f_tiempo.pack(anchor="w", padx=10, pady=10)
    tk.Label(f_tiempo, text="Tiempo Minuta:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(side="left", padx=(0,10))
    tk.Entry(f_tiempo, textvariable=vars_minuta['min_tiempo'], width=20).pack(side="left")

def get_minuta_data():
    fecha_min = f"{vars_minuta['dia'].get()} de {vars_minuta['mes'].get()} del {vars_minuta['anio'].get()}"
    return {
        "numMinutaAC": vars_minuta['numMin'].get(),
        "titulo_minuta_AC": vars_minuta['titulo'].get(),
        "id_minuta_AC": vars_minuta['id'].get(),
        "p_minuta_AC": vars_minuta['p_etapa'].get(),
        "pP_minuta_AC": vars_minuta['p_total'].get(),
        "fecha_minuta_AC": fecha_min,
        "minuta_actividad": vars_textos_minuta['min_act'].get("1.0", tk.END).strip(),
        "minuta_acuerdo": vars_textos_minuta['min_acu'].get("1.0", tk.END).strip(),
        "minuta_tiempo": vars_minuta['min_tiempo'].get()
    }