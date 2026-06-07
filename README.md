# 🗂️ FileForge — CRUD File Management System

A clean, dark-themed **File Management System** built with **Python** and **Streamlit**.  
Supports full CRUD operations — Create, Read, Update, and Delete files — through a modern browser-based UI.

---

## ✨ Features

- 📄 **Create** — Create new files with custom content
- 👁️ **Read** — View file contents with metadata (size, line count)
- ✏️ **Update** — Rename, append to, or overwrite existing files
- 🗑️ **Delete** — Safely delete files with a confirmation guard
- 📁 **File Browser** — Live view of all files in the workspace
- 🔒 **Path Traversal Protection** — Files are sandboxed in a dedicated folder

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core logic |
| Streamlit | Web UI framework |
| Pathlib | File system operations |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/anaydev29/CRUD-file-management.git
cd CRUD-file-management
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install streamlit
```

### 4. Run the app
```bash
python -m streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## 📁 Project Structure

```
CRUD-file-management/
│
├── app.py               # Main Streamlit application
├── main.py              # Original CLI version
├── .gitignore
└── README.md
```

---

## 🖥️ UI Preview

> Dark terminal-aesthetic UI with color-coded tabs for each operation.

---

## 👨‍💻 Author

**Anay** — [@anaydev29](https://github.com/anaydev29)

---

⭐ If you found this useful, consider giving it a star!