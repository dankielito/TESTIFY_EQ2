import tkinter as tk
from tkinter import ttk

vars_minuta_gr = {}
vars_textos_minuta_gr = {}

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

def render_minuta_gr_tab(parent_frame):
    note_min = ttk.Notebook(parent_frame)
    t_min_encab, t_min_enun = tk.Frame(note_min, bg="#ecf0f1"), tk.Frame(note_min, bg="#ecf0f1")
    note_min.add(t_min_encab, text="1. Encabezado Minuta")
    note_min.add(t_min_enun, text="2. Enunciados Minuta")
    note_min.pack(expand=True, fill="both", padx=10, pady=5)

    vars_minuta_gr.update({
        'numMin': tk.StringVar(value="10"), 'numMGR': tk.StringVar(value="1"),
        'titulo': tk.StringVar(value="Testify"), 'id': tk.StringVar(value="ES0DC4EM10"),
        'p_etapa': tk.StringVar(value="127,270.79"), 'p_total': tk.StringVar(value="14,462,590.00"),
        'dia': tk.StringVar(value="27"), 'mes': tk.StringVar(value="abril"), 'anio': tk.StringVar(value="2026"),
        't1': tk.StringVar(value="2 días"), 't2': tk.StringVar(value="3 días")
    })

    tk.Label(t_min_encab, text="Num Minuta:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=5, padx=10)
    f_nums = tk.Frame(t_min_encab, bg="#ecf0f1")
    f_nums.grid(row=0, column=1, sticky="w")
    tk.Entry(f_nums, textvariable=vars_minuta_gr['numMin'], width=5).pack(side="left")
    tk.Label(f_nums, text=" Num ET:", bg="#ecf0f1").pack(side="left")
    tk.Entry(f_nums, textvariable=vars_minuta_gr['numMGR'], width=5).pack(side="left")
    
    tk.Label(t_min_encab, text="Título:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=5, padx=10)
    tk.Entry(t_min_encab, textvariable=vars_minuta_gr['titulo'], width=30).grid(row=1, column=1, sticky="w")
    tk.Label(t_min_encab, text="ID:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=5, padx=10)
    tk.Entry(t_min_encab, textvariable=vars_minuta_gr['id'], width=30).grid(row=2, column=1, sticky="w")
    
    tk.Label(t_min_encab, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=5, padx=10)
    e1 = tk.Entry(t_min_encab, textvariable=vars_minuta_gr['p_etapa'], width=30)
    e1.grid(row=3, column=1, sticky="w")
    e1.bind("<KeyRelease>", formato_moneda_tiempo_real)
    
    tk.Label(t_min_encab, text="Presupuesto Total:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=5, padx=10)
    e2 = tk.Entry(t_min_encab, textvariable=vars_minuta_gr['p_total'], width=30)
    e2.grid(row=4, column=1, sticky="w")
    e2.bind("<KeyRelease>", formato_moneda_tiempo_real)

    tk.Label(t_min_encab, text="Fecha:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=5, padx=10)
    f_date = tk.Frame(t_min_encab, bg="#ecf0f1")
    f_date.grid(row=5, column=1, sticky="w")
    ttk.Combobox(f_date, textvariable=vars_minuta_gr['dia'], values=[str(i) for i in range(1,32)], width=3).pack(side="left")
    ttk.Combobox(f_date, textvariable=vars_minuta_gr['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date, textvariable=vars_minuta_gr['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    # Pestaña 2: Scroll para los enunciados
    c_enun = tk.Canvas(t_min_enun, bg="#ecf0f1", highlightthickness=0)
    s_enun = tk.Scrollbar(t_min_enun, orient="vertical", command=c_enun.yview)
    f_scroll = tk.Frame(c_enun, bg="#ecf0f1")
    f_scroll.bind("<Configure>", lambda e: c_enun.configure(scrollregion=c_enun.bbox("all")))
    c_enun.create_window((0, 0), window=f_scroll, anchor="nw")
    c_enun.configure(yscrollcommand=s_enun.set)
    c_enun.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    s_enun.pack(side="right", fill="y")

    tk.Label(f_scroll, text="Minuta Actividad 1:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10,0))
    vars_textos_minuta_gr['act1'] = tk.Text(f_scroll, height=2, width=90)
    vars_textos_minuta_gr['act1'].insert("1.0", "Definición y arquitectura para guardar la información en la nube")
    vars_textos_minuta_gr['act1'].pack(pady=5)

    tk.Label(f_scroll, text="Minuta Actividad 2:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w")
    vars_textos_minuta_gr['act2'] = tk.Text(f_scroll, height=2, width=90)
    vars_textos_minuta_gr['act2'].insert("1.0", "Revisión de Algoritmos de IA")
    vars_textos_minuta_gr['act2'].pack(pady=5)

    tk.Label(f_scroll, text="Minuta Acuerdo 1:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w")
    vars_textos_minuta_gr['acu1'] = tk.Text(f_scroll, height=3, width=90)
    vars_textos_minuta_gr['acu1'].insert("1.0", "Daniel y Estephany acordaron migrar la base de datos de un entorno local a una instancia de AWS RDS para asegurar la disponibilidad del 99.5%.")
    vars_textos_minuta_gr['acu1'].pack(pady=5)

    tk.Label(f_scroll, text="Minuta Acuerdo 2:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w")
    vars_textos_minuta_gr['acu2'] = tk.Text(f_scroll, height=3, width=90)
    vars_textos_minuta_gr['acu2'].insert("1.0", "Daniel presentó el ajuste en el motor de mapeo para evitar errores de lectura en archivos CSV con formatos variables. Estephany estuvo de acuerdo con el mapeo por lo cual se aplicara.")
    vars_textos_minuta_gr['acu2'].pack(pady=5)

    f_tiempo = tk.Frame(f_scroll, bg="#ecf0f1")
    f_tiempo.pack(anchor="w", pady=10)
    tk.Label(f_tiempo, text="Tiempo 1:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(side="left")
    tk.Entry(f_tiempo, textvariable=vars_minuta_gr['t1'], width=10).pack(side="left", padx=5)
    tk.Label(f_tiempo, text="Tiempo 2:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(side="left", padx=(15,0))
    tk.Entry(f_tiempo, textvariable=vars_minuta_gr['t2'], width=10).pack(side="left", padx=5)

def get_minuta_gr_data():
    return {
        "numMinutaGR": vars_minuta_gr['numMin'].get(), "numMGR": vars_minuta_gr['numMGR'].get(),
        "titulo_minuta_GR": vars_minuta_gr['titulo'].get(), "id_minuta_GR": vars_minuta_gr['id'].get(),
        "p_minuta_GR": vars_minuta_gr['p_etapa'].get().replace(',', ''), "pP_minuta_GR": vars_minuta_gr['p_total'].get().replace(',', ''),
        "fecha_minuta_GR": f"{vars_minuta_gr['dia'].get()} de {vars_minuta_gr['mes'].get()} del {vars_minuta_gr['anio'].get()}",
        "minuta_actividad_GR1": vars_textos_minuta_gr['act1'].get("1.0", tk.END).strip(),
        "minuta_actividad_GR2": vars_textos_minuta_gr['act2'].get("1.0", tk.END).strip(),
        "minuta_acuerdos_GR1": vars_textos_minuta_gr['acu1'].get("1.0", tk.END).strip(),
        "minuta_acuerdos_GR2": vars_textos_minuta_gr['acu2'].get("1.0", tk.END).strip(),
        "minuta_tiempo_GR1": vars_minuta_gr['t1'].get(), "minuta_tiempo_GR2": vars_minuta_gr['t2'].get()
    }