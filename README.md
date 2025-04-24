# 🚀 Project Web Generator

Project Web Generator is a 🛠️ Python tool that helps developers quickly create a structured web project with their preferred CSS framework. Users can navigate the selection using arrow keys and confirm their choice with Enter.

## ✨ Features
- ✅ **Automatically generates a web project structure** based on user input.
- 🎨 **Allows users to choose a CSS framework** for their project:
  - 🌐 **Manual CSS** (for HTML + CSS projects)
  - 🎨 **Bootstrap** (for HTML + CSS projects)
  - 🌊 **Tailwind CSS** (for HTML + CSS and React projects)
  - 🧩 **Custom CSS** (for React projects)
- ⌨️ **Interactive CLI interface**: Uses arrow keys for selection, and Enter to confirm.
- 📂 **Creates essential project files**:
  - For **HTML + CSS**: `index.html`, `style.css`, `script.js`.
  - For **React**: `index.html`, `App.jsx`, `App.css`, `main.jsx`, `index.css`, `vite.config.js`, and `package.json`.
- ⚙️ **Supports automatic installation** of dependencies like React, Vite, and Tailwind CSS (if selected).


## 📋 Requirements
Make sure you have Python installed (version 3.x recommended). You also need the `pynput` package for keyboard navigation.

Install dependencies using:
```sh
pip install -r requirements.txt
```

## 🚀 Installation & Usage
### 🔹 Install Globally
To use `webgen` as a globally executable command:
1. Install the package in editable mode:
   ```sh
   pip install --editable .
   ```
2. Now, you can execute the command from anywhere:
   ```sh
   python -m webgen
   ```

### 🔹 Run Locally
1. Clone this repository:
   ```sh
   git clone https://github.com/zen-Hikari/Project-Web-Generator.git
   ```
2. Navigate to the project folder:
   ```sh
   cd Project-Web-Generator
   ```
3. Run the script directly:
   ```sh
   python __main__.py
   ```
4. Follow the on-screen instructions to create your project.

## 🤝 Contributing
Feel free to fork this project and submit pull requests to improve it! 💡

## 📜 License
This project is licensed under the MIT License.

