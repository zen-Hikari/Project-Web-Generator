#!/usr/bin/env node

// Bersihkan terminal
console.clear();

// Import modul dari Node.js
const { execSync } = require("child_process");
const path = require("path");
const fs = require("fs");

// Path ke file Python
const scriptPath = path.join(__dirname, "__main__.py");

// Cek apakah file Python ada
if (!fs.existsSync(scriptPath)) {
  console.error("❌ File webgen.py tidak ditemukan.");
  process.exit(1);
}

// Jalankan file Python
try {
  execSync(`python "${scriptPath}"`, { stdio: "inherit" });
} catch (error) {
  console.error("❌ Gagal menjalankan webgen.py:", error.message);
  process.exit(1);
}
