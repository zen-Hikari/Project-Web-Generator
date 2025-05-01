#!/usr/bin/env node

import updateNotifier from 'update-notifier';
import chalk from 'chalk';
import { execSync } from "child_process";
import path from "path";
import fs from "fs";
import { fileURLToPath } from 'url';
import pkg from './package.json' assert { type: 'json' };

// Menangani path untuk modul ES
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
// Notifikasi update
const notifier = updateNotifier({ pkg });
if (notifier.update) {
  console.log(chalk.yellow(`🚨 Update tersedia! Versi baru: ${notifier.update.latest}`));
  console.log(chalk.green(`Jalankan 'pnpm update -g @novalhikari/webgen-cli' untuk memperbarui.`));
} else {
  console.log(chalk.green("✅ Tidak ada pembaruan tersedia."));
}

console.log("DEBUG UPDATE CHECK:", notifier.update);
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
  const args = process.argv.slice(2).join(" ");
  execSync(`python "${scriptPath}" ${args}`, { stdio: "inherit" });
} catch (error) {
  console.error("❌ Gagal menjalankan __main__.py:", error.message);
  process.exit(1);
}
