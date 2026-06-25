import os
import time
import platform
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm

def inyectar_datos_en_word(ruta_template, ruta_salida, diccionario_datos, actualizar_barra):
    try:
        actualizar_barra(20, "Leyendo estructura XML del documento...")
        time.sleep(0.4) 
        
        doc = DocxTemplate(ruta_template)
        
        # Procesamiento especial para inyectar imágenes dinámicas
        if "logo_path" in diccionario_datos and os.path.exists(diccionario_datos["logo_path"]):
            # Mm(30) es el tamaño de la imagen. Puedes subirlo a Mm(40) o Mm(50) según encaje en tu tabla
            diccionario_datos["logo"] = InlineImage(doc, diccionario_datos["logo_path"], width=Mm(35))
        else:
            diccionario_datos["logo"] = "" # Deja vacio si no hay imagen
        
        actualizar_barra(50, "Inyectando etiquetas y listas dinámicas...")
        time.sleep(0.4)
        
        doc.render(diccionario_datos)
        
        actualizar_barra(80, "Ensamblando y guardando nuevo documento...")
        time.sleep(0.4)
        
        doc.save(ruta_salida)
        
        actualizar_barra(100, "¡Inyección 100% completada!")
        time.sleep(0.3)
        
        if platform.system() == 'Windows':
            os.startfile(ruta_salida)
            
        return True
    except Exception as e:
        print(f"Error fatal en la inyección XML: {e}")
        return False