from colorama import init, Fore, Style
import subprocess
import sys
import time
import threading

init(autoreset=True)

def spinner_animation():
    spinner = ['|', '/', '-', '\\']
    while not done_event.is_set():
        for char in spinner:
            sys.stdout.write(f'\r{Fore.CYAN}Processing {char}')
            sys.stdout.flush()
            time.sleep(0.1)

def run_migrations():
    global done_event
    done_event = threading.Event()  
    
    spinner_thread = threading.Thread(target=spinner_animation)
    spinner_thread.start()

    print(Fore.YELLOW + "-" * 50)
    print(Fore.YELLOW + "Starting Django Migrations...")
    print(Fore.YELLOW + "-" * 50)

    try:
        print(Fore.CYAN + "Creating migrations...")
        result = subprocess.run(['python', 'manage.py', 'makemigrations'], check=True, capture_output=True, text=True)
        print(Fore.GREEN + "\rMigrations created successfully! " + Style.BRIGHT + "✓")
        print(Fore.GREEN + "-" * 50)
        print(Fore.GREEN + result.stdout)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "\rError creating migrations " + Style.BRIGHT + "✗")
        print(Fore.RED + "-" * 50)
        print(Fore.RED + e.stderr)
        done_event.set()
        return  

    try:
        print(Fore.CYAN + "Applying migrations...")
        result = subprocess.run(['python', 'manage.py', 'migrate'], check=True, capture_output=True, text=True)
        print(Fore.GREEN + "\rMigrations applied successfully! " + Style.BRIGHT + "✓")
        print(Fore.GREEN + "-" * 50)
        print(Fore.GREEN + result.stdout)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "\rError applying migrations " + Style.BRIGHT + "✗")
        print(Fore.RED + "-" * 50)
        print(Fore.RED + e.stderr)
    
    done_event.set()  
    spinner_thread.join()  

if __name__ == "__main__":
    run_migrations()
