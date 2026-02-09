import tkinter as tk
import json
import os
import sys
from gui import PhotoCleanerApp  # GUI-Klasse auslagern
from tkinter import messagebox
from utils import load_language

# Aktuelle Sprache (Standard: Englisch)
CURRENT_LANGUAGE = "de"

# Hauptfunktion
def main():
    global CURRENT_LANGUAGE
    # GUI-Hauptfenster
    root = tk.Tk()
    root.geometry("1024x700")
    root.title("Mamas Photo Cleaner 🖼🧼")
    root.resizable(True, True)

    # Rundungen & Theme (optional, kommt später mit Styles)
    root.configure(bg="#f9f9f9")  # Helles Grau statt Standard-Grau

    # Sprache laden
    texts = load_language(CURRENT_LANGUAGE)

    # App starten
    app = PhotoCleanerApp(root, texts, CURRENT_LANGUAGE)
    root.mainloop()

if __name__ == "__main__":
    main()

