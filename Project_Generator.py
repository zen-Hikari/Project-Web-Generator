import os
import sys
import subprocess
from pynput import keyboard
from colorama import Fore, Style, init

init(autoreset=True)  # Mengaktifkan reset otomatis warna

# Daftar pilihan framework CSS
css_frameworks = ["Tanpa Framework", "Bootstrap", "Tailwind CSS"]
selected_index = 0  # Indeks pilihan yang dipilih

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar
    print(Fore.CYAN + "🌟 Pilih framework CSS: 🌟" + Style.RESET_ALL)
    for i, framework in enumerate(css_frameworks):
        prefix = Fore.GREEN + "➜ " if i == selected_index else "  "
        print(f"{prefix}{framework}" + Style.RESET_ALL)

def on_press(key):
    global selected_index
    if key == keyboard.Key.up:
        selected_index = (selected_index - 1) % len(css_frameworks)
    elif key == keyboard.Key.down:
        selected_index = (selected_index + 1) % len(css_frameworks)
    elif key == keyboard.Key.enter:
        return False  # Stop listener saat enter ditekan
    display_menu()

# Fungsi utama untuk membuat proyek
def create_project(project_name, css_framework):
    structure = [
        f"{project_name}/css",
        f"{project_name}/js",
        f"{project_name}/img"
    ]
    for folder in structure:
        os.makedirs(folder, exist_ok=True)
    
    # File HTML
    with open(f"{project_name}/index.html", "w") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    {generate_css_link(css_framework)}
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>Welcome to {project_name}!</h1>
    <script src="js/script.js"></script>
</body>
</html>
""")
    
    # File CSS
    with open(f"{project_name}/css/style.css", "w") as f:
        f.write("body { font-family: Arial, sans-serif; }")
    
    # File JS
    with open(f"{project_name}/js/script.js", "w") as f:
        f.write("console.log('Hello World');")
    
    print(Fore.YELLOW + f"🎉 Proyek '{project_name}' berhasil dibuat dengan {css_framework}! 🚀" + Style.RESET_ALL)
    print(Fore.MAGENTA + "🔧 Tool by Noval" + Style.RESET_ALL)

# Fungsi untuk menambahkan link CSS
def generate_css_link(css_framework):
    if css_framework == "Bootstrap":
        return '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">'
    elif css_framework == "Tailwind CSS":
        return '<script src="https://cdn.tailwindcss.com"></script>'
    return ""

# Jalankan
if __name__ == "__main__":
    project_name = input(Fore.BLUE + "📁 Masukkan nama proyek: " + Style.RESET_ALL)
    
    # Pilih CSS Framework dengan navigasi panah
    display_menu()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    
    chosen_framework = css_frameworks[selected_index]
    create_project(project_name, chosen_framework)
