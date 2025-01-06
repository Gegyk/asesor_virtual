import os
import subprocess

def convert_to_mp4(input_file, output_file, audio_stream_index):
    try:
        # Comando ffmpeg para extraer la pista de audio específica y combinarla con el video
        command = [
            r'C:\ffmpeg\bin\ffmpeg.exe',  # Ruta completa al ejecutable
            '-i', input_file,
            '-map', '0:v:0',
            '-map', f'0:a:{audio_stream_index}',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-strict', 'experimental',
            output_file
        ]
        # Ejecutar el comando ffmpeg
        subprocess.run(command, check=True)

        print(f"Conversión exitosa: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error durante la conversión de {input_file}: {e}")

def batch_convert_to_mp4(input_folder, output_folder, audio_stream_index=1):
    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Iterar sobre cada archivo en la carpeta de entrada
    for file in os.listdir(input_folder):
        # Verificar si el archivo es un archivo de video MKV
        if file.endswith(".mkv"):
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp4")

            # Convertir el archivo a MP4 con la pista de audio especificada
            convert_to_mp4(input_file, output_file, audio_stream_index)

# Carpeta de entrada y carpeta de salida
input_folder = r"E:\\pelis\\"
output_folder = r"E:\\pelis\\mp4"

# Llamada a la función de conversión masiva, seleccionando la pista de audio número 2 (índice 1)
batch_convert_to_mp4(input_folder, output_folder, audio_stream_index=3)
