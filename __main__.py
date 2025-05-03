import os
import shutil
import json
import sys
import signal
import questionary
from questionary import Choice, Style


# ==== baca package.json ====
def get_version_from_package():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Lokasi file .py ini
        path = os.path.join(base_dir, "package.json")  # Path ke package.json
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("version", "Unknown")
    except FileNotFoundError:
        return f"package.json not found"
    except json.JSONDecodeError:
        return f"Invalid JSON in package.json"

# ======== CLI ARGUMENTS HANDLER ========

def show_help():
    print("""
Usage: python main.py [OPTIONS]

Options:
  --help        Show help and how to use
  --list        Show list of available templates and CSS
  --version     Show project version
""")

def show_list():
    print("""
🧩 Available Project Templates:
  - HTML + CSS
  - React
  - Vue

🎨 Available CSS Frameworks:
  For HTML:
    - Manual CSS
    - Tailwind CSS
    - Bootstrap
  For React & Vue:
    - CSS Sendiri
""")
    
def show_version():
    version = get_version_from_package()
    print(f"Webgen CLI Generator - Version {version}")
    sys.exit(0)

# Check arguments
if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg == "--help":
        show_help()
        sys.exit(0)
    elif arg == "--list":
        show_list()
        sys.exit(0)
    elif arg == "--version":
        show_version()
        sys.exit(0)



# === ASCII ART di Awal ===
ascii_art = """
\033[1;35m
██╗    ██╗███████╗██████╗  ██████╗ ███████╗███╗   ██╗
██║    ██║██╔════╝██╔══██╗██╔════╝ ██╔════╝████╗  ██║
██║ █╗ ██║█████╗  ██████╔╝██║  ███╗█████╗  ██╔██╗ ██║
██║███╗██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██║╚██╗██║
╚███╔███╔╝███████╗██████╔╝╚██████╔╝███████╗██║ ╚████║
 ╚══╝╚══╝ ╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝
\033[0m
"""
print(ascii_art)

# ==== Credit ====
# color
BLUE = "\033[34m"
RESET = "\033[0m"

fixed_width = 60

# text
title = f"{BLUE}Halo, Selamat datang di Webgen{RESET}"
author = f"{BLUE}By Noval Hasmi W. @2025{RESET}"

print(title.center(fixed_width))
print(author.center(fixed_width))
print("\n") 


# Custom CLI style
custom_style = Style([
    ("qmark", "fg:#3498db"),
    ("question", "fg:#95a5a6"),
    ("selected", "fg:#FF00FF"),
    ("pointer", "fg:#3498db"),
    ("answer", "fg:#f2f2f2"),
    ("separator", "fg:#666666"),
    ("highlighted", "fg:#3498db"),
    ("disabled", "fg:#858585 italic"),
    ("instruction", "fg:#5f5f5f italic")
])

# Handle Ctrl+C
def signal_handler(sig, frame):
    print("\n❌ Operasi dibatalkan.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# ==== Masukkan nama proyek ====
project_name = questionary.text(
    "📁 Masukkan nama proyek:",
    style=custom_style
).ask()
if not project_name:
    print("❌ Nama proyek tidak boleh kosong.")
    sys.exit(1)
project_name = project_name.strip().replace(" ", "-")

# ==== Pilih tipe proyek ====
project_type = questionary.select(
    "🌟 Pilih FrameWork:",
    choices=[
        Choice(title="HTML + CSS", value="html"),
        Choice(title="React", value="react"),
        Choice(title="Vue", value="vue"),
    ],
    style=custom_style,
    pointer="➥"
).ask()

# ==== Pilih variant framework ====
# ==== react ====
if project_type == "react":
    variant_framework = questionary.select(
        "🔧 Pilih Variant untuk React:",
        choices=[
            Choice("JavaScript", "JavaScript"),
            Choice("TypeScript", "TypeScript"),
            ],
        style=custom_style,
        pointer="➥"
    ).ask()
    if variant_framework == "JavaScript":
        print("🔄 meng-clone project React Js dari repo...")
        repo_url_react_js = "https://github.com/zen-Hikari/react-template.git"
        try:
            result = os.system(f"git clone {repo_url_react_js} {project_name}")
            if result != 0:
                raise Exception("printah git clone gagal")
        except Exception as e:
            print(f"❌ gagal repo: {e}")
            sys.exit(1)
    elif variant_framework == "TypeScript":
        print("🔄 meng-clone project Vue TS dari repo...")
        url_repo_react_ts = "https://github.com/zen-Hikari/react-ts-template.git"
        try:
            result = os.system(f"git clone {url_repo_react_ts} {project_name}")
            if result != 0:
                raise Exception("perintah git clone gagal")
        except Exception as e:
            print(f"❌ gagal repo: {e}")
            sys.exit(1)
# ==== vue ====
elif project_type == "vue":
    variant_framework = questionary.select(
        "🔧 Pilih Variant untuk Vue:",
        choices=[
            Choice("JavaScript", "JavaScript"),
            Choice("TypeScript", "TypeScript")
            ],
        style=custom_style,
        pointer="➥"
    ).ask()
    if variant_framework == "TypeScript":
        print("🔄 meng-clone project Vue TS dari repo...")
        repo_url_vue_ts = "https://github.com/zen-Hikari/vue-ts-template.git"
        try:
            result = os.system(f"git clone {repo_url_vue_ts} {project_name}")
            if result != 0:
                raise Exception("Perintah git clone gagal")
        except Exception as e:
            print(f"❌ Gagal clone repo: {e}")
            sys.exit(1)
    elif variant_framework == "JavaScript":
        print("🔄 meng-clone project Vue Js dari repo...")
        repo_url_vue = "https://github.com/zen-Hikari/vue-template.git"
        try:
            result = os.system(f"git clone {repo_url_vue} {project_name}")
            if result != 0:
                raise Exception("Perintah git clone gagal")
        except Exception as e:
            print(f"❌ Gagal clone repo: {e}")
            sys.exit(1)
else:
    css_framework = questionary.select(
        "🎨 Pilih CSS untuk HTML:",
        choices=[
            Choice("Manual CSS", "CSS standard"),
            Choice("Tailwind CSS", "Tailwind"),
            Choice("Bootstrap", "Bootstrap"),
        ],
        style=custom_style,
        pointer="➥"
    ).ask()


print("\n")

# ==== Fungsi bantu menulis file ====
def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ==== HTML + CSS ====
if project_type == "html":
    os.makedirs(f"{project_name}/css", exist_ok=True)
    os.makedirs(f"{project_name}/js", exist_ok=True)   

    css_cdn = ""
    if css_framework == "Tailwind CSS":
        css_cdn = '<script src="https://cdn.tailwindcss.com"></script>'
    elif css_framework == "Bootstrap":
        css_cdn = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">'

    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    {css_cdn}
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>Selamat datang di {project_name}!</h1>
    <script src="js/script.js"></script>
</body>
</html>
"""
    write_file(f"{project_name}/index.html", html_content)
    write_file(f"{project_name}/css/style.css", "body { font-family: Arial, sans-serif; }")
    write_file(f"{project_name}/js/script.js", "console.log('Hello World');")
    
    pkg_path = os.path.join(project_name, "package.json")
    if os.path.exists(pkg_path):
        with open(pkg_path, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data["name"] = project_name
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

# ==== OUTPUT ====
print("\n✅ Proyek berhasil dibuat!")
print(f"📁 Nama proyek: {project_name}")
print(f"🔧 Tipe: {'HTML + CSS' if project_type == 'html' else project_type.capitalize()}")
if project_type in ("html"):
    print(f"🎨 CSS: {css_framework}")
if project_type in ("react", "vue"):
    print(f"Variant: {variant_framework}")
print("🚀 Jalankan:")
print(f"   cd {project_name}")
if project_type in ("react", "vue"):
    print("   pnpm install && pnpm run dev")

