import tkinter as tk
from tkinter import ttk, filedialog
import os
from .minuta.minuta import render_minuta_edt_tab, get_minuta_edt_data

vars_encabezado_edt = {}

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

def cambiar_logo_edt():
    ruta = filedialog.askopenfilename(title="Seleccionar Logo", filetypes=[("Archivos PNG", "*.png")])
    if ruta:
        vars_encabezado_edt['logo_path_EDT'].set(ruta)
        try:
            img = tk.PhotoImage(file=ruta).subsample(3, 3)
            lbl_preview_edt.config(image=img, text="")
            lbl_preview_edt.image = img
        except Exception:
            lbl_preview_edt.config(text="✓ Ruta Guardada")

def render_edt_tab(parent_frame):
    header = tk.Frame(parent_frame, bg="#ecf0f1")
    header.pack(fill="x", pady=10)
    tk.Label(header, text="EDICIÓN: 4. Estructura de Desglose de Trabajo (EDT)", font=("Helvetica", 16, "bold"), bg="#ecf0f1").pack(side="left", padx=10)
    
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
    t_encab = tk.Frame(note_plant, bg="#ecf0f1")
    note_plant.add(t_encab, text="1. Encabezado Plantilla")
    note_plant.pack(expand=True, fill="both", padx=10, pady=5)

    global lbl_preview_edt
    frame_img = tk.Frame(t_encab, bg="#ecf0f1")
    frame_img.grid(row=0, column=0, rowspan=5, padx=20, pady=20)
    lbl_preview_edt = tk.Label(frame_img, text="[ Logo ]", bg="#bdc3c7", width=20, height=10)
    lbl_preview_edt.pack()
    tk.Button(frame_img, text="Cambiar Logo", command=cambiar_logo_edt).pack(pady=5)

    vars_encabezado_edt['logo_path_EDT'] = tk.StringVar(value=os.path.abspath(os.path.join("modulos", "img", "logo.png")))
    vars_encabezado_edt.update({
        'numPlan': tk.StringVar(value="8"), 'numET': tk.StringVar(value="1"),
        'titulo': tk.StringVar(value="Testify"), 'id': tk.StringVar(value="ES0DC1E8"),
        'p_etapa': tk.StringVar(value="127,270.79"), 'p_total': tk.StringVar(value="14,462,590.00"),
        'dia': tk.StringVar(value="27"), 'mes': tk.StringVar(value="abril"), 'anio': tk.StringVar(value="2026")
    })

    f_datos = tk.Frame(t_encab, bg="#ecf0f1")
    f_datos.grid(row=0, column=1, sticky="nw", pady=20)

    tk.Label(f_datos, text="Num Plantilla:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=2)
    f_nums = tk.Frame(f_datos, bg="#ecf0f1")
    f_nums.grid(row=0, column=1, sticky="w")
    tk.Entry(f_nums, textvariable=vars_encabezado_edt['numPlan'], width=5).pack(side="left")
    tk.Label(f_nums, text=" Num ET:", bg="#ecf0f1").pack(side="left")
    tk.Entry(f_nums, textvariable=vars_encabezado_edt['numET'], width=5).pack(side="left")

    tk.Label(f_datos, text="Título:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_edt['titulo'], width=30).grid(row=1, column=1, sticky="w")
    tk.Label(f_datos, text="ID:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=2)
    tk.Entry(f_datos, textvariable=vars_encabezado_edt['id'], width=30).grid(row=2, column=1, sticky="w")
    
    tk.Label(f_datos, text="Presupuesto Etapa:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=2)
    e1 = tk.Entry(f_datos, textvariable=vars_encabezado_edt['p_etapa'], width=30)
    e1.grid(row=3, column=1, sticky="w")
    e1.bind("<KeyRelease>", formato_moneda)
    
    tk.Label(f_datos, text="Presupuesto Total:", bg="#ecf0f1").grid(row=4, column=0, sticky="e", pady=2)
    e2 = tk.Entry(f_datos, textvariable=vars_encabezado_edt['p_total'], width=30)
    e2.grid(row=4, column=1, sticky="w")
    e2.bind("<KeyRelease>", formato_moneda)

    tk.Label(f_datos, text="Fecha:", bg="#ecf0f1").grid(row=5, column=0, sticky="e", pady=2)
    f_date1 = tk.Frame(f_datos, bg="#ecf0f1")
    f_date1.grid(row=5, column=1, sticky="w")
    ttk.Combobox(f_date1, textvariable=vars_encabezado_edt['dia'], values=[str(i) for i in range(1, 32)], width=3).pack(side="left")
    ttk.Combobox(f_date1, textvariable=vars_encabezado_edt['mes'], values=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], width=10).pack(side="left", padx=5)
    ttk.Combobox(f_date1, textvariable=vars_encabezado_edt['anio'], values=["2025", "2026", "2027"], width=5).pack(side="left")

    render_minuta_edt_tab(view_minuta)
    view_plantilla.tkraise()

def get_datos_edt():
    data = {
        "logo_path_EDT": vars_encabezado_edt['logo_path_EDT'].get(),
        "numPlantillaEDT": vars_encabezado_edt['numPlan'].get(), "numET_EDT": vars_encabezado_edt['numET'].get(),
        "titulo_plantilla_EDT": vars_encabezado_edt['titulo'].get(), "id_plantilla_EDT": vars_encabezado_edt['id'].get(),
        "p_plantilla_EDT": vars_encabezado_edt['p_etapa'].get().replace(',', ''), "pP_plantilla_EDT": vars_encabezado_edt['p_total'].get().replace(',', ''),
        "fecha_plantilla_EDT": f"{vars_encabezado_edt['dia'].get()} de {vars_encabezado_edt['mes'].get()} del {vars_encabezado_edt['anio'].get()}"
    }
    data.update(get_minuta_edt_data())
    return data