import os
import csv
import zipfile
from datetime import datetime
from tkinter import filedialog, messagebox


def export_duplicates(checkbox_refs, texts):
    if not checkbox_refs:
        messagebox.showwarning("Export", texts.get("no_export_data", "Keine Daten zum Exportieren."))
        return


    export_folder = filedialog.askdirectory(title=texts.get("choose_export_folder", "Wähle Zielordner"))
    if not export_folder:
        return


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = os.path.join(export_folder, f"duplikate_{timestamp}.csv")
    zip_path = os.path.join(export_folder, f"duplikate_{timestamp}.zip")


    with open(csv_path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Dateiname", "Typ", "Vollständiger Pfad"])
        for var, _, label, color, path in checkbox_refs:
            if var.get():
                typ = "Duplikat im selben Ordner" if color == "blue" else "Duplikat in anderem Ordner"
                writer.writerow([label.cget("text"), typ, path])


    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, arcname=os.path.basename(csv_path))


    messagebox.showinfo("Export", texts.get("export_success", "Export erfolgreich!") + f"\n\n{zip_path}")
