import tkinter as tk
from tkinter import ttk

vars_tablas = {}

# Variables para las listas dinámicas de la Tabla 4
vars_inc_tec, vars_inc_ope, vars_inc_fin, vars_inc_rh, vars_inc_com = [], [], [], [], []

def agregar_inclusion(lista_vars, parent_frame, txt=""):
    row = len(lista_vars)
    v_chk = tk.BooleanVar(value=True)
    v_txt = tk.StringVar(value=txt)
    tk.Checkbutton(parent_frame, variable=v_chk, bg="#ecf0f1").grid(row=row, column=0, sticky="w")
    tk.Entry(parent_frame, textvariable=v_txt, width=60).grid(row=row, column=1, pady=2, sticky="w")
    lista_vars.append({"activo": v_chk, "texto": v_txt})

def render_tablas_alcance(parent_frame):
    global vars_inc_tec, vars_inc_ope, vars_inc_fin, vars_inc_rh, vars_inc_com
    vars_inc_tec, vars_inc_ope, vars_inc_fin, vars_inc_rh, vars_inc_com = [], [], [], [], []

    # ==========================================
    # TABLA 1: Atributos del Proyecto
    # ==========================================
    tk.Label(parent_frame, text="1. Atributos del Proyecto", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(10,5))
    f1 = tk.Frame(parent_frame, bg="#ecf0f1")
    f1.pack(fill="x", pady=5)
    
    attr_nombres = ["Nombre del proyecto", "Acrónimo", "Sector / giro", "Mercado Meta", "Duración total", "Presupuesto", "Stack Tecnológico", "Metodología"]
    det_default = ["Testify", "TFY", "Tecnologías de la información / servicios", "6 empresas de TI en la alcaldía Cuauhtémoc", "12 meses", "$14,462,590 MXN", "AWS, PostgreSQL, APIs de IA, Python y Framewoeks web", "Scrum"]
    
    for i in range(1, 9):
        vars_tablas[f'at_{i}'] = tk.StringVar(value=attr_nombres[i-1])
        vars_tablas[f'det_{i}'] = tk.StringVar(value=det_default[i-1])
        row = tk.Frame(f1, bg="#ecf0f1")
        row.pack(fill="x")
        tk.Entry(row, textvariable=vars_tablas[f'at_{i}'], width=25).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f'det_{i}'], width=60).pack(side="left", padx=2, pady=2)

    # ==========================================
    # TABLA 2: Entregables
    # ==========================================
    tk.Label(parent_frame, text="2. Entregables principales del Proyecto", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f2 = tk.Frame(parent_frame, bg="#ecf0f1")
    f2.pack(fill="x", pady=5)
    
    ent_default = ["Software Testify", "Módulo de IA", "MVP", "Base de Datos", "Manual Técnico", "Reportes QA", "Plan Comercial", "Contratos de venta", "Plan de soporte"]
    des2_default = ["Plataforma funcional en la nube", "Generación automática de reportes", "Prototipos funcional validado", "Sistema PostgreSQL configurado", "Documentación del Sistema", "Resultado de pruebas", "Estrategia de mercado", "Licencias vendidas", "Servicio post-venta"]
    res2_default = ["Tecnológico", "Tecnológico", "Tecnológico", "Tecnológico", "Operativo", "Operativo", "Comercial", "Comercial", "Comercial"]

    for i in range(1, 10):
        vars_tablas[f't2_ent_{i}'] = tk.StringVar(value=ent_default[i-1])
        vars_tablas[f't2_des_{i}'] = tk.StringVar(value=des2_default[i-1])
        vars_tablas[f't2_res_{i}'] = tk.StringVar(value=res2_default[i-1])
        row = tk.Frame(f2, bg="#ecf0f1")
        row.pack(fill="x")
        tk.Entry(row, textvariable=vars_tablas[f't2_ent_{i}'], width=25).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f't2_des_{i}'], width=40).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f't2_res_{i}'], width=20).pack(side="left", padx=2, pady=2)

    # ==========================================
    # TABLA 3: Criterios de Aceptación
    # ==========================================
    tk.Label(parent_frame, text="3. Criterios de Aceptación", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f3 = tk.Frame(parent_frame, bg="#ecf0f1")
    f3.pack(fill="x", pady=5)
    
    t3_ent = ["Software Testify", "Módulo de IA", "MVP", "Base de Datos", "Manual Técnico", "UI"]
    t3_cri = ["Funciona al 100% sin errores críticos", "Genera reportes en un 95% y que sean correctos", "Validado al 100% por usuarios piloto", "Almacenamiento al 100%", "Completo al 100% y entendible ante los usuarios", "Fácil navegación y uso al 95%."]
    t3_res = ["Cliente", "QA", "Cliente", "DevOps", "Operativo", "Usuario Final"]

    for i in range(1, 7):
        vars_tablas[f't3_ent_{i}'] = tk.StringVar(value=t3_ent[i-1])
        vars_tablas[f't3_cri_{i}'] = tk.StringVar(value=t3_cri[i-1])
        vars_tablas[f't3_res_{i}'] = tk.StringVar(value=t3_res[i-1])
        row = tk.Frame(f3, bg="#ecf0f1")
        row.pack(fill="x")
        tk.Entry(row, textvariable=vars_tablas[f't3_ent_{i}'], width=25).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f't3_cri_{i}'], width=50).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f't3_res_{i}'], width=15).pack(side="left", padx=2, pady=2)

    # ==========================================
    # TABLA 4: Inclusiones (Dinámica)
    # ==========================================
    tk.Label(parent_frame, text="4. Inclusiones (Trabajo Incluido)", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f4 = tk.Frame(parent_frame, bg="#ecf0f1")
    f4.pack(fill="x", pady=5)

    def render_area_inc(titulo, lista_vars, defaults):
        tk.Label(f4, text=titulo, bg="#ecf0f1", font=("Arial", 9, "bold")).pack(anchor="w", pady=(5,0))
        frame_area = tk.Frame(f4, bg="#ecf0f1")
        frame_area.pack(fill="x", padx=10)
        for txt in defaults:
            agregar_inclusion(lista_vars, frame_area, txt)
        tk.Button(f4, text=f"➕ Agregar a {titulo}", bg="#34495e", fg="white", font=("Arial", 8), command=lambda l=lista_vars, f=frame_area: agregar_inclusion(l, f, "")).pack(anchor="w", padx=10, pady=2)

    render_area_inc("Tecnológica:", vars_inc_tec, ["Desarrollo de Sofware", "Plan operativo", "Plan general de trabajo", "Plan de comercialización", "Estudio y estratificación de mercado", "El código fuente esta registrado como inautor"])
    render_area_inc("Operativa:", vars_inc_ope, ["Diseño de Software", "Documentación de pruebas y validación", "Manual técnico"])
    render_area_inc("Financiera:", vars_inc_fin, ["Gestión de presupuesto", "Afiliaciones con patrocinadores", "Proyección financiera", "Esquema de pagos", "Balances generales"])
    render_area_inc("Recursos Humanos:", vars_inc_rh, ["Contratación de personal", "Capacitación al personal", "Diseño de talleres formativos", "Encuestas"])
    render_area_inc("Comercial:", vars_inc_com, ["Ventas del software", "Marketing", "Posicionamiento en el mercado"])

    # ==========================================
    # TABLA 5: Exclusiones
    # ==========================================
    tk.Label(parent_frame, text="5. Exclusiones", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f5 = tk.Frame(parent_frame, bg="#ecf0f1")
    f5.pack(fill="x", pady=5)

    t5_exc = ["Desarrollo de hardware", "Soporte limitado", "Implementación fuera de CDMX", "Personalización Total del Sofware", "Solo en empresas de TI"]
    t5_jus = ["No es objetivo del proyecto", "Solo soporte definido por SLA", "Alcance geográfico limitado", "Solo plantillas definidas", "Solo se venderá el software a empresas de TI por el objetivo del proyecto"]

    for i in range(1, 6):
        vars_tablas[f't5_exc_{i}'] = tk.StringVar(value=t5_exc[i-1])
        vars_tablas[f't5_jus_{i}'] = tk.StringVar(value=t5_jus[i-1])
        row = tk.Frame(f5, bg="#ecf0f1")
        row.pack(fill="x")
        tk.Entry(row, textvariable=vars_tablas[f't5_exc_{i}'], width=40).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f't5_jus_{i}'], width=55).pack(side="left", padx=2, pady=2)

    # ==========================================
    # TABLA 6: Restricciones del Proyecto
    # ==========================================
    tk.Label(parent_frame, text="6. Restricciones del Proyecto", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f6 = tk.Frame(parent_frame, bg="#ecf0f1")
    f6.pack(fill="x", pady=5)

    t6_res = ["Presupuesto", "Tiempo", "Recursos humanos", "Tecnología", "Mercado"]
    t6_des = ["Solo tenemos un límite de presupuesto de $14,462,590 MXN", "Lo tenemos que realizar en un periodo de 12 meses.", "Tenemos un equipo limitado que se compro y se contrato", "Se tiene una dependencia solamente con AWS", "Solo esta enfocado en la CDMX como mercado meta, objetivo y potencial"]
    t6_tip = ["Económico", "Temporal", "Organizacional", "Técnica", "Comercial"]
    t6_imp = ["Alto", "Alto", "Medio", "Alto", "Medio"]

    for i in range(1, 6):
        vars_tablas[f't6_res_{i}'] = tk.StringVar(value=t6_res[i-1])
        vars_tablas[f't6_des_{i}'] = tk.StringVar(value=t6_des[i-1])
        vars_tablas[f't6_tip_{i}'] = tk.StringVar(value=t6_tip[i-1])
        vars_tablas[f't6_imp_{i}'] = tk.StringVar(value=t6_imp[i-1])
        row = tk.Frame(f6, bg="#ecf0f1")
        row.pack(fill="x")
        tk.Entry(row, textvariable=vars_tablas[f't6_res_{i}'], width=20).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f't6_des_{i}'], width=45).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f't6_tip_{i}'], width=15).pack(side="left", padx=2, pady=2)
        ttk.Combobox(row, textvariable=vars_tablas[f't6_imp_{i}'], values=["Bajo", "Medio", "Alto"], state="readonly", width=8).pack(side="left", padx=2, pady=2)

    # ==========================================
    # TABLA 7: Supuestos (Parte 1)
    # ==========================================
    tk.Label(parent_frame, text="7. Supuestos del Proyecto", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f7 = tk.Frame(parent_frame, bg="#ecf0f1")
    f7.pack(fill="x", pady=5)

    t7_sup = ["Disponibilidad de equipo", "Infraestructura", "Clientes", "Tecnología", "Financiamiento"]
    t7_des = ["Personal contratado a tiempo", "AWS disponible sin fallos", "Aceptación del 73% del mercado", "APIs de IA funcionales", "Recursos disponibles y disponibilidad de financiamiento antes de la Etapa 2."]

    for i in range(1, 6):
        vars_tablas[f't7_sup_{i}'] = tk.StringVar(value=t7_sup[i-1])
        vars_tablas[f't7_des_{i}'] = tk.StringVar(value=t7_des[i-1])
        row = tk.Frame(f7, bg="#ecf0f1")
        row.pack(fill="x")
        tk.Entry(row, textvariable=vars_tablas[f't7_sup_{i}'], width=25).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f't7_des_{i}'], width=70).pack(side="left", padx=2, pady=2)

    # ==========================================
    # TABLA 8: Supuestos del Proyecto (Actividades)
    # ==========================================
    tk.Label(parent_frame, text="8. Supuestos del Proyecto (Actividades)", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f8 = tk.Frame(parent_frame, bg="#ecf0f1")
    f8.pack(fill="x", pady=5)

    t8_act = ["Solicitud", "Evaluación", "Aprobación", "Implementación", "Validación", "Documentación"]
    t8_des = ["El cliente solicita un cambio oportuno en el software", "Se analiza el impacto que puede tener", "El comité decide el cambio adecuado", "Se ejecuta el cambio a realizar", "Se verifica el resultado por el cliente y funcionamiento correcto del mismo", "Se actualiza el proyecto"]

    for i in range(1, 7):
        vars_tablas[f't8_act_{i}'] = tk.StringVar(value=t8_act[i-1])
        vars_tablas[f't8_des_{i}'] = tk.StringVar(value=t8_des[i-1])
        row = tk.Frame(f8, bg="#ecf0f1")
        row.pack(fill="x")
        tk.Entry(row, textvariable=vars_tablas[f't8_act_{i}'], width=25).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f't8_des_{i}'], width=70).pack(side="left", padx=2, pady=2)

    # ==========================================
    # TABLA G: Validación y Alcance
    # ==========================================
    tk.Label(parent_frame, text="G. Validación y alcance", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    fg = tk.Frame(parent_frame, bg="#ecf0f1")
    fg.pack(fill="x", pady=5)

    tg_act = ["Revisión de entregables", "Pruebas funcionales", "Aprobación formal de los líderes", "Aprobación formal"]
    tg_des = ["Validación con cliente", "QA verifica el funcionamiento del software", "Firma de actas por parte del líder, el patrocinador y los directores para avalar que todo se entregó correctamente", "Cliente acepta los entregables en tiempo y forma"]

    for i in range(1, 5):
        vars_tablas[f'tg_act_{i}'] = tk.StringVar(value=tg_act[i-1])
        vars_tablas[f'tg_des_{i}'] = tk.StringVar(value=tg_des[i-1])
        row = tk.Frame(fg, bg="#ecf0f1")
        row.pack(fill="x")
        tk.Entry(row, textvariable=vars_tablas[f'tg_act_{i}'], width=35).pack(side="left", padx=2, pady=2)
        tk.Entry(row, textvariable=vars_tablas[f'tg_des_{i}'], width=60).pack(side="left", padx=2, pady=2)


def get_tablas_alcance():
    data = {}
    # Mapeo Tabla 1
    for i in range(1, 9):
        data[f'atributo{i}'] = vars_tablas[f'at_{i}'].get()
        data[f'detalle{i}'] = vars_tablas[f'det_{i}'].get()
    
    # Mapeo Tabla 2
    for i in range(1, 10):
        data[f'entregable{i}'] = vars_tablas[f't2_ent_{i}'].get()
        data[f'descripcion{i}'] = vars_tablas[f't2_des_{i}'].get()
        data[f'responsable{i}'] = vars_tablas[f't2_res_{i}'].get()
        
    # Mapeo Tabla 3
    for i in range(1, 7):
        data[f'ent{i}'] = vars_tablas[f't3_ent_{i}'].get()
        data[f'criterio{i}'] = vars_tablas[f't3_cri_{i}'].get()
        data[f'res{i}'] = vars_tablas[f't3_res_{i}'].get()
        
    # Mapeo Tabla 4 (Dinámica)
    data["inc_tec"] = [{"texto": v["texto"].get()} for v in vars_inc_tec if v["activo"].get()]
    data["inc_ope"] = [{"texto": v["texto"].get()} for v in vars_inc_ope if v["activo"].get()]
    data["inc_fin"] = [{"texto": v["texto"].get()} for v in vars_inc_fin if v["activo"].get()]
    data["inc_rh"] = [{"texto": v["texto"].get()} for v in vars_inc_rh if v["activo"].get()]
    data["inc_com"] = [{"texto": v["texto"].get()} for v in vars_inc_com if v["activo"].get()]

    # Mapeo Tabla 5
    for i in range(1, 6):
        data[f'exclusion{i}'] = vars_tablas[f't5_exc_{i}'].get()
        data[f'justificacion{i}'] = vars_tablas[f't5_jus_{i}'].get()

    # Mapeo Tabla 6
    for i in range(1, 6):
        data[f'restPro{i}'] = vars_tablas[f't6_res_{i}'].get()
        data[f'descPro{i}'] = vars_tablas[f't6_des_{i}'].get()
        data[f'tipo{i}'] = vars_tablas[f't6_tip_{i}'].get()
        data[f'impacto{i}'] = vars_tablas[f't6_imp_{i}'].get()

    # Mapeo Tabla 7
    for i in range(1, 6):
        data[f'supuesto{i}'] = vars_tablas[f't7_sup_{i}'].get()
        data[f'desSup{i}'] = vars_tablas[f't7_des_{i}'].get()

    # Mapeo Tabla 8
    for i in range(1, 7):
        data[f'actSup{i}'] = vars_tablas[f't8_act_{i}'].get()
        data[f'desSupPro{i}'] = vars_tablas[f't8_des_{i}'].get()

    # Mapeo Tabla G
    for i in range(1, 5):
        data[f'actVal{i}'] = vars_tablas[f'tg_act_{i}'].get()
        data[f'desVal{i}'] = vars_tablas[f'tg_des_{i}'].get()

    return data