# m0ftp-ps - FTP Manager for PS4

An open-source FTP client application designed for managing files on PlayStation 4 (PS4) systems.  
Built with Python and Tkinter, it provides a clean dark-mode interface and supports multilingual translations (Arabic, Spanish, English).

---

## Features

- FTP connection to PS4 or any standard FTP server.
- Dark theme UI with alternating row colors for better readability.
- Internationalisation: Arabic, Spanish, and English (switchable at runtime).
- Core file operations: upload, download, delete, rename, create directory.
- Real-time progress bar for upload/download operations.
- Quick navigation to common PS4 paths (e.g., `/data`).
- Context menu (right-click) for rapid actions.
- Keyboard shortcuts: `Ctrl+O` for connection, `F5` for refresh.

---

## Requirements

- Python 3.6 or higher.
- No external dependencies; uses built-in modules:
  - `tkinter`
  - `ftplib`
  - `os`, `threading`, `datetime`

---

## Installation and Execution

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/m0ftp-ps.git
   cd m0ftp-ps
