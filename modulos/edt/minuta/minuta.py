import tkinter as tk
from tkinter import ttk

vars_minuta_edt = {}
vars_textos_minuta_edt = {}

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
        else:
            formateado = f"{int(filtrado):,}"
        widget.delete(0, tk.END)
        widget.insert(0, formateado)
        widget.icursor(pos + (len(formateado) - len(texto)))
    except ValueError: pass

def render_minuta_edt_tab(parent_frame):
    note_min = ttk.Notebook(parent_frame)
    t_min_encab, t_min_enun = tk.Frame(note_min, bg="#ecf0f1"), tk.Frame(note_min, bg="#ecf0f1")
    note_min.add(t_min_encab, text="1. Encabezado Minuta")
    note_min.add(t_min_enun, text="2. Enunciados Minuta")
    note_min.pack(expand=True, fill="both", padx=10, pady=5)

    vars_minuta_edt.update({
        'numMin': tk.StringVar(value="8"), 'numMEDT': tk.StringVar(value="1"),
        'titulo': tk.StringVar(value="Testify"), 'id': tk.StringVar(value="ES0DC4EM8"),
        'p_etapa': tk.StringVar(value="127,270.79"), 'p_total': tk.StringVar(value="14,462,590.00"),
        'dia': tk.StringVar(value="27"), 'mes': tk.StringVar(value="abril"), 'anio': tk.StringVar(value="2026"),
        'min_tiempo': tk.StringVar(value="4 días")
    })

    tk.Label(t_min_encab, text="Num Minuta:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=5, padx=10)
    f_nums = tk.Frame(t_min_encab, bg="#ecf0f1")
    f_nums.grid(row=0, column=1, sticky="w")
    tk.Entry(f_nums, textvariable=vars_minuta_edt['numMin'], width=5).pack(side="left")
    tk.Label(f_nums, text=" Num ET:", bg="#ecf0f1").pack(side="left")
    tk.Entry(f_nums, textvariable=vars_minuta_edt['numMEDT'], width=5).pack(side="left")
    
    tk.Label(t_min_encab, text="Título:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=5, padx=10)
    tk.Entry(t_min_encab, textvariable=vars_minuta_edt['titulo'], width=30).grid(row=1, column=1, sticky="w")
    tk.Label(t_min_encab, text="ID:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=5, padx=10)
    tk.Entry(t_min_encab, textvariable=vars_minuta_edt['id'], width=30).grid(row=2, column=1, sticky="w")
    
    tk.Label(t_min_encab, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=5, padx=10)
    e1 = tk.Entry(t_min_encab, textvariable=vars_minuta_edt['p_etapa'], width=30)
    e1.grid(row=3, column=1, sticky="w")
    e1.bind("<KeyRelease>", formato_moneda_tiempo_real)
    
    tk.Label(t_min_encab, text="Presupuesto Total:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=5, padx=10)
    e2 = tk.Entry(t_min_encab, textvariable=vars_minuta_edt['p_total'], width=30)
    e2.grid(row=4, column=1, sticky="w")
    e2.bind("<KeyRelease>", formato_moneda_tiempo_real)

    tk.Label(t_min_encab, text="Fecha:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=5, padx=10)
    f_date = tk.Frame(t_min_encab, bg="#ecf0f1")
    f_date.grid(row=5, column=1, sticky="w")
    ttk.Combobox(f_date, textvariable=vars_minuta_edt['dia'], values=[str(i) for i in range(1,32)], width=3).pack(side="left")
    ttk.Combobox(f_date, textvariable=vars_minuta_edt['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date, textvariable=vars_minuta_edt['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    tk.Label(t_min_enun, text="Minuta Actividad:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=(10,0))
    vars_textos_minuta_edt['min_act'] = tk.Text(t_min_enun, height=4, width=90)
    vars_textos_minuta_edt['min_act'].insert("1.0", "Definición y descomposición jerárquica del alcance total del proyecto Testify para la creación de la EDT.")
    vars_textos_minuta_edt['min_act'].pack(padx=10, pady=5)

    tk.Label(t_min_enun, text="Minuta Acuerdos:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor="w", padx=10)
    vars_textos_minuta_edt['min_acu'] = tk.Text(t_min_enun, height=6, width=90)
    vars_textos_minuta_edt['min_acu'].insert("1.0", "Eduardo Carbajal Mendoza realizó de manera individual la sesión técnica para desglosar el proyecto en componentes manejables. Se acordó aplicar la Regla del 100%, validando que los entregables técnicos (IA y base de datos) quedaran correctamente estructurados sin intervención de otros miembros del equipo.")
    vars_textos_minuta_edt['min_acu'].pack(padx=10, pady=5)

    f_tiempo = tk.Frame(t_min_enun, bg="#ecf0f1")
    f_tiempo.pack(anchor="w", padx=10, pady=10)
    tk.Label(f_tiempo, text="Tiempo Minuta:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(side="left", padx=(0,10))
    tk.Entry(f_tiempo, textvariable=vars_minuta_edt['min_tiempo'], width=20).pack(side="left")

def get_minuta_edt_data():
    return {
        "numMinutaEDT": vars_minuta_edt['numMin'].get(), "numMEDT": vars_minuta_edt['numMEDT'].get(),
        "titulo_minuta_EDT": vars_minuta_edt['titulo'].get(), "id_minuta_EDT": vars_minuta_edt['id'].get(),
        "p_minuta_EDT": vars_minuta_edt['p_etapa'].get().replace(',', ''), "pP_minuta_EDT": vars_minuta_edt['p_total'].get().replace(',', ''),
        "fecha_minuta_EDT": f"{vars_minuta_edt['dia'].get()} de {vars_minuta_edt['mes'].get()} del {vars_minuta_edt['anio'].get()}",
        "minuta_actividad_EDT": vars_textos_minuta_edt['min_act'].get("1.0", tk.END).strip(),
        "minuta_acuerdos_EDT": vars_textos_minuta_edt['min_acu'].get("1.0", tk.END).strip(),
        "minuta_tiempo_EDT": vars_minuta_edt['min_tiempo'].get()
    }