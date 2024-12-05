# Renombrador de Fotos por Fecha de Captura o Secuencia

Este proyecto es una aplicación de escritorio en **Python** que permite renombrar fotos en un directorio según:
1. **Fecha de captura** (extraída de los metadatos EXIF).
2. **Secuencia numérica** (IMG_0001, IMG_0002, etc.) ordenadas por la fecha más antigua.

---

## 🚀 Características

- **Renombrar por Fecha de Captura**: Utiliza los metadatos EXIF de las fotos para renombrarlas con su fecha de captura.
- **Renombrar Secuencialmente**: Ordena las fotos por fecha de captura y les asigna nombres como `IMG_0001`, `IMG_0002`, etc.
- **Interfaz gráfica**: Usa `Tkinter` para proporcionar una interfaz amigable y fácil de usar.
- **Soporte de múltiples formatos**: Compatible con `.jpg`, `.jpeg`, y `.png`.

---

## 🛠️ Instalación

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/sergiofz22/PhotoRenamer.git
   cd PhotoRenamer
   
2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt

   
---

## ⚙️ Uso

1. **Ejecuta la aplicación**:
   - Haz doble clic en el archivo ejecutable (si ya fue generado) o usa `python main.py` desde la terminal.

2. **Selecciona un directorio**:
   - Navega hasta la carpeta que contiene las fotos que deseas renombrar.

3. **Confirma el resultado**:
   - La aplicación renombrará las fotos y mostrará un mensaje de finalización.

---

##  📂 Estructura del Proyecto

![image](https://github.com/user-attachments/assets/9d53cf34-c44b-42c5-bbe2-158e7f2fe63b)

---

##  🧩 Dependencias
Este proyecto utiliza las siguientes bibliotecas:

Pillow: Para extraer y manejar los metadatos EXIF de las fotos.
Tkinter: Para crear la interfaz gráfica.
(Opcional) PyInstaller: Para generar el ejecutable.
Instálalas todas ejecutando:

pip install -r requirements.txt

---

##  🛠️ Generar el Ejecutable
1. Instala PyInstaller:
pip install pyinstaller

2. Genera el ejecutable:
pyinstaller --onefile --noconsole main.py

3. El archivo ejecutable estará en la carpeta dist. Ejecuta el archivo para iniciar la aplicación.

##  🛡️ Licencia
Este proyecto está bajo la Licencia MIT.
