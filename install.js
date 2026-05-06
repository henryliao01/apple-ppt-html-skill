#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const os = require("os");

const DEST = path.join(os.homedir(), ".claude", "skills", "apple-ppt-html");
const SKIP = new Set(["install.js", "package.json", "README.md", ".git", ".npmignore"]);

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    if (SKIP.has(entry.name)) continue;
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

try {
  copyDir(__dirname, DEST);
  console.log(`\n✅ apple-ppt-html skill installed to: ${DEST}`);
  console.log("   Restart Claude Code to activate.\n");
} catch (err) {
  console.error("\n❌ Installation failed:", err.message);
  process.exit(1);
}
