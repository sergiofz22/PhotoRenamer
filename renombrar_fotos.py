import os
from tkinter import Tk, filedialog, Label, Button, messagebox
from PIL import Image
from PIL.ExifTags import TAGS


def get_capture_date(image_path):
    """Extrae la fecha de captura de los metadatos EXIF de una imagen."""
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == "DateTimeOriginal":
                return value
    except Exception as e:
        print(f"Error leyendo EXIF de {image_path}: {e}")
    return None


def rename_photos(directory):
    """Renombra las fotos secuencialmente según la fecha de captura más antigua."""
    photos = []

    # Extraer fechas de captura para cada foto
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if not os.path.isfile(file_path) or not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        capture_date = get_capture_date(file_path)
        if capture_date:
            photos.append((file_path, capture_date))
        else:
            print(f"No se pudo extraer la fecha de captura de: {filename}")

    # Ordenar las fotos por fecha de captura
    photos.sort(key=lambda x: x[1])

    # Renombrar las fotos secuencialmente
    count = 1
    for file_path, capture_date in photos:
        new_filename = f"IMG_{count:04d}.jpg"
        new_file_path = os.path.join(directory, new_filename)
        if not os.path.exists(new_file_path):
            os.rename(file_path, new_file_path)
            print(f"Renombrado: {os.path.basename(file_path)} -> {new_filename}")
            count += 1
        else:
            print(f"Ya existe un archivo con el nombre: {new_filename}")

    messagebox.showinfo("Finalizado", "El renombrado secuencial por fecha ha terminado.")


def select_directory():
    """Abre un cuadro de diálogo para seleccionar un directorio."""
    directory = filedialog.askdirectory()
    if directory:
        rename_photos(directory)
    else:
        messagebox.showwarning("Error", "No se seleccionó ningún directorio.")


# Interfaz gráfica con Tkinter
root = Tk()
root.title("Renombrar Fotos por Fecha")
root.geometry("400x200")

label = Label(root, text="Selecciona un directorio con las fotos:", font=("Arial", 14))
label.pack(pady=20)

button = Button(root, text="Seleccionar directorio", command=select_directory, font=("Arial", 12))
button.pack(pady=10)

exit_button = Button(root, text="Salir", command=root.quit, font=("Arial", 12))
exit_button.pack(pady=10)

root.mainloop()
