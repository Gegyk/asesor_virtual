from moviepy.editor import VideoFileClip
import os

def convert_to_mp4(input_file, output_file):
    try:
        # Cargar el archivo de video
        video_clip = VideoFileClip(input_file)
        
        # Escribir el video en formato MP4
        video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
        
        print("Conversión exitosa.")
    except Exception as e:
        print("Error durante la conversión:", e)

def batch_convert_to_mp4(input_folder, output_folder):
    # Obtener una lista de todos los archivos en la carpeta de entrada
    files = os.listdir(input_folder)
    
    # Iterar sobre cada archivo en la lista
    for file in files:
        # Verificar si el archivo es un archivo de video
        if file.endswith(".mkv"):
            # Construir las rutas de entrada y salida para el archivo actual
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp4")
            
            # Convertir el archivo a MP4
            convert_to_mp4(input_file, output_file)

# Carpeta de entrada y carpeta de salida
input_folder = r"W:\\"
output_folder = r"W:\\"

# Llamada a la función de conversión masiva
batch_convert_to_mp4(input_folder, output_folder)
