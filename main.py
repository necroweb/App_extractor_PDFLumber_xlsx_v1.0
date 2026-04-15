import os
import glob
import pdfplumber
import pandas as pd


# ============================================================
# ✅ 1. CONFIGURACIÓN
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_PDFS = os.path.join(BASE_DIR, "pdfs")
CARPETA_SALIDA = os.path.join(BASE_DIR, "excel")

os.makedirs(CARPETA_SALIDA, exist_ok=True)


# ============================================================
# ✅ 2. FUNCIONES DEL PROCESO
# ============================================================

def extraer_tablas(pdf_path):
    """Extrae todas las filas de todas las tablas dentro de un PDF."""
    filas = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tabla = page.extract_table()
            if tabla:
                filas.extend(tabla)

    return filas



def crear_dataframe(filas):
    """Convierte lista de filas en DataFrame con columnas adecuadas."""
    df = pd.DataFrame(filas)

    # Asumimos las primeras 6 columnas del PDF
    df = df.iloc[:, :6]
    df.columns = ["#caja", "ID Contenedor", "Descripción", "Ean", "Cantidad", "Peso"]

    return df



def limpiar_dataframe(df):
    """Limpia texto, cantidad, peso y elimina filas inválidas."""
    
    # Strip general
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # Eliminar filas inválidas de caja
    df = df[df["#caja"].str.strip() != "0"]

    # Limpiar unidad de medida: quitar UND/KIT/etc.
    df["Cantidad"] = df["Cantidad"].str.extract(r"(\d+)")
    df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce")

    return df


def agregar_ptr(df, nombre_pdf):
    """Crea la columna PTR anclada al nombre del archivo."""
    df.insert(0, "PTR", nombre_pdf)
    return df


def eliminar_columnas_no_usadas(df):
    """Elimina columnas #caja y Peso (no se usan en el resultado final)."""
    df = df.drop(columns=["#caja", "Peso"], errors="ignore")
    return df


def guardar_excel(df, nombre_pdf):
    """Guarda un DataFrame como Excel individual."""
    ruta_excel = os.path.join(CARPETA_SALIDA, f"{nombre_pdf}.xlsx")
    df.to_excel(ruta_excel, index=False)
    print(f"✅ Excel generado: {ruta_excel}")


def consolidar_excels():
    """Une todos los excels generados en un solo archivo final."""
    excels = glob.glob(os.path.join(CARPETA_SALIDA, "*.xlsx"))
    df_consolidado = pd.DataFrame()

    for archivo in excels:
        df_temp = pd.read_excel(archivo)
        df_consolidado = pd.concat([df_consolidado, df_temp], ignore_index=True)

    ruta_consolidado = os.path.join(CARPETA_SALIDA, "CONSOLIDADO_PTR.xlsx")
    df_consolidado.to_excel(ruta_consolidado, index=False)

    print(f"\n📌 Archivo unificado creado: {ruta_consolidado}")



# ============================================================
# ✅ 3. FUNCIÓN PRINCIPAL DEL SCRIPT
# ============================================================

def main():
    print("\n🔍 Iniciando procesamiento de PDFs...\n")

    for archivo in os.listdir(CARPETA_PDFS):
        if archivo.lower().endswith(".pdf"):

            ruta_pdf = os.path.join(CARPETA_PDFS, archivo)
            nombre_sin_ext = os.path.splitext(archivo)[0]

            print(f"📄 Procesando: {archivo}")

            filas = extraer_tablas(ruta_pdf)

            if not filas:
                print(f"⚠️ {archivo} NO contiene tablas, omitido.\n")
                continue

            df = crear_dataframe(filas)
            df = limpiar_dataframe(df)
            df = agregar_ptr(df, nombre_sin_ext)
            df = eliminar_columnas_no_usadas(df)
            guardar_excel(df, nombre_sin_ext)

    consolidar_excels()
    print("\n🎉 Proceso completado correctamente.\n")



# ============================================================
# ✅ EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    main()