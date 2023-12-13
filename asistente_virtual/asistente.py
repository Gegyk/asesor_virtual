import speech_recognition as sr
import subprocess as subp
import pyttsx3
import os


# Crear un objeto Pyttx3 (voz)
recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 180) 

def escuchar():
    try:
        # Crear un objeto Recognizer y Microphone para que el programa no tarde mas en cada vuelta
        recognizer = sr.Recognizer()
        microphono = sr.Microphone()
        # Abrir el micrófono para capturar audio
        with sr.Microphone() as source:
            print("ecuchando")
            audio = recognizer.listen(source, timeout=10)
            print("¡Escucha terminada!")

        # Intentar reconocer el texto usando el reconocimiento de voz a texto
        
        texto = recognizer.recognize_google(audio, language='es-ES') 
        print(texto)
        return texto
    except Exception as e:
        print(e)
        

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

engine.say("Buenos dias, Rubén")
print("hay va")
engine.runAndWait()

while funcionamiento:

    try:
        texto = escuchar()
        texto = texto.lower()

        if texto == "atención ordenador":
            engine.say("¿Que es lo que estas buscando?")
            engine.runAndWait()
            
            texto = escuchar()
            if not isinstance(texto, str):
                engine.say("Lo siento, no entendi lo que me pediste")
                engine.runAndWait()

            texto = texto.lower()

            

            if texto == operaciones[0]:
                #Apaga el asesor virtual
                engine.say("Cerrando tu asesor virtual")
                engine.runAndWait()
                funcionamiento = False
            if texto == operaciones[1]:
                #Abre steam
                engine.say("Abriendo Steam")
                engine.runAndWait()
                subp.run("C:\Program Files (x86)\Steam\steam.exe")
            if texto == operaciones[2]:
                #Abre Google
                engine.say("Abriendo google")
                engine.runAndWait()
                subp.run("C:\Program Files\Google\Chrome\Application\chrome.exe")
            if texto == operaciones[3]:
                #Abre Opera GX
                engine.say("Abriendo Opera GX")
                engine.runAndWait()
                subp.run("C:\\Users\\ruben\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
            if texto == operaciones[4]:
                #Abre el Minecraft
                engine.say("Hora de viciar al Minecraft")
                engine.runAndWait()
                subp.run("C:\\Users\\ruben\\Desktop\\Minecraft Launcher.lnk", shell=True)
            if texto == operaciones[5]:
                #Apaga el ordeandor
                engine.say("Apagando el ordenador")
                engine.runAndWait()
                os.system("shutdown /s /t 0")
            if texto == operaciones[6]:
                #Abre visual studio
                engine.say("Hora de programar. Abriendo visual studio")
                engine.runAndWait()
                subp.run("C:\\Users\\ruben\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            if texto == operaciones[7]:
                #Abre discord
                engine.say("Abriendo discord")
                engine.runAndWait()
                subp.run("C:\\Users\\ruben\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
            if texto == operaciones[8]:
                #Abre el videjuego de steam Souldiers
                engine.say("Abriendo el Souldiers")
                engine.runAndWait()
                subp.run("E:\\Steam\\steamapps\\common\\Souldiers")
            if texto not in operaciones:
                #no entendio la peticion
                engine.say("Lo siento, no entendi lo que me pediste")
                engine.runAndWait()
        
    except Exception:
        pass
