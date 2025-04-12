# 🐍 CYZ GEN - Python Reverse Shell Generator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Made for Kali](https://img.shields.io/badge/Kali-Linux-red.svg)](https://www.kali.org/)

> **CYZ GEN** is a powerful CLI tool written in Python to quickly generate reverse shell payloads using `msfvenom`, launch an HTTP server, and automate the Metasploit handler process. It includes multi-language support and a built-in tutorial.

---

## 🚀 Features

- 🎯 Generate reverse shell payloads easily:
  - `windows/meterpreter/reverse_tcp`
  - `windows/meterpreter/reverse_http`
  - `windows/meterpreter/reverse_https`
- 🌐 Start an HTTP server on port 80 for payload delivery
- 💀 Auto-launch Metasploit with a configured handler
- ♻️ Clean up generated files
- 📚 Built-in interactive tutorial
- 🌍 Language selection (English 🇬🇧 / French 🇫🇷)

---

## 📸 Preview

██████╗ ██╗ ██╗██╗ ██████╗ █████╗ ██████╗ ██╔══██╗██║ ██║██║ ██╔═══██╗██╔══██╗██╔══██╗ ██████╔╝██║ ██║██║ ██║ ██║███████║██║ ██║ ██╔═══╝ ██║ ██║██║ ██║ ██║██╔══██║██║ ██║ ██║ ╚██████╔╝███████╗╚██████╔╝██║ ██║██████╔╝ ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝ ╚═╝╚═════╝

🐍 CYZ GEN — Python Reverse Shell Generator 🐍


---

## ⚙️ Requirements

- **Python 3.9+**
- **Metasploit Framework** (must be installed)
- `msfvenom`, `msfconsole`
- Optional: `colorama` (for colored CLI output)

Install dependencies:

```bash
sudo apt install metasploit-framework
python3 -m venv venv
source venv/bin/activate
pip install colorama

📦 Installation

Clone the repository:

git clone https://github.com/YourUsername/CYZ-GEN.git
cd CYZ-GEN

📚 Usage

Run the application:

sudo python3 cyz_gen.py

Follow the prompts to:

    Choose your language (English / Français)

    Generate your payload

    Launch an HTTP server

    Start the Metasploit handler

    Clean up generated files

    Display the built-in tutorial

📄 License

This project is licensed under the MIT License (with a custom credit requirement). See the LICENSE file for details.
🙌 Credits

Created by CYZ
Special thanks to the Metasploit team and the Kali Linux community.
⚠️ Disclaimer

This tool is intended for educational purposes only. Use it only on systems and networks for which you have explicit authorization.
