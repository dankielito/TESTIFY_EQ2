import os
import sys

# MAGIA: Redirigir la basura de __pycache__ a una sola carpeta externa
os.environ["PYTHONPYCACHEPREFIX"] = os.path.abspath("basureroCache")

import tkinter as tk
from tkinter import ttk, messagebox
import threading

# Importaciones de los módulos
from modulos.inicio import render_inicio_tab
from modulos.inyector_word import inyectar_datos_en_word
from modulos.actaconstitucion.acta import render_acta_tab, get_datos_acta
from modulos.registrointeresados.registrointeresados import render_interesados_tab, get_datos_interesados

# AQUI IMPORTAMOS LA GESTIÓN DEL ALCANCE
from modulos.gestionalcance.gestionalcance import render_alcance_tab, get_datos_alcance

modulos_check = {}
frames_modulos = {}

def cambiar_pantalla(nombre_modulo):
    for frame in frames_modulos.values():
        frame.pack_forget()
    frames_modulos[nombre_modulo].pack(expand=1, fill="both")

def actualizar_barra(valor, texto):
    progreso_var.set(valor)
    lbl_estado_progreso.config(text=texto)
    ventana.update_idletasks()

def hilo_generacion(payload_global):
    ruta_template = os.path.abspath(os.path.join("templates", "ETAPA_1.docx"))
    carpeta_salida = os.path.abspath("wordGenerado")
    
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
        
    nombre_archivo = "Project_Testify_Eduardo_Angela_Daniel.docx"
    ruta_salida = os.path.join(carpeta_salida, nombre_archivo)
    
    exito = inyectar_datos_en_word(ruta_template, ruta_salida, payload_global, actualizar_barra)
    
    btn_generar.config(state="normal")
    if exito:
        messagebox.showinfo("Éxito", f"Documento {nombre_archivo} generado correctamente en /wordGenerado/")
    else:
        messagebox.showerror("Error", "Ocurrió un error al inyectar el código XML.")
        actualizar_barra(0, "Error en la inyección")

def disparar_generacion():
    payload_global = {}
    
    if modulos_check["Acta Constitucion"].get():
        datos_acta = get_datos_acta()
        if datos_acta is not None:
            payload_global.update(datos_acta)

    if modulos_check["Registro Interesados"].get():
        datos_interesados = get_datos_interesados()
        if datos_interesados is not None:
            payload_global.update(datos_interesados)

    # AQUI RECOLECTAMOS LOS DATOS DE GESTIÓN DEL ALCANCE
    if modulos_check["Gestion de Alcance"].get():
        datos_alcance = get_datos_alcance()
        if datos_alcance is not None:
            payload_global.update(datos_alcance)

    if not payload_global:
        messagebox.showwarning("Aviso", "No has seleccionado módulos para editar.")
        return

    btn_generar.config(state="disabled")
    actualizar_barra(0, "Iniciando proceso...")
    proceso = threading.Thread(target=hilo_generacion, args=(payload_global,))
    proceso.start()

# --- INTERFAZ GRÁFICA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Testify - Editor de Plantillas PMBOK")
ventana.geometry("1100x750")

sidebar = tk.Frame(ventana, bg="#2c3e50", width=250)
sidebar.pack(side="left", fill="y")

contenido_principal = tk.Frame(ventana, bg="#ecf0f1")
contenido_principal.pack(side="right", expand=1, fill="both")

tk.Label(sidebar, text="TESTIFY APP", fg="white", bg="#2c3e50", font=("Arial", 16, "bold")).pack(pady=20)

btn_inicio = tk.Button(sidebar, text="🏠 Inicio", bg="#2980b9", fg="white", font=("Arial", 11, "bold"), relief="flat", command=lambda: cambiar_pantalla("Inicio"))
btn_inicio.pack(fill="x", padx=10, pady=10)

frames_modulos["Inicio"] = tk.Frame(contenido_principal, bg="#ecf0f1")
render_inicio_tab(frames_modulos["Inicio"])

lista_modulos = ["Acta Constitucion", "Registro Interesados", "Gestion de Alcance", "EDT", "Plan Direccion", "Gestion Requerimientos"]

for mod in lista_modulos:
    modulos_check[mod] = tk.BooleanVar(value=True if mod == "Acta Constitucion" else False)
    fila = tk.Frame(sidebar, bg="#2c3e50")
    fila.pack(fill="x", pady=5, padx=10)
    
    chk = tk.Checkbutton(fila, variable=modulos_check[mod], bg="#2c3e50", activebackground="#2c3e50")
    chk.pack(side="left")
    
    btn = tk.Button(fila, text=mod, bg="#34495e", fg="white", anchor="w", relief="flat", command=lambda m=mod: cambiar_pantalla(m))
    btn.pack(side="left", fill="x", expand=1)
    
    frames_modulos[mod] = tk.Frame(contenido_principal, bg="#ecf0f1")

# === CONEXIÓN DE LOS MÓDULOS ACTIVOS ===
render_acta_tab(frames_modulos["Acta Constitucion"])
render_interesados_tab(frames_modulos["Registro Interesados"])
render_alcance_tab(frames_modulos["Gestion de Alcance"]) # AQUI CONECTAMOS LA VISTA

# === MÓDULOS EN CONSTRUCCIÓN ===
modulos_pendientes = ["EDT", "Plan Direccion", "Gestion Requerimientos"]
for mod in modulos_pendientes:
    tk.Label(frames_modulos[mod], text=f"Módulo '{mod}' en construcción...", font=("Arial", 16), bg="#ecf0f1").pack(pady=100)

frame_progreso = tk.Frame(sidebar, bg="#2c3e50")
frame_progreso.pack(side="bottom", fill="x", padx=10, pady=20)

lbl_estado_progreso = tk.Label(frame_progreso, text="", bg="#2c3e50", fg="#bdc3c7", font=("Arial", 9, "italic"))
lbl_estado_progreso.pack(pady=5)

progreso_var = tk.DoubleVar()
barra_progreso = ttk.Progressbar(frame_progreso, variable=progreso_var, maximum=100)
barra_progreso.pack(fill="x", pady=5)

btn_generar = tk.Button(frame_progreso, text="GENERAR ETAPA 1", bg="#27ae60", fg="white", font=("Arial", 12, "bold"), pady=10, command=disparar_generacion)
btn_generar.pack(fill="x", pady=10)

cambiar_pantalla("Inicio")
ventana.mainloop()