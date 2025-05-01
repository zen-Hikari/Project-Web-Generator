import os
import shutil
import json
import sys
import signal
import questionary
from questionary import Choice, Style

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
    "🌟 Pilih Tipe Proyek:",
    choices=[
        Choice(title="HTML + CSS", value="html"),
        Choice(title="React", value="react"),
        Choice(title="Vue", value="vue"),
    ],
    style=custom_style,
    pointer="➥"
).ask()

# ==== Pilih CSS framework ====
if project_type == "react":
    css_framework = questionary.select(
        "🎨 Pilih CSS untuk React:",
        choices=[Choice("CSS Sendiri", "CSS standard")],
        style=custom_style,
        pointer="➥"
    ).ask()
elif project_type == "vue":
    css_framework = questionary.select(
        "🎨 Pilih CSS untuk Vue:",
        choices=[Choice("CSS Sendiri", "CSS standard")],
        style=custom_style,
        pointer="➥"
    ).ask()
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

# ==== React ====
elif project_type == "react":
    print("🔄 Meng-clone template React dari GitHub...")
    repo_url = "https://github.com/zen-Hikari/react-template.git"
    try:
        result = os.system(f"git clone {repo_url} {project_name}")
        if result != 0:
            raise Exception("Perintah git clone gagal")
    except Exception as e:
        print(f"❌ Gagal clone repo: {e}")
        sys.exit(1)

# ==== Vue ====
elif project_type == "vue":
    print("🔄 Meng-clone template Vue dari GitHub...")
    repo_url_vue = "https://github.com/zen-Hikari/vue-template.git"
    try:
        result = os.system(f"git clone {repo_url_vue} {project_name}")
        if result != 0:
            raise Exception("Perintah git clone gagal")
    except Exception as e:
        print(f"❌ Gagal clone repo: {e}")
        sys.exit(1)

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
print(f"🎨 CSS: {css_framework}")
print("🚀 Jalankan:")
print(f"   cd {project_name}")
if project_type in ("react", "vue"):
    print("   pnpm install && pnpm run dev")
