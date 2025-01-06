import os
import subprocess

def fix_mp4_metadata(input_file, output_file):
    try:
        # Comando ffmpeg para copiar el contenido y reescribir los metadatos
        command = [
            r'C:\ffmpeg\bin\ffmpeg.exe',  # Ruta completa al ejecutable
            '-i', input_file,
            '-c', 'copy',  # Copiar sin recodificar
            '-map', '0',   # Incluir todos los streams
            '-movflags', 'faststart',  # Reorganizar para streaming y metadatos
            output_file
        ]
        # Ejecutar el comando ffmpeg
        subprocess.run(command, check=True)

        print(f"Metadatos arreglados: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error al procesar {input_file}: {e}")

def batch_fix_mp4_metadata(input_folder, output_folder):
    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Iterar sobre cada archivo en la carpeta de entrada
    for file in os.listdir(input_folder):
        # Verificar si el archivo es un archivo de video MP4
        if file.endswith(".mp4"):
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, file)

            # Arreglar metadatos del archivo MP4
            fix_mp4_metadata(input_file, output_file)

# Carpeta de entrada y carpeta de salida
input_folder = r"C:\Users\ruben\Desktop\pelis\Jojo\Battle Tendency"
output_folder = r"C:\Users\ruben\Desktop\pelis\Jojo\Battle Tendency\mp4"

# Llamada a la función para procesar los archivos MP4
batch_fix_mp4_metadata(input_folder, output_folder)
