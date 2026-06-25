import tkinter as tk
from tkinter import ttk

vars_tablas = {}

def render_tablas_gr(parent_frame):
    # TABLA 1: Info General
    tk.Label(parent_frame, text="1. Información general del proyecto", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(10,5))
    f1 = tk.Frame(parent_frame, bg="#ecf0f1")
    f1.pack(fill="x")
    vars_tablas.update({
        'nomProy_GR': tk.StringVar(value="Diseño y desarrollo de un software único de pruebas de documentación para las empresas de TI en la CDMX."),
        'resProy_GR': tk.StringVar(value="Alexis Daniel Romero Razo."),
        'fechaInicio_GR': tk.StringVar(value="3/Febrero/2026"),
        'versionDoc_GR': tk.StringVar(value="V1.0."),
        'descGeneral_GR': tk.StringVar(value="Sistema basado en Inteligencia Artificial diseñado para optimizar los flujos de trabajo de documentación de pruebas en empresas de tecnología. El software automatiza la creación de reportes ejecutivos y técnicos, transformando datos de pruebas (CSV) en documentos narrativos (Word/PDF), aumentando la eficiencia operativa y reduciendo errores manuales.")
    })
    campos_t1 = [("Nombre del proyecto:", 'nomProy_GR', 90), ("Responsable:", 'resProy_GR', 40), ("Fecha de inicio:", 'fechaInicio_GR', 20), ("Versión:", 'versionDoc_GR', 10), ("Descripción general:", 'descGeneral_GR', 90)]
    for lbl, var, w in campos_t1:
        r = tk.Frame(f1, bg="#ecf0f1")
        r.pack(fill="x", pady=2)
        tk.Label(r, text=lbl, bg="#ecf0f1", width=20, anchor="e").pack(side="left")
        tk.Entry(r, textvariable=vars_tablas[var], width=w).pack(side="left", padx=5)

    # TABLA 2: 24 Requerimientos
    tk.Label(parent_frame, text="2. Tabla de Requerimientos", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f2 = tk.Frame(parent_frame, bg="#ecf0f1")
    f2.pack(fill="x")
    
    nombres = ["Registro y Autenticación", "Gestión de Perfiles", "Panel de Control", "Generación con IA", "Clasificación de Errores", "Exportación de Reportes", "Integración de Herramientas", "Base de Datos Central", "Actualización Real-Time", "Historial de Versiones", "Edición Colaborativa", "Notificaciones Críticas", "Disponibilidad (Uptime)", "Compatibilidad Web", "Tiempo de Respuesta", "Seguridad Cloud", "Escalabilidad", "Accesibilidad", "Cifrado de Información", "Logs de Auditoría", "Portabilidad Cloud", "Metodología Scrum", "Respaldo de Datos", "Gobierno de TI"]
    descripciones = ["Permitir el acceso mediante credenciales seguras.", "Roles de administradores, testers y desarrolladores.", "Interfaz centralizada para visualizar resultados.", "Automatización de reportes desde archivos CSV.", "Categorización de hallazgos por severidad.", "Generación de archivos en Word y PDF.", "Conexión con GitHub y Jira Enterprise.", "Persistencia de datos en servidor PostgreSQL.", "Sincronización inmediata del panel de control.", "Acceso a reportes y versiones anteriores.", "Consulta y edición simultánea por el equipo.", "Alertas automáticas sobre fallas o terminación.", "Garantizar el 99.5% de tiempo de actividad.", "Soporte para Chrome, Edge, Firefox y Safari.", "Máximo de 3 segundos por acción.", "Autenticación multifactor y encriptación.", "Ajuste automático de recursos según demanda.", "Cumplimiento con pautas WCAG 2.1.", "Protocolos HTTPS/TLS y AES-256.", "Registro inalterable de acciones críticas.", "Flexibilidad entre AWS, Azure y GCP.", "Entregas funcionales cada 15 días.", "Backups automáticos diarios en la nube.", "Alineación con normas ISO/IEC 27001."]
    tipos = ["Funcional"]*12 + ["No Funcional"]*12
    prioridades = ["Alta", "Media", "Alta", "Alta", "Media", "Alta", "Media", "Alta", "Media", "Media", "Alta", "Media", "Alta", "Media", "Media", "Alta", "Alta", "Baja", "Alta", "Media", "Baja", "Media", "Alta", "Media"]
    responsables = ["Daniel", "Estephany", "Estephany", "Daniel", "Estephany", "Estephany", "Daniel", "Estephany", "Estephany", "Estephany", "Estephany", "Estephany", "Daniel", "Estephany", "Estephany", "Daniel", "Daniel", "Estephany", "Daniel", "Estephany", "Daniel", "Daniel", "Daniel", "Daniel"]
    estados = ["Terminado", "En proceso", "En proceso", "En proceso", "Pendiente", "Pendiente", "Terminado", "Terminado", "En proceso", "Pendiente", "Pendiente", "En proceso", "En proceso", "En proceso", "En proceso", "En proceso", "Pendiente", "Pendiente", "Terminado", "Pendiente", "Pendiente", "En proceso", "Terminado", "En proceso"]
    
    for i in range(1, 25):
        vars_tablas[f'nombre{i}_GR'] = tk.StringVar(value=nombres[i-1])
        vars_tablas[f'd{i}_GR'] = tk.StringVar(value=descripciones[i-1])
        vars_tablas[f't{i}_GR'] = tk.StringVar(value=tipos[i-1])
        vars_tablas[f'p{i}_GR'] = tk.StringVar(value=prioridades[i-1])
        vars_tablas[f'r{i}_GR'] = tk.StringVar(value=responsables[i-1])
        vars_tablas[f'es{i}_GR'] = tk.StringVar(value=estados[i-1])
        
        r = tk.Frame(f2, bg="#ecf0f1")
        r.pack(fill="x", pady=1)
        tk.Entry(r, textvariable=vars_tablas[f'nombre{i}_GR'], width=22).pack(side="left", padx=1)
        tk.Entry(r, textvariable=vars_tablas[f'd{i}_GR'], width=45).pack(side="left", padx=1)
        tk.Entry(r, textvariable=vars_tablas[f't{i}_GR'], width=12).pack(side="left", padx=1)
        ttk.Combobox(r, textvariable=vars_tablas[f'p{i}_GR'], values=["Alta", "Media", "Baja", "Bajo"], state="readonly", width=6).pack(side="left", padx=1)
        tk.Entry(r, textvariable=vars_tablas[f'r{i}_GR'], width=12).pack(side="left", padx=1)
        ttk.Combobox(r, textvariable=vars_tablas[f'es{i}_GR'], values=["Pendiente", "En proceso", "Terminado"], state="readonly", width=12).pack(side="left", padx=1)

    # TABLA 3: Campos (El que te cansó jaja)
    tk.Label(parent_frame, text="3. Definición de Campos", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f3 = tk.Frame(parent_frame, bg="#ecf0f1")
    f3.pack(fill="x")
    vars_tablas.update({
        'nombresuki_GR': tk.StringVar(value="Código único del requerimiento"),
        'descripcionsuki_GR': tk.StringVar(value="Título breve del requerimiento"),
        'eltipo_GR': tk.StringVar(value="Explicación clara del requerimiento"),
        'prioridad_GR': tk.StringVar(value="Funcional / No funcional"),
        'responsablesuki_GR': tk.StringVar(value="Alta / Media / Baja"),
        'yaEstoyCansadoAyuda_GR': tk.StringVar(value="Pendiente / En proceso / Terminado")
    })
    tk.Entry(f3, textvariable=vars_tablas['nombresuki_GR'], width=30).pack(side="left", padx=2)
    tk.Entry(f3, textvariable=vars_tablas['descripcionsuki_GR'], width=30).pack(side="left", padx=2)
    tk.Entry(f3, textvariable=vars_tablas['eltipo_GR'], width=30).pack(side="left", padx=2)

    # TABLA 4: Cambios
    tk.Label(parent_frame, text="4. Control de Cambios", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(anchor="w", pady=(15,5))
    f4 = tk.Frame(parent_frame, bg="#ecf0f1")
    f4.pack(fill="x")
    f_def = ["13/04/2026", "18/04/2026", "22/04/2026", "25/04/2026"]
    req_def = ["RQ-03", "RQ-04", "RQ-08", "RQ-01"]
    cam_def = ["Ajuste en el algoritmo de extracción de texto de la IA.", "Rediseño de la interfaz del Panel de Control para móviles.", "Cambio de servidor de base de datos local a instancia AWS RDS.", "Implementación de validación de correo por token."]
    imp_def = ["Tiempo: +2 días de desarrollo.\nCosto: Sin impacto.", "Tiempo: +3 días.\nCosto: $12,450 MXN (pago de horas extra al equipo operativo).", "Tiempo: -1 día.\nCosto: $4,500 MXN mensuales adicionales de consumo cloud.", "Tiempo: +1 día.\nCosto: Sin impacto."]
    apr_def = ["Daniel Romero", "Estephany Muñoz", "Daniel Romero", "Estephany Muñoz"]
    
    for i in range(1, 5):
        vars_tablas[f'laFecha{i}_GR'] = tk.StringVar(value=f_def[i-1])
        vars_tablas[f'req{i}_GR'] = tk.StringVar(value=req_def[i-1])
        vars_tablas[f'cambios{i}_GR'] = tk.StringVar(value=cam_def[i-1])
        vars_tablas[f'impacto{i}_GR'] = tk.StringVar(value=imp_def[i-1].replace('\n', ' '))
        vars_tablas[f'aprob{i}_GR'] = tk.StringVar(value=apr_def[i-1])
        
        r = tk.Frame(f4, bg="#ecf0f1")
        r.pack(fill="x", pady=1)
        tk.Entry(r, textvariable=vars_tablas[f'laFecha{i}_GR'], width=12).pack(side="left", padx=2)
        tk.Entry(r, textvariable=vars_tablas[f'req{i}_GR'], width=8).pack(side="left", padx=2)
        tk.Entry(r, textvariable=vars_tablas[f'cambios{i}_GR'], width=45).pack(side="left", padx=2)
        tk.Entry(r, textvariable=vars_tablas[f'impacto{i}_GR'], width=45).pack(side="left", padx=2)
        tk.Entry(r, textvariable=vars_tablas[f'aprob{i}_GR'], width=15).pack(side="left", padx=2)

def get_tablas_gr_data():
    return {k: v.get() for k, v in vars_tablas.items()}