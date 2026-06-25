import tkinter as tk
from tkinter import ttk

vars_tablas = {}

def render_tablas_pdp(parent_frame):
    # Tabla 1: Versiones
    tk.Label(parent_frame, text="1. Control de Versiones", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(10,5))
    f1 = tk.Frame(parent_frame, bg="#ecf0f1")
    f1.pack(fill="x")
    campos_t1 = [("versionPDP", "1.0", 5), ("HechaPDP", "Alexis Daniel Romero Razo", 30), ("RevisadaPDP", "Equipo de proyecto", 25), ("AprobadaPDP", "", 20), ("FechaPDP", "25 de abril de 2026", 20)]
    for i, (k, v, w) in enumerate(campos_t1):
        vars_tablas[k] = tk.StringVar(value=v)
        tk.Entry(f1, textvariable=vars_tablas[k], width=w).pack(side="left", padx=2)

    # Tabla 2: Nombre
    tk.Label(parent_frame, text="2. Nombre y Siglas", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f2 = tk.Frame(parent_frame, bg="#ecf0f1")
    f2.pack(fill="x")
    vars_tablas['nombreProyPDP'] = tk.StringVar(value="Testify")
    vars_tablas['siglasPDP'] = tk.StringVar(value="TFY")
    tk.Entry(f2, textvariable=vars_tablas['nombreProyPDP'], width=30).pack(side="left", padx=2)
    tk.Entry(f2, textvariable=vars_tablas['siglasPDP'], width=15).pack(side="left", padx=2)

    # Tabla 3: Ciclo de vida (5 filas)
    tk.Label(parent_frame, text="3. Ciclo de Vida del Proyecto", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f3 = tk.Frame(parent_frame, bg="#ecf0f1")
    f3.pack(fill="x")
    t3_fases = ["1. Gestión del Proyecto", "2. Contratos", "3. Curso de Gestión de Proyectos", "4. Curso de Gestión con MS Project", "5. Informes"]
    t3_ent = ["Acta, Alcance, EDT, Presupuesto", "Contratos AWS y clientes", "Informes, RRHH, Roles", "Cronograma en MS Project", "Informe Final"]
    t3_ini = ["Aprobación de acta y alcance", "Identificación de proveedores", "Disponibilidad del equipo", "Definición de EDT", "Recopilación de información"]
    t3_fin = ["Validación de documentos", "Firma y validación de contratos", "Confirmación de recursos asignados", "Validación del cronograma", "Entrega del informe final y cierre"]
    suf = ["", "2", "3", "4", "5"]
    for i in range(5):
        vars_tablas[f'Fase{suf[i]}PDP'] = tk.StringVar(value=t3_fases[i])
        vars_tablas[f'Entregable{suf[i]}PDP'] = tk.StringVar(value=t3_ent[i])
        vars_tablas[f'ConIni{suf[i]}PDP'] = tk.StringVar(value=t3_ini[i])
        vars_tablas[f'ConCierre{suf[i]}PDP'] = tk.StringVar(value=t3_fin[i])
        r = tk.Frame(f3, bg="#ecf0f1")
        r.pack(fill="x", pady=2)
        tk.Entry(r, textvariable=vars_tablas[f'Fase{suf[i]}PDP'], width=25).pack(side="left", padx=2)
        tk.Entry(r, textvariable=vars_tablas[f'Entregable{suf[i]}PDP'], width=30).pack(side="left", padx=2)
        tk.Entry(r, textvariable=vars_tablas[f'ConIni{suf[i]}PDP'], width=35).pack(side="left", padx=2)
        tk.Entry(r, textvariable=vars_tablas[f'ConCierre{suf[i]}PDP'], width=35).pack(side="left", padx=2)

    # Tabla 4: Procesos (15 filas)
    tk.Label(parent_frame, text="4. Procesos de Dirección", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f4 = tk.Frame(parent_frame, bg="#ecf0f1")
    f4.pack(fill="x")
    t4_niv = ["Una sola vez, al inicio"] * 2 + ["Al inicio, actualizable"] + ["Inicio del proyecto"] * 6 + ["Durante todo el proyecto", "Durante el proyecto", "Durante el proyecto", "Durante todo el proyecto", "Durante todo el proyecto", "Durante la ejecución"]
    t4_her = ["Plantillas de gestión", "Plantillas, análisis", "Plantillas, Scrum", "Plantillas, análisis", "Técnica descomposición", "MS Project", "Estimación de costos", "Estándares de calidad", "Organigramas", "Herramientas de comunicación", "Análisis de riesgos", "Análisis make or buy", "Metodología Scrum", "Valor ganado", "Reportes"]
    t4_in = ["Idea, necesidades", "Acta, requerimientos", "Acta, alcance preliminar", "Alcance, plan", "Alcance del proyecto", "EDT, actividades", "Cronograma, recursos", "Plan del proyecto", "Plan del proyecto", "Plan del proyecto", "Plan del proyecto", "Alcance, recursos", "Plan del proyecto", "Datos de desempeño", "Datos del proyecto"]
    t4_mod = ["Reuniones patrocinador", "Reuniones de equipo", "Reuniones de equipo", "Trabajo colaborativo", "Reuniones de equipo", "Planeación de equipo", "Análisis financiero", "Definición estándares", "Asignación de roles", "Reuniones periódicas", "Evaluación de riesgos", "Negociación", "Sprints", "Monitoreo continuo", "Presentación de avances"]
    t4_out = ["Acta de constitución", "Doc. de alcance", "Plan de dirección", "Plan de alcance", "EDT y diccionario", "Cronograma", "Presupuesto", "Plan de calidad", "Roles", "Plan de comunicaciones", "Plan de riesgos", "Plan de adquisiciones", "Entregables", "Reportes de avance", "Informes de rendimiento"]
    for i in range(1, 16):
        vars_tablas[f'NIVEL{i}_PDP'] = tk.StringVar(value=t4_niv[i-1])
        vars_tablas[f'HER{i}_PDP'] = tk.StringVar(value=t4_her[i-1])
        vars_tablas[f'IN{i}_PDP'] = tk.StringVar(value=t4_in[i-1])
        vars_tablas[f'MODO{i}_PDP'] = tk.StringVar(value=t4_mod[i-1])
        vars_tablas[f'OP{i}_PDP'] = tk.StringVar(value=t4_out[i-1])
        r = tk.Frame(f4, bg="#ecf0f1")
        r.pack(fill="x", pady=1)
        tk.Entry(r, textvariable=vars_tablas[f'NIVEL{i}_PDP'], width=22).pack(side="left", padx=1)
        tk.Entry(r, textvariable=vars_tablas[f'HER{i}_PDP'], width=22).pack(side="left", padx=1)
        tk.Entry(r, textvariable=vars_tablas[f'IN{i}_PDP'], width=22).pack(side="left", padx=1)
        tk.Entry(r, textvariable=vars_tablas[f'MODO{i}_PDP'], width=22).pack(side="left", padx=1)
        tk.Entry(r, textvariable=vars_tablas[f'OP{i}_PDP'], width=22).pack(side="left", padx=1)

    # Tabla 5: Revisión de Gestión (5 filas)
    tk.Label(parent_frame, text="5. Revisión de Gestión", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f5 = tk.Frame(parent_frame, bg="#ecf0f1")
    f5.pack(fill="x")
    t5_con = ["Revisión de acuerdos y avances", "Informe de desempeño", "Análisis de problemas/riesgos", "Presentación de avances", "Intercambio de información"]
    t5_ext = ["Participa todo el equipo", "Evaluación del avance general", "Solo equipo involucrado", "Revisión de entregables", "Facilita coordinación diaria"]
    t5_opo = ["Semanal (lunes)", "Semanal", "Cuando se requiera", "Según solicitud", "En cualquier momento"]
    for i in range(1, 6):
        vars_tablas[f'CONTE{i}_PDP'] = tk.StringVar(value=t5_con[i-1])
        vars_tablas[f'EXTEAL{i}_PDP'] = tk.StringVar(value=t5_ext[i-1])
        vars_tablas[f'OPORTU{i}_PDP'] = tk.StringVar(value=t5_opo[i-1])
        r = tk.Frame(f5, bg="#ecf0f1")
        r.pack(fill="x", pady=1)
        tk.Entry(r, textvariable=vars_tablas[f'CONTE{i}_PDP'], width=40).pack(side="left", padx=2)
        tk.Entry(r, textvariable=vars_tablas[f'EXTEAL{i}_PDP'], width=40).pack(side="left", padx=2)
        tk.Entry(r, textvariable=vars_tablas[f'OPORTU{i}_PDP'], width=30).pack(side="left", padx=2)

    # Tabla 6: Adjuntos (18 filas)
    tk.Label(parent_frame, text="6. Planes Adjuntos (SÍ/NO)", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f6 = tk.Frame(parent_frame, bg="#ecf0f1")
    f6.pack(fill="x")
    t6_defaults = ["Sí", "Sí", "Sí", "Sí", "No", "Sí", "No", "No", "No", "Sí", "No", "No", "Sí", "No", "Sí", "No", "Sí", "Sí"]
    for i in range(1, 19):
        vars_tablas[f'AD{i}_PDP'] = tk.StringVar(value=t6_defaults[i-1])
        ttk.Combobox(f6, textvariable=vars_tablas[f'AD{i}_PDP'], values=["Sí", "No"], state="readonly", width=5).grid(row=(i-1)//6, column=(i-1)%6, padx=5, pady=2)

def get_tablas_pdp_data():
    return {k: v.get() for k, v in vars_tablas.items()}