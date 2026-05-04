# = EXTRACTOR_TABLAS_PDFLUMBER_EXCEL V.1.0 = 
**Lenguaje:** Python 3.11.9 (version estable recomendada)
---
## Autoría 
- **Equipo:** Nalsani S.A.S. (Ecommerce / Automatización)
- **Área:** Mercadeo 
- **Rol:** Practicante ADSO SENA
- **Encargado:**
- **CCopyright © SENA & Nalsani S.A.S
contacto interno:** *(ajustar según políticas de la empresa en cuanto autoria , acceso y tratamiento de la informacion con la que se ejecuta la API)*
- **Dirigido a:** Maria Angelica Correo Tapia  - Analista Back-Office
---
# 📌 INTRODUCCION 
# 📄 Extractor de Tablas desde PDF por PTR (Proyecto de Automatización)
Este proyecto permite **extraer tablas desde archivos PDF**, limpiar los datos relevantes y generar:

✅ Un archivo **Excel por cada PDF**, con formato estandarizado  
✅ Un archivo **consolidado final** que incluye todas las filas de todos los PDFs procesados  

El script está diseñado para procesar automáticamente cualquier cantidad de archivos PDF (1, 5, 10, 20…).  
Cada PDF debe estar asociado a un **PTR**, y el nombre del archivo debe respetar esa estructura:


# 🚀 1. Objetivo del proyecto

 Leer archivos PDF de una carpeta, extraer tablas específicas, limpiar esos datos, guardarlos individualmente en Excel y finalmente crear un consolidado maestro

---

# 🔧 2. Requerimientos

### ✅ Python 3.10 o 3.11  
(Probado correctamente en Python 3.11)

### ✅ Librerías necesarias

Instálalas con:

```bash
python -m pip install pdfplumber pandas openpyxl

### ✅ Estructura de proyecto 

Extractor_PDF_CAMELOT/
│── main.py
│
├── pdfs/          # Aquí colocas los PDFs a procesar
│     ├── PTR_000177875.pdf
│     ├── PTR_000177876.pdf
│     └── ...
│
└── excel/         # Aquí se generan los archivos Excel de salida
      ├── PTR_000177875.xlsx
      ├── PTR_000177876.xlsx
      └── CONSOLIDADO_PTR.xlsx

### ✅ ===== ¿ COMO EJECUTAR PROYECTO ? =====
1- Ubicar el ficharo 
2- Usar comando: python name_file.py
# Ejemplo: C:\dev\Python_project\Extractor_PDF_CAMELOT> python main.py

📄 Procesando: PTR_000177875.pdf
✅ Excel generado: .../excel/PTR_000177875.xlsx

📌 Archivo unificado creado: .../excel/CONSOLIDADO_PTR.xlsx
🎉 Proceso completado correctamente.


# ✅✅ **TEST.md (COMPLETO)**  
Copia y pega esto en un archivo llamado **TEST.md**:

---

```md
# ✅ Documento de Pruebas — Extractor de Tablas PDF por PTR

Este documento describe las pruebas funcionales realizadas al script `main.py`, así como los criterios de validación para asegurar que el proceso funciona correctamente.

---

# 🧪 1. Preparación del entorno

### ✅ Prerrequisitos instalados

bash:
winget install Python.Python.3
winget install Python.Python.3.11
python --version     # Debe ser 3.10 o 3.11
python -m pip install pdfplumber pandas openpyxl

