import speech_recognition as sr
import subprocess as subp
import os

# Crear un objeto Recognizer
recognizer = sr.Recognizer()

def escuchar():
    # Abrir el micrófono para capturar audio
    with sr.Microphone() as source:
        print("escuchando...")
        audio = recognizer.listen(source)

    # Intentar reconocer el texto usando el reconocimiento de voz a texto
    try:
        texto = recognizer.recognize_google(audio, language='es-ES') 
        print("Texto reconocido:")
        print(texto)
        return texto
    except Exception:
        print("error general")

operaciones = [
    "abre steam",
    "abre google",
    "abre ópera",
    "abre el minecraft",
    "apaga el ordenador",
    "abre visual studio",
    "abre discord",
    "abre soldiers"
]

texto = escuchar()
texto = texto.lower()

if texto == "escucha ordenador":
    texto = escuchar()
    texto = texto.lower()

    if texto == operaciones[0]:
        subp.run("C:\Program Files (x86)\Steam\steam.exe")
    if texto == operaciones[1]:
        subp.run("C:\Program Files\Google\Chrome\Application\chrome.exe")
    if texto == operaciones[2]:
        subp.run("C:\\Users\\ruben\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
    if texto == operaciones[3]:
        subp.run("C:\\Users\\ruben\\Desktop\\Minecraft Launcher.lnk", shell=True)
    if texto == operaciones[4]:
        os.system("shutdown /s /t 0")
    if texto == operaciones[5]:
        subp.run("C:\\Users\\ruben\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    if texto == operaciones[6]:
        subp.run("C:\\Users\\ruben\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
    if texto == operaciones[7]:
        subp.run("E:\\Steam\\steamapps\\common\\Souldiers")

        

        

    
