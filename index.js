#!/usr/bin/env node

import chalk from 'chalk';
import { execSync } from "child_process";
import path from "path";
import fs from "fs";
import { fileURLToPath } from 'url';

// ES Module Path Resolver
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Fungsi baca versi dari package.json lokal
function getLocalVersion() {
  try {
    const pkgPath = path.join(__dirname, "package.json");
    const pkgData = JSON.parse(fs.readFileSync(pkgPath, "utf-8"));
    return pkgData.version;
  } catch {
    return null;
  }
}

// Fungsi cek versi terbaru dari npm
function getLatestNpmVersion(pkgName) {
  try {
    const output = execSync(`pnpm view ${pkgName} version`, { encoding: "utf-8" });
    return output.trim();
  } catch {
    return null;
  }
}

// Cek pembaruan
function checkForUpdate() {
  const localVersion = getLocalVersion();
  const latestVersion = getLatestNpmVersion("@novalhikari/webgen-cli");

  if (localVersion && latestVersion && localVersion !== latestVersion) {
    console.log(chalk.yellow(`🚨 Versi terbaru tersedia: ${latestVersion} (saat ini: ${localVersion})`));
    console.log(chalk.green(`💡 Jalankan 'pnpm update -g @novalhikari/webgen-cli' untuk memperbarui.`));
  }
}

// Jalankan cek pembaruan
checkForUpdate();

// Cek apakah Python tersedia
try {
  execSync("python --version", { stdio: "ignore" });
} catch {
  console.error("❌ Python tidak terdeteksi. Pastikan Python sudah terinstall dan ditambahkan ke PATH.");
  process.exit(1);
}

// Cek apakah modul Python seperti questionary sudah terinstall
try {
  execSync("python -c \"import questionary\"", { stdio: "ignore" });
} catch {
  const requirementsPath = path.join(__dirname, "requirements.txt");
  if (fs.existsSync(requirementsPath)) {
    console.log(chalk.yellow("📦 Menginstal dependensi Python dari requirements.txt..."));
    try {
      execSync(`pip install -r "${requirementsPath}"`, { stdio: "inherit" });
    } catch (e) {
      console.error(chalk.red("❌ Gagal menginstal dependencies Python."));
      process.exit(1);
    }
  } else {
    console.warn(chalk.red("⚠️ File requirements.txt tidak ditemukan, dan modul Python belum terinstall."));
    process.exit(1);
  }
}

// Jalankan __main__.py dengan argumen CLI
const scriptPath = path.join(__dirname, "__main__.py");

if (!fs.existsSync(scriptPath)) {
  console.error("❌ File __main__.py tidak ditemukan.");
  process.exit(1);
}

try {
  const args = process.argv.slice(2).join(" ");
  execSync(`python "${scriptPath}" ${args}`, { stdio: "inherit" });
} catch (error) {
  console.error("❌ Gagal menjalankan __main__.py:`, error.message");
  process.exit(1);
}