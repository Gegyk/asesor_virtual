import speech_recognition as sr
import subprocess as subp
import pyautogui
import pyttsx3
import os
import time


# Crear un objeto Pyttx3 (voz)
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 180)

operaciones = [
    "abre steam",
    "abre ópera",
    "abre el minecraft",
    "apaga el ordenador",
    "abre visual studio",
    "abre soldiers",
]

discord = [
    "abre discord",
    "abre discord y conectate a llamada",
]

google = [
    "abre google",
    "busca en google",
    "busca en youtube"
]

funcionamiento = True

def escuchar():
    try:
        # Crear un objeto Recognizer y Microphone para que el programa no tarde mas en cada vuelta
        recognizer = sr.Recognizer()
        microphono = sr.Microphone()
        # Abrir el micrófono para capturar audio
        with sr.Microphone() as source:
            print("ecuchando")
            audio = recognizer.listen(source, timeout=20)
            print("¡Escucha terminada!")

        # Intentar reconocer el texto usando el reconocimiento de voz a texto
        
        texto = recognizer.recognize_google(audio, language='es-ES') 
        print(texto)
        return texto
    except Exception as e:
        print(e)


def operacionesAcciones(texto):
    if texto == operaciones[0]:
        #Abre steam
        engine.say("Abriendo Steam")
        engine.runAndWait()
        subp.run("C:\Program Files (x86)\Steam\steam.exe")
        return True
    if texto == operaciones[1]:
        #Abre Opera GX
        engine.say("Abriendo Opera GX")
        engine.runAndWait()
        subp.run("C:\\Users\\ruben\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
        return True
    if texto == operaciones[2]:
        #Abre el Minecraft
        engine.say("Hora de viciar al Minecraft")
        engine.runAndWait()
        subp.run("C:\\Users\\ruben\\Desktop\\Minecraft Launcher.lnk", shell=True)
        return True
    if texto == operaciones[3]:
        #Apaga el ordeandor
        engine.say("Apagando el ordenador")
        engine.runAndWait()
        os.system("shutdown /s /t 0")
        return True
    if texto == operaciones[4]:
        #Abre visual studio
        engine.say("Hora de programar. Abriendo visual studio")
        engine.runAndWait()
        subp.run("C:\\Users\\ruben\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        return True
    if texto == operaciones[5]:
        #Abre el videjuego de steam Souldiers
        engine.say("Abriendo el Souldiers")
        engine.runAndWait()
        subp.run("E:\\Steam\\steamapps\\common\\Souldiers")
        return True

def discordAcciones(texto):
    # Operaciones de discord
    if texto == discord[0]:
        #Abre discord
        engine.say("Abriendo discord")
        engine.runAndWait()
        subp.run("C:\\Users\\ruben\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
        return True
    if texto == discord[1]:
        #Abre discord y se conecta
        engine.say("Abriendo discord")
        engine.runAndWait()
        subp.run("C:\\Users\\ruben\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
        time.sleep(5)
        pyautogui.click(40, 145)
        pyautogui.click(220, 450)
        return True

def googleAcciones(texto):
    if texto == google[0]:
        #Abre Google
        engine.say("Abriendo google")
        engine.runAndWait()
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        return True
    if texto == google[1]:
        #Hace una busqueda en internet
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        engine.say("Que es lo que quieres que busque")
        engine.runAndWait()
        texto = escuchar()
        if not isinstance(texto, str):
            engine.say("Lo siento, no entendi lo que me pediste")
            engine.runAndWait()
        else:
            subp.run("C:\Program Files\Google\Chrome\Application\chrome.exe")
            time.sleep(5)
            pyautogui.click(240, 80)
            pyautogui.typewrite(texto)
            pyautogui.hotkey('enter')
            return True
    if texto == google[2]:
        #Hace una busqueda en youtube
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        engine.say("Que es lo que quieres que busque en youtube")
        engine.runAndWait()
        texto = escuchar()
        pyautogui.click(240, 80)
        pyautogui.sleep(1)
        pyautogui.typewrite("https://www.youtube.com")
        pyautogui.hotkey('enter')
        pyautogui.sleep(4)
        pyautogui.click(590, 145)
        pyautogui.sleep(1)
        pyautogui.typewrite(texto)
        pyautogui.hotkey('enter')
        pyautogui.sleep(2)
        pyautogui.click(640, 660)
        return True

engine.say("Buenos dias Rubén")
engine.runAndWait()

while funcionamiento:

    try:
        texto = escuchar()
        texto = texto.lower()

        if texto.find("atención ordenador") != -1:
            engine.say("¿Que es lo que estas buscando?")
            engine.runAndWait()
            
            texto = escuchar()
            if not isinstance(texto, str):
                engine.say("Lo siento, no entendi lo que me pediste")
                engine.runAndWait()

            texto = texto.lower()

            if texto == "cerrar asesor":
                #Apaga el asesor virtual
                engine.say("Cerrando tu asesor virtual")
                engine.runAndWait()
                funcionamiento = False

            resultado = False

            resultado = operacionesAcciones(texto)
            resultado = googleAcciones(texto)
            resultado = discordAcciones(texto)

            if resultado == False:
                engine.say("Lo siento, no entendi lo que me pediste")
                engine.runAndWait()
     
    except Exception:
        pass
