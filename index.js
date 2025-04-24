#!/usr/bin/env node

const updateNotifier = require('update-notifier');
const chalk = require('chalk');
const { execSync } = require("child_process");
const path = require("path");
const fs = require("fs");
const pkg = require('./package.json');

// Notifikasi update
updateNotifier({ pkg }).notify();

// Bersihkan terminal dan info versi
console.clear();
console.log(chalk.blueBright(`🚀 WebGen CLI v${pkg.version}`));

// Cek apakah Python tersedia
try {
  execSync("python --version", { stdio: "ignore" });
} catch {
  console.error("❌ Python tidak terdeteksi. Pastikan Python sudah terinstall dan ditambahkan ke PATH.");
  process.exit(1);
}

// Jalankan __main__.py
const scriptPath = path.join(__dirname, "__main__.py");

if (!fs.existsSync(scriptPath)) {
  console.error("❌ File __main__.py tidak ditemukan.");
  process.exit(1);
}

try {
  execSync(`python "${scriptPath}"`, { stdio: "inherit" });
} catch (error) {
  console.error("❌ Gagal menjalankan __main__.py:", error.message);
  process.exit(1);
}
