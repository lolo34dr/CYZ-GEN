```markdown
# 🐍 CYZ GEN - Python Reverse Shell Generator

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Made for Kali](https://img.shields.io/badge/Kali-Linux-red)

> **CYZ GEN** is a powerful CLI tool written in Python to quickly generate reverse shell payloads using `msfvenom`, launch an HTTP server, and automate the Metasploit handler process. Includes multi-language support and a built-in tutorial.

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

```bash
██████╗ ██╗   ██╗██╗      ██████╗  █████╗ ██████╗ 
██╔══██╗██║   ██║██║     ██╔═══██╗██╔══██╗██╔══██╗
██████╔╝██║   ██║██║     ██║   ██║███████║██║  ██║
██╔═══╝ ██║   ██║██║     ██║   ██║██╔══██║██║  ██║
██║     ╚██████╔╝███████╗╚██████╔╝██║  ██║██████╔╝
╚═╝      ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

🐍 CYZ GEN — Python Reverse Shell Generator 🐍
```

---

## ⚙️ Requirements

- **Python 3.9+**
- **Metasploit Framework** (must be installed)
- `msfvenom`, `msfconsole`, `xterm`
- Optional: `colorama` (for color in terminal)

Install dependencies:

```bash
sudo apt install metasploit-framework xterm
python3 -m venv venv
source venv/bin/activate
pip install colorama
```

---

## 📦 Installation

```bash
git clone https://github.com/YourUsername/CYZ-GEN.git
cd CYZ-GEN
python3 cyzgen.py
```

---

## 📚 Tutorial

Inside the tool, select the **Tutorial** option to get step-by-step help.

---

## 🛡 Disclaimer

> This project is **only for educational purposes** and ethical penetration testing.
> Using this tool for malicious purposes is strictly forbidden and illegal.

---

## 🙌 Credits

Created by **CYZ**  
Contributions, feedback, and stars are welcome ⭐

---

## 📜 License

MIT License - see the [LICENSE](LICENSE) file for details.
```
