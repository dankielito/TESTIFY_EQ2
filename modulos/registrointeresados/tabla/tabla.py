import tkinter as tk
from tkinter import ttk
from .datos_tabla import nombres_interesados, opciones_poder, opciones_estrategia

filas_memoria = []
herramienta_actual = None

def aplicar_herramienta(event, variable_celda):
    if herramienta_actual:
        variable_celda.set(herramienta_actual.get())

def render_tabla_interesados(parent_frame):
    global herramienta_actual, filas_memoria
    filas_memoria = []

    # --- 1. PANEL DE HERRAMIENTAS (Pincel) ---
    panel_herramientas = tk.Frame(parent_frame, bg="#ecf0f1")
    panel_herramientas.pack(fill="x", pady=10, padx=10)
    
    tk.Label(panel_herramientas, text="🖌️ Herramienta de Compromiso:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(side="left", padx=5)
    
    herramienta_actual = tk.StringVar(value="X")
    
    estilo_radio = {"bg": "#ecf0f1", "activebackground": "#ecf0f1", "font": ("Arial", 10)}
    tk.Radiobutton(panel_herramientas, text="Solo 'X'", variable=herramienta_actual, value="X", **estilo_radio).pack(side="left", padx=5)
    tk.Radiobutton(panel_herramientas, text="Solo 'D'", variable=herramienta_actual, value="D", **estilo_radio).pack(side="left", padx=5)
    tk.Radiobutton(panel_herramientas, text="Ambas 'X,D'", variable=herramienta_actual, value="X,D", **estilo_radio).pack(side="left", padx=5)
    tk.Radiobutton(panel_herramientas, text="Borrar Celda", variable=herramienta_actual, value="", **estilo_radio).pack(side="left", padx=5)
    
    tk.Label(panel_herramientas, text="(Selecciona una y haz clic en las celdas blancas de abajo)", bg="#ecf0f1", fg="#7f8c8d", font=("Arial", 9, "italic")).pack(side="left", padx=20)

    # --- 2. CONTENEDOR CON SCROLL PARA LA TABLA ---
    canvas = tk.Canvas(parent_frame, bg="white", highlightthickness=1, highlightbackground="#bdc3c7")
    scrollbar = tk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="white")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True, padx=10, pady=5)
    scrollbar.pack(side="right", fill="y")

    # --- 3. ENCABEZADOS DE LA TABLA ---
    headers = ["Interesado", "Desconoce", "Se resiste", "Neutral", "Apoya", "Líder", "Poder", "Interés", "Estrategia"]
    for col, txt in enumerate(headers):
        tk.Label(scroll_frame, text=txt, bg="#34495e", fg="white", font=("Arial", 9, "bold"), width=15 if col == 0 or col == 8 else 8, relief="ridge").grid(row=0, column=col, sticky="nsew")

    # --- 4. GENERACIÓN DE FILAS (1 al 17) ---
    for row, nombre in enumerate(nombres_interesados, start=1):
        tk.Label(scroll_frame, text=nombre, bg="#f8f9fa", font=("Arial", 9), relief="ridge", anchor="w", padx=5).grid(row=row, column=0, sticky="nsew")
        
        diccionario_fila = {"nombre": nombre}
        
        columnas_comp = ["des", "res", "neu", "apo", "lid"]
        for col_idx, clave in enumerate(columnas_comp, start=1):
            var_celda = tk.StringVar(value="")
            diccionario_fila[clave] = var_celda
            
            lbl_celda = tk.Entry(scroll_frame, textvariable=var_celda, font=("Arial", 10, "bold"), justify="center", bg="white", cursor="hand2", relief="ridge")
            lbl_celda.bind("<Button-1>", lambda e, v=var_celda: aplicar_herramienta(e, v))
            lbl_celda.grid(row=row, column=col_idx, sticky="nsew")

        var_poder = tk.StringVar(value="A")
        cb_poder = ttk.Combobox(scroll_frame, textvariable=var_poder, values=opciones_poder, state="readonly", width=5, justify="center")
        cb_poder.grid(row=row, column=6, padx=2, pady=2)
        diccionario_fila["poder"] = var_poder

        var_interes = tk.StringVar(value="A")
        cb_interes = ttk.Combobox(scroll_frame, textvariable=var_interes, values=opciones_poder, state="readonly", width=5, justify="center")
        cb_interes.grid(row=row, column=7, padx=2, pady=2)
        diccionario_fila["interes"] = var_interes

        var_est = tk.StringVar(value="Gestionar de cerca")
        cb_est = ttk.Combobox(scroll_frame, textvariable=var_est, values=opciones_estrategia, state="readonly", width=18)
        cb_est.grid(row=row, column=8, padx=2, pady=2)
        diccionario_fila["estrategia"] = var_est

        filas_memoria.append(diccionario_fila)

# ==============================================================
# MAPEO PLANO HACIA EL WORD (1 al 17 exacto)
# ==============================================================
def get_tabla_data():
    payload = {}
    
    # Recorre la memoria y va armando { "nom_1": "Director", "des_1": "X", ... }
    for i, fila in enumerate(filas_memoria, start=1):
        payload[f"nom_{i}"] = fila["nombre"]
        payload[f"des_{i}"] = fila["des"].get()
        payload[f"res_{i}"] = fila["res"].get()
        payload[f"neu_{i}"] = fila["neu"].get()
        payload[f"apo_{i}"] = fila["apo"].get()
        payload[f"lid_{i}"] = fila["lid"].get()
        payload[f"pod_{i}"] = fila["poder"].get()
        payload[f"int_{i}"] = fila["interes"].get()
        payload[f"est_{i}"] = fila["estrategia"].get()
        
    return payload