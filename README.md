# File Organizer GUI Application

A simple Python GUI application that organizes files in a directory by sorting them into category-specific folders.


## Features

- 📂 GUI interface for easy folder selection
- 🗂 Automatic file organization by type:
  - Images (JPG, PNG, GIF)
  - Documents (PDF, DOCX, TXT)
  - Spreadsheets (XLSX, CSV)
  - Others (all other file types)
- ✅ Status notifications and error handling
- 🛡 Safe organization (doesn't modify system files)

## Requirements

- Python 3.6+
- Pillow library (for GUI components)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/file-organizer-gui.git
```

2. Install dependencies:
```bash
pip install pillow
```

## Usage

1. Run the application:
```bash
python file_organizer_gui.py
```

2. Click "Browse Folder" to select a directory

3. Click "Organize Files!" to sort files

4. Files will be organized into subfolders:
```
📂 Selected Folder
├── 📂 Images
├── 📂 Documents
├── 📂 Spreadsheets
└── 📂 Others
```

## Customization

To add/modify file categories, edit the `categories` dictionary in the code:
```python
categories = {
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    # Add more categories as needed
}
```

## License

MIT License - feel free to modify and use for personal or commercial projects

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**Note:** Always test with copies of files first. The author is not responsible for any data loss.