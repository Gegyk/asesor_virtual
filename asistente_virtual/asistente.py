import speech_recognition as sr
import subprocess as subp
import pyttsx3
import os

# Crear un objeto Recognizer y Pyttx3 (voz)
recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 150) 

def escuchar():
    # Abrir el micrófono para capturar audio
    with sr.Microphone() as source:
        print("ecuchando")
        audio = recognizer.listen(source, timeout=5)
        print("¡Escucha terminada!")

    # Intentar reconocer el texto usando el reconocimiento de voz a texto
    try:
        texto = recognizer.recognize_google(audio, language='es-ES') 
        print(texto)
        return texto
    except Exception:
        pass
        

operaciones = [
    "cerrar asesor",
    "abre steam",
    "abre google",
    "abre ópera",
    "abre el minecraft",
    "apaga el ordenador",
    "abre visual studio",
    "abre discord",
    "abre soldiers"
]

funcionamiento = True

while funcionamiento:
    try:
        texto = escuchar()
        texto = texto.lower()

        if texto == "oye ordenador":
            texto = escuchar()
            texto = texto.lower()

            engine.say("¿Que es lo que estas buscando?")
            engine.runAndWait()

            if texto == operaciones[0]:
                funcionamiento = False
            if texto == operaciones[1]:
                subp.run("C:\Program Files (x86)\Steam\steam.exe")
            if texto == operaciones[2]:
                subp.run("C:\Program Files\Google\Chrome\Application\chrome.exe")
            if texto == operaciones[3]:
                subp.run("C:\\Users\\ruben\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
            if texto == operaciones[4]:
                subp.run("C:\\Users\\ruben\\Desktop\\Minecraft Launcher.lnk", shell=True)
            if texto == operaciones[5]:
                os.system("shutdown /s /t 0")
            if texto == operaciones[6]:
                subp.run("C:\\Users\\ruben\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            if texto == operaciones[7]:
                subp.run("C:\\Users\\ruben\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
            if texto == operaciones[8]:
                subp.run("E:\\Steam\\steamapps\\common\\Souldiers")
    except Exception:
        pass

        

        

    
