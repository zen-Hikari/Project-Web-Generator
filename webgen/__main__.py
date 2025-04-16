import os
import questionary
import signal
import sys
from questionary import Choice, Style

# Gaya Vite
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

# Fungsi untuk menangani Ctrl+C
def signal_handler(sig, frame):
    print("\nOperation canceled")
    sys.exit(0)

# Menangani sinyal SIGINT (Ctrl + C)
signal.signal(signal.SIGINT, signal_handler)

# Masukkan nama proyek di awal
try:
    project_name = questionary.text("📁 Masukkan nama proyek:").ask()
    if not project_name:
        raise ValueError("Nama proyek tidak boleh kosong.")
except KeyboardInterrupt:
    print("\nOperation canceled")
    sys.exit(0)
except ValueError as e:
    print(f"\n{e}")
    sys.exit(0)

project_name = project_name.strip().replace(" ", "-")

# Pilih jenis proyek
project_type = questionary.select(
    "🌟 Pilih Tipe Proyek:",
    choices=[
        "○ │  HTML + CSS",
        "○ │  React",
        "○ │  Vue",
        "○ │  Svelte"
    ],
    style=custom_style
).ask()

print("\n")

# Pilih framework CSS
css_framework = questionary.select(
    "🧩 Pilih CSS Framework:",
    choices=[
        "○ │  Tanpa Framework (Manual CSS)",
        "○ │  Tailwind CSS",
        "○ │  Bootstrap",
        "○ │  Bulma",
        "○ │  Materialize",
        Choice("○ │  Chakra UI", disabled="❌ Belum tersedia")
    ],
    style=custom_style
).ask()

print("\n")

# Buat struktur proyek
folders = [
    f"{project_name}/css",
    f"{project_name}/js",
    f"{project_name}/img"
]
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Fungsi generate link CSS
def generate_css_link(framework):
    if "Tailwind" in framework:
        return '<script src="https://cdn.tailwindcss.com"></script>'
    elif "Bootstrap" in framework:
        return '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">'
    elif "Bulma" in framework:
        return '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">'
    elif "Materialize" in framework:
        return '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">'
    return ""  # Manual CSS

# Buat file HTML
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
    <h1>Selamat datang di {project_name}!</h1>
    <script src="js/script.js"></script>
</body>
</html>
""")

# Buat file style.css dan script.js
with open(f"{project_name}/css/style.css", "w") as f:
    f.write("body { font-family: Arial, sans-serif; }")

with open(f"{project_name}/js/script.js", "w") as f:
    f.write("console.log('Hello World');")

# Output akhir
print("\n✅ Proyek berhasil dibuat!")
print(f"📁 Nama proyek: {project_name}")
print(f"🔧 Tipe: {project_type.replace('○ │  ', '')}")
print(f"🎨 CSS: {css_framework.replace('○ │  ', '')}")
print("🚀 Sukses! 🎉")
