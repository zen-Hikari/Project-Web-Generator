import os
import shutil
import json
import sys
import signal
import questionary
from questionary import Choice, Style

# Custom CLI style
custom_style = Style([
    ("qmark", "fg:#00ffff bold"),
    ("question", "bold"),
    ("selected", "fg:#00ff00 bold"),
    ("pointer", "fg:#00ffff bold"),
    ("answer", "fg:#f2f2f2 bold"),
    ("separator", "fg:#666666"),
    ("highlighted", "fg:#ffff00 bold"),
    ("disabled", "fg:#858585 italic"),
    ("instruction", "fg:#5f5f5f italic")
])

# Handle Ctrl+C
def signal_handler(sig, frame):
    print("\n❌ Operasi dibatalkan.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Masukkan nama proyek
project_name = questionary.text("📁 Masukkan nama proyek:").ask()
if not project_name:
    print("❌ Nama proyek tidak boleh kosong.")
    sys.exit(1)
project_name = project_name.strip().replace(" ", "-")

# Pilih tipe proyek
project_type = questionary.select(
    "🌟 Pilih Tipe Proyek:",
    choices=[
        "HTML + CSS",
        "React"
    ],
    style=custom_style
).ask()

# Pilih CSS framework
if project_type == "React":
    css_framework = questionary.select(
        "🎨 Pilih CSS untuk React:",
        choices=[
            "CSS Sendiri"
        ],
        style=custom_style
    ).ask()
else:
    css_framework = questionary.select(
        "🎨 Pilih CSS untuk HTML:",
        choices=[
            "Manual CSS",
            "Tailwind CSS",
            "Bootstrap"
        ],
        style=custom_style
    ).ask()

# Fungsi bantu untuk menulis file
def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Path ke template react
TEMPLATE_REACT = os.path.join(os.path.dirname(__file__), "template", "react")

# ==== HTML + CSS ====
if project_type == "HTML + CSS":
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

# ==== REACT ====
elif project_type == "React":
    os.makedirs(f"{project_name}/public", exist_ok=True)
    os.makedirs(f"{project_name}/src/assets", exist_ok=True)

    # Salin file template dari template/react
    shutil.copy(os.path.join(TEMPLATE_REACT, "App.jsx"), f"{project_name}/src/App.jsx")
    shutil.copy(os.path.join(TEMPLATE_REACT, "main.jsx"), f"{project_name}/src/main.jsx")
    shutil.copy(os.path.join(TEMPLATE_REACT, "App.css"), f"{project_name}/src/App.css")
    shutil.copy(os.path.join(TEMPLATE_REACT, "react.png"), f"{project_name}/src/assets/react.png")

    # Buat index.css default
    write_file(f"{project_name}/src/index.css", """body {
    background-color: rgb(25, 25, 39);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
""")

    # index.html
    write_file(f"{project_name}/index.html", f"""<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{project_name}</title>
    <script type="module" src="/src/main.jsx"></script>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
""")

    # package.json kosong
    write_file(f"{project_name}/package.json", "{}")

    # Install React & Vite
    os.system(f"cd {project_name} && pnpm add react react-dom")
    os.system(f"cd {project_name} && pnpm add -D vite @vitejs/plugin-react")

    # Setup tailwind modern (jika dipilih)
    if css_framework == "Tailwind CSS":
        os.system(f"cd {project_name} && pnpm install tailwindcss @tailwindcss/vite")

        # Ganti index.css
        write_file(f"{project_name}/src/index.css", """@import "tailwindcss";

body {
  background-color: rgb(25, 25, 39);
}
""")

        # Ganti vite.config.js
        write_file(f"{project_name}/vite.config.js", """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss()
  ],
})
""")
    else:
        # Jika CSS sendiri
        write_file(f"{project_name}/vite.config.js", """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'


export default defineConfig({
  plugins: [react(),],
})
""")

    # Tambahkan scripts ke package.json
    pkg_path = os.path.join(project_name, "package.json")
    with open(pkg_path, "r+", encoding="utf-8") as f:
        data = json.load(f)
        data["scripts"] = {
            "dev": "vite",
            "build": "vite build",
            "preview": "vite preview"
        }
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

# ==== OUTPUT ====
print("✅ Proyek berhasil dibuat!")
print(f"📁 Nama proyek: {project_name}")
print(f"🔧 Tipe: {project_type}")
print(f"🎨 CSS: {css_framework}")
print("🚀 Jalankan:")
print(f"   cd {project_name} && pnpm install && pnpm run dev")
