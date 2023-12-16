import speech_recognition as sr
import subprocess as subp
import pygetwindow as window
import webbrowser
import pyautogui
import os
import time
import random
import pygame

# Crear un objeto recognize 
recognizer = sr.Recognizer()


funcionamiento = True

atencion = [
    "C:\\Users\\ruben\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\atencion1.wav",
    "C:\\Users\\ruben\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\atencion2.wav",
    "C:\\Users\\ruben\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\atencion3.wav",
    "C:\\Users\\ruben\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\atencion4.wav"
]

def reproducir_audio(ruta):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play()

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
    
def cerrar_ventana(app):
    # Encuentra la ventana de Discord
    discord_windows = window.getWindowsWithTitle(app)
    if discord_windows:
        # Cierra la ventana de Discord
        discord_windows[0].close()
        print("Discord cerrado")


def operacionesAcciones(texto):
    if texto == "amplia ventana":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\ampliar_ventana.wav")
        pyautogui.hotkey('win', 'up')
        return True

    if texto == "abre steam":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\steam.wav")

        subp.run("C:\Program Files (x86)\Steam\steam.exe")
        return True
    elif texto == "cierra steam":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\cerrar_steam.wav")
        cerrar_ventana('steam')
        return True
    
    if texto == "abre ópera":
        #Abre Opera GX
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\opera.wav")

        subp.run("C:\\Users\\ruben\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
        return True
    elif texto == "cierra ópera":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\cerrar_opera.wav")
        cerrar_ventana('Opera')
        return True
    
    if texto == "abre el minecraft":
        #Abre el Minecraft
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\minecraft.wav")
        time.sleep(2)
        subp.run("C:\\Users\\ruben\\Desktop\\Minecraft Launcher.lnk", shell=True)
        return True
    elif texto == "cierra el minecraft":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\cerrar_minecraft.wav")
        cerrar_ventana('minecraft')
        return True
    
    if texto == "abre el fortnite" or texto == "abre fortnite":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\abrir_fortnite.wav")

        webbrowser.open("com.epicgames.launcher://apps/fn%3A4fe75bbc5a674f4f9b356b5c90567da5%3AFortnite?action=launch&silent=true")
        return True
    elif texto == "cierra fortnite" or texto == "cierra el fortnite":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\cerrar_fortnite.wav")
        cerrar_ventana('Fortnite')
        return True
    
    if texto == "apaga el ordenador":
        #Apaga el ordeandor
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\apagar_pc.wav")
        time.sleep(2)
        os.system("shutdown /s /t 0")
        return True
    
    if texto == "abre visual studio":
        #Abre visual studio
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\visual_studio.wav")
        time.sleep(2)
        subp.run("C:\\Users\\ruben\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        return True
    elif texto == "cierra steam":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\cerrar_visual.wav")
        cerrar_ventana('Code')
        return True
    
    if texto == "canta algo" or texto == "canta":
        #Abre visual studio
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\intro_cancion.wav")
        time.sleep(5)
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\gladosSong.mp3")
        return True
    
    if texto == "hijo de puta":
        #Responde al insulto
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\insulto.wav")
        time.sleep(3)
        return True

def discordAcciones(texto):
    # Operaciones de discord
    if texto == "abre discord":
        #Abre discord
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\abrir_discord.wav")
        time.sleep(1)
        subp.run("C:\\Users\\ruben\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
        return True
    elif texto == "cierra discord":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\cerrar_discord.wav")
        cerrar_ventana('Discord')
        return True
    
    if texto == "abre discord y conéctate a llamada" or texto == "entra a llamada" or texto == "conéctate a llamada" or texto == "entra en llamada":
        #Abre discord y se conecta
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\conectarse_llamada.wav")
        time.sleep(1)
        subp.run("C:\\Users\\ruben\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
        time.sleep(5)
        pyautogui.click(40, 145)
        pyautogui.click(220, 450)
        return True

def googleAcciones(texto):
    if texto == "abre google":
        #Abre Google
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\chrome.wav")
        time.sleep(1)
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        return True
    elif texto == "cierra google":
        #Abre steam
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\cerrar_chrome.wav")
        cerrar_ventana('chrome')
        return True
    
    if texto == "busca en google":
        #Hace una busqueda en internet
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\buscar_google.wav")
        time.sleep(2)
        texto = escuchar()
        if not isinstance(texto, str):
            reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\no_entendido.wav")
            time.sleep(2)
        else:
            subp.run("C:\Program Files\Google\Chrome\Application\chrome.exe")
            time.sleep(5)
            pyautogui.click(240, 80)
            pyautogui.typewrite(texto)
            pyautogui.hotkey('enter')
            return True
    if texto == "busca en youtube" or texto == "abre en youtube":
        #Hace una busqueda en youtube
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\buscar_google.wav")
        time.sleep(2)
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
        pyautogui.click(640, 430)
        return True

reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\buenos_dias.wav")

while funcionamiento:

    try:
        texto = escuchar()
        texto = texto.lower()

        if texto.find("atención ordenador") != -1 or texto.find("escucha glados") != -1:
            nRandom = random.randint(0, 3)
            reproducir_audio(atencion[nRandom])
            time.sleep(1)
            
            texto = escuchar()
            if not isinstance(texto, str):
                reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\no_entendido.wav")
                time.sleep(2)
            
            if texto == "cerrar asesor":
                #Apaga el asesor virtual
                reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\cerrar_asesor.wav")
                time.sleep(2)
                funcionamiento = False
                resultado = True

            texto = texto.lower()

            resultado = operacionesAcciones(texto)
            if resultado == None:
                resultado = googleAcciones(texto)
            if resultado == None:
                resultado = discordAcciones(texto)

            if resultado == None :
                reproducir_audio("C:\\Users\\ruben\\Documents\\Visual studio\\Python\\asistente_virtual\\voces\\no_entendido.wav")
                time.sleep(1)
     
    except Exception:
        pass
