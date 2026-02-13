[🇩🇪 Deutsche Version](README_de.md)  
![AGPL v3 License](https://img.shields.io/badge/license-AGPLv3-blue.svg)
![Windows](https://img.shields.io/badge/platform-Windows-blue)
![Status](https://img.shields.io/badge/status-Prototyp-orange)

# Mamas Photo Cleaner – Simple. Clear. Local.

**Mamas Photo Cleaner** is a user-friendly Windows tool for detecting and safely deleting duplicate files — whether photos, PDFs, Excel sheets, or system files.  
The app was created because my mother wanted a simple solution to remove duplicate files without technical stress. From this idea, a fully working prototype was built that anyone can now use.

---

## 🧰 Main Features

- Detects duplicate files based on their **content (hash comparison)**
- Supports many formats: PNG, JPG, PDF, DOCX, XLSX, JSON and more
- Color-coded overview for clarity:
  - 🟦 **Blue** = duplicate in the same folder
  - 🟨 **Yellow** = duplicate in another folder
  - **White** = original file (will not be deleted)
- Image preview (for image formats)
- Secure delete function with confirmation dialog
- Language switch (German / English)
- Export function as **ZIP and CSV** (optional)

---

## 🧩 Compatibility


Two versions are available in the GitHub Release:


- **MamasPhotoCleaner.zip** – for modern Windows systems (Windows 10 / 11)
- **MamasPhotoCleaner_Legacy.zip** – for older Windows systems (Windows 7 / 8)


Choose the version that matches your operating system.

---

## 💻 System Requirements

- Windows system (tested from Windows 10 upward)
- No installation required — just extract and start
- No internet connection needed
- No external programs or Python dependencies required

---

## ⚙️ Installation

1. Download the ZIP archive from GitHub  
2. Right-click → **“Extract All”**  
3. Start the app by double-clicking `MamasPhotoCleaner.exe`

**Tip:** Place it directly on the Desktop — this ensures more stable folder access.

---

## 🚀 Usage – Step by Step

### 1. Select Folder  
Click **“Select Folder”** and choose one or more specific folders.  
**Important:** Please avoid selecting huge root folders like the entire Desktop — this may cause the app to freeze.

### 2. Scan for Duplicates  
Click **“Scan for Duplicates.”**  
Detected duplicates will appear in a color-marked list.

### 3. Understand the Overview  
Color meanings:  
- 🟦 Blue = duplicate in the same folder  
- 🟨 Yellow = duplicate in another folder  
- White = original (will not be deleted)

Image files appear in the preview panel on the right.  
The preview size can be adjusted using the slider.

### 4. Delete Files  
Click **“Delete.”** A confirmation dialog appears, for example:  
> “Do you really want to delete 14 files?”

Only checked duplicates will be removed.  
**Tip:** Restart the app after deleting files.

### 5. Export Function (Optional)  
Export selected files as a **ZIP archive and CSV file.**  
Ideal for developers — regular users can ignore this step.

### 6. Switch Language  
In the top-right corner, you can switch between **German and English** at any time.

---

## 🖼️ Screenshots Explained

### Screenshot 1 – Default View  
![Screenshot 1](images/Screenshot%202026-02-09%20143043.png)  
Left: detected PNG files in the list.  
Right: image preview.  
🟦 Blue = duplicate in same folder (checked)  
🟨 Yellow = duplicate in another folder (checked)  
White = original file

---

### Screenshot 2 – Image Maximized  
![Screenshot 2](images/Screenshot%202026-02-09%20132432.png)  
The preview panel was expanded to nearly full width for a large image view.

---

### Screenshot 3 – List Maximized  
![Screenshot 3](images/Screenshot%202026-02-09%20132413.png)  
The file list panel was expanded — ideal for reviewing many files.

---

### Screenshot 4 – Delete Confirmation  
![Screenshot 4](images/Screenshot%202026-02-09%20143110.png)  
Shows the safety confirmation dialog when clicking **Delete.**

---

### Screenshot 5 – Language Switch & Other File Types  
![Screenshot 5](images/Screenshot%202026-02-09%20145334.png)  
Language switched to English.  
Various file types are visible: JSON, `.pth`, images, and system files.

---

### Screenshot 6 – Additional Formats in Test  
![Screenshot 6](images/Screenshot%202026-02-09%20150130.png)  
Demonstrates detection of Excel, PDF, Markdown, GitKeep files, and developer folders such as Templates or Workshops.

---

## ⚠️ Technical Notes

- Only **exact duplicates** are detected (no similarity comparison)
- No preview for PDFs or Office files
- Very large root folders may cause the app to freeze
- Restart the app after heavy operations
- Image resizing is currently slider-based — a dedicated button is planned for the Pro version

---

## 🧪 Limitations of the Free Version

- No preview for PDFs or Office files
- No dedicated zoom button for images
- Scanning huge root folders is not recommended
- No automatic selection optimization

---

## 🔜 Planned Pro Version

- Faster processing for large folders
- Similarity comparison (not only identical files)
- Preview for PDF, text, and Office documents
- One-click image zoom button
- Advanced filtering and selection tools
- And much more

---

## 📜 License & Openness

- License: **AGPLv3**  
- No ads, no tracking, no account required  
- Free to use, modify, and share (with attribution)  
- Source code publicly available on GitHub

---

## ✨ Background

Created from a real-life need: bringing order into digital file chaos — without technical jargon.  
What started as a small tool for my mother now helps others keep their files organized — both privately and professionally.
