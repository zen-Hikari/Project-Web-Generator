#!/usr/bin/env node

import chalk from 'chalk';
import { execSync } from "child_process";
import path from "path";
import fs from "fs";
import { fileURLToPath } from 'url';

// ES Module Path Resolver
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Cek apakah Python tersedia
try {
  execSync("python --version", { stdio: "ignore" });
} catch {
  console.error("❌ Python tidak terdeteksi. Pastikan Python sudah terinstall dan ditambahkan ke PATH.");
  process.exit(1);
}

// Jalankan __main__.py dengan argumen CLI
const scriptPath = path.join(__dirname, "__main__.py");

if (!fs.existsSync(scriptPath)) {
  console.error("❌ File __main__.py tidak ditemukan.");
  process.exit(1);
}

try {
  // Ambil semua argumen CLI kecuali "node" dan "index.js"
  const args = process.argv.slice(2).join(" ");
  execSync(`python "${scriptPath}" ${args}`, { stdio: "inherit" });
} catch (error) {
  console.error("❌ Gagal menjalankan __main__.py:", error.message);
  process.exit(1);
}
