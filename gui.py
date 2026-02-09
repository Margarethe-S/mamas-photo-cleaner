import os
import sys
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from core import find_duplicate_groups, classify_duplicates
from exporter import export_duplicates
from utils import load_language

class PhotoCleanerApp:
    def __init__(self, root, texts, language):
        self.root = root
        self.texts = texts
        self.language = language

        self.debug_mode = False

        self.selected_folders = []
        self.folder_tag_container = None
        self.duplicate_files = []

        self._setup_style()
        self._build_gui()

    def _setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6, relief="flat", background="#ffffff", foreground="#060000", font=("Arial", 14))
        style.map("TButton", background=[("active", "#e6e6e6")])
        style.configure("blue.TFrame", background="#cce0ff", relief="flat", borderwidth=1)
        style.configure("yellow.TFrame", background="#fff5cc", relief="flat", borderwidth=1)

        style.configure("Default.TFrame", background="#ffffff")
        self.root.option_add("*Font", "Arial", 15)

    def _build_gui(self):
        # --- Top Frame mit Buttons ---
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_select_folder = ttk.Button(top_frame, text=self.texts["select_folder"], command=self.select_folder)
        self.btn_select_folder.pack(side=tk.LEFT, padx=5)

        self.btn_scan = ttk.Button(top_frame, text=self.texts["scan_duplicates"], command=self.scan_for_duplicates)
        self.btn_scan.pack(side=tk.LEFT, padx=5)

        self.btn_delete = ttk.Button(top_frame, text=self.texts["delete_selected"], command=self.delete_selected)
        self.btn_delete.pack(side=tk.LEFT, padx=5)

        self.btn_export = ttk.Button(top_frame, text=self.texts["export"], command=lambda: export_duplicates(self.checkbox_refs, self.texts))
        self.btn_export.pack(side=tk.LEFT, padx=5)

        self.btn_language = ttk.Button(top_frame, text=self.texts["language"], command=self.toggle_language)
        self.btn_language.pack(side=tk.RIGHT, padx=5)

        self.btn_exit = ttk.Button(top_frame, text=self.texts["exit"], command=self.root.quit)
        self.btn_exit.pack(side=tk.RIGHT, padx=5)

        # --- Scrollbarer Bereich für Ordner-Tags ---
        scroll_canvas = tk.Canvas(self.root, height=40, bg="#f9f9f9", highlightthickness=0)
        scroll_canvas.pack(fill=tk.X, padx=10, pady=(5, 0))

        scrollbar = ttk.Scrollbar(self.root, orient="horizontal", command=scroll_canvas.xview)
        scrollbar.pack(fill=tk.X, padx=10)

        self.folder_tag_container = ttk.Frame(scroll_canvas)
        self.folder_tag_container.bind("<Configure>", lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))
        scroll_canvas.create_window((0, 0), window=self.folder_tag_container, anchor="nw")
        scroll_canvas.configure(xscrollcommand=scrollbar.set)

       # Ergebnisbereich als PanedWindow mit gleichmäßiger Aufteilung
        self.results_frame = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.results_frame.pack(fill=tk.BOTH, expand=True)


        self.left_container = ttk.Frame(self.results_frame)
        self.right_container = ttk.Frame(self.results_frame)


        self.results_frame.add(self.left_container, weight=1)
        self.results_frame.add(self.right_container, weight=1)

        # Vorschau-Label (auch wenn nicht im Debug-Modus)
        self.preview_label = ttk.Label(self.right_container, text="[ " + self.texts["placeholder_info"] + " ]", anchor="center", background="#dddddd")
        self.preview_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


        self.enlarge_button = ttk.Button(self.right_container, text="🔍 " + self.texts["enlarge"], command=self._enlarge_image)
        self.enlarge_button.pack(pady=10)


        # Canvas + Scrollbars
        self.left_canvas = tk.Canvas(self.left_container, bg="#ffffff", highlightthickness=0)
        self.left_canvas.grid(row=0, column=0, sticky="nsew")


        self.left_scrollbar = ttk.Scrollbar(self.left_container, orient="vertical", command=self.left_canvas.yview)
        self.left_scrollbar.grid(row=0, column=1, sticky="ns")


        self.left_hscrollbar = ttk.Scrollbar(self.left_container, orient="horizontal", command=self.left_canvas.xview)
        self.left_hscrollbar.grid(row=1, column=0, sticky="ew")


        self.left_canvas.configure(yscrollcommand=self.left_scrollbar.set, xscrollcommand=self.left_hscrollbar.set)


        # Frame IN Canvas (für Einträge)
        self.left_frame = ttk.Frame(self.left_canvas)
        self.canvas_window = self.left_canvas.create_window((0, 0), window=self.left_frame, anchor="nw")


        # Scrollbereich updaten
        def _on_frame_configure(event):
            self.left_canvas.configure(scrollregion=self.left_canvas.bbox("all"))


        self.left_frame.bind("<Configure>", _on_frame_configure)


        # Fix: Canvas-Size anpassen, damit Frame nicht unsichtbar ist
        def _on_canvas_resize(event):
            canvas_width = event.width
            self.left_canvas.itemconfig(self.canvas_window, width=canvas_width)


        self.left_canvas.bind("<Configure>", _on_canvas_resize)


        # Konfig für Gewichtung
        self.left_container.rowconfigure(0, weight=1)
        self.left_container.columnconfigure(0, weight=1)
        
        # Legende (unabhängig vom Debug-Modus)
        self.legend_frame = tk.Frame(self.root, bg="#f9f9f9")
        self.legend_frame.pack(side=tk.BOTTOM, pady=5)


        tk.Label(self.legend_frame, bg="#fff5cc", width=2, height=1, relief="solid").pack(side=tk.LEFT, padx=5)
        tk.Label(self.legend_frame, text="= " + self.texts["legend_yellow"].split("=", 1)[-1], bg="#f9f9f9").pack(side=tk.LEFT, padx=(0, 20))


        tk.Label(self.legend_frame, bg="#cce0ff", width=2, height=1, relief="solid").pack(side=tk.LEFT, padx=5)
        tk.Label(self.legend_frame, text="= " + self.texts["legend_blue"].split("=", 1)[-1], bg="#f9f9f9").pack(side=tk.LEFT)


        # Dummy-Dateien
        if self.debug_mode:
            self.checkbox_refs = []  # Liste zum Speichern (optional)

            dummy_data = [
                ("Pictures", [("IMG_001.jpg", "blue"), ("IMG_002.jpg", "yellow")]),
                ("Screenshots", [("IMG_002.jpg", "yellow"), ("IMG_003.jpg", "blue")])
            ]

            for folder, files in dummy_data:
                folder_label = ttk.Label(self.left_frame, text=f"📂 {folder}", font=("Arial", 12, "bold"))
                folder_label.pack(anchor="w", pady=(10, 2))

                for filename, color in files:
                    frame = ttk.Frame(self.left_frame, style="Default.TFrame")
                    frame.pack(fill=tk.X, pady=2)

                    bg_color = "#cce0ff" if color == "blue" else "#fff5cc"
                    var = tk.BooleanVar()

                    # Dateiname als echtes Label (nicht ttk, damit bg funktioniert)
                    file_label = tk.Label(frame, text=filename, bg="#ffffff", padx=5)
                    file_label.pack(side=tk.LEFT)

                    chk = ttk.Checkbutton(frame, variable=var)
                    chk.pack(side=tk.LEFT)

                    def on_check(var=var, frame=frame, label=file_label, color=color):
                        if var.get():
                            frame.configure(style=f"{color}.TFrame")
                            label.configure(bg=bg_color)
                        else:
                            frame.configure(style="Default.TFrame")
                            label.configure(bg="#ffffff")

                    # Verknüpfung aktivieren
                    var.trace_add("write", lambda *_,
                                v=var, f=frame, l=file_label, c=color, bg=bg_color:
                                self._handle_check(v, f, l, c, bg))

                    # Optional speichern
                    self.checkbox_refs.append((var, frame, file_label, color))

            # Vorschau rechts
            self.preview_label = ttk.Label(self.right_container, text="[ Bildvorschau ]", anchor="center", background="#dddddd")
            self.preview_label.pack(fill=tk.BOTH, expand=True)

            self.enlarge_button = ttk.Button(self.right_container, text="🔍 " + self.texts["enlarge"], command=self._enlarge_image)
            self.enlarge_button.pack(pady=10)

            legend_frame = tk.Frame(self.root, bg="#f9f9f9")
            legend_frame.pack(side=tk.BOTTOM, pady=5)

            tk.Label(legend_frame, bg="#fff5cc", width=2, height=1, relief="solid").pack(side=tk.LEFT, padx=5)
            tk.Label(legend_frame, text="= " + self.texts["legend_yellow"].split("=", 1)[-1], bg="#f9f9f9").pack(side=tk.LEFT, padx=(0, 20))

            tk.Label(legend_frame, bg="#cce0ff", width=2, height=1, relief="solid").pack(side=tk.LEFT, padx=5)
            tk.Label(legend_frame, text="= " + self.texts["legend_blue"].split("=", 1)[-1], bg="#f9f9f9").pack(side=tk.LEFT)

    def _handle_check(self, var, frame, label, color, bg_color):
        if var.get():
            frame.configure(style=f"{color}.TFrame")
            label.configure(bg=bg_color)
        else:
            frame.configure(style="Default.TFrame")
            label.configure(bg="#ffffff")

    def _clear_results(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()

    def _show_results(self, structured):
        self.checkbox_refs = []
        for folder, files in structured.items():
            folder_label = ttk.Label(self.left_frame, text=f"📂 {os.path.basename(folder)}", font=("Arial", 12, "bold"))
            folder_label.pack(anchor="w", pady=(10, 2))

            for file_path, color in files:
                filename = os.path.basename(file_path)
                frame = ttk.Frame(self.left_frame, style="Default.TFrame")
                frame.pack(fill=tk.X, pady=2)

                bg_color = "#cce0ff" if color == "blue" else "#fff5cc" if color == "yellow" else "#ffffff"
                var = tk.BooleanVar()

                # AUTOMATISCH MARKIEREN
                if color in ("blue", "yellow"):
                    var.set(True)

                file_label = tk.Label(frame, text=filename, bg="#ffffff", padx=5)
                file_label.pack(side=tk.LEFT)
                file_label.bind("<Button-1>", lambda e, p=file_path: self._show_image(p))

                chk = ttk.Checkbutton(frame, variable=var)
                chk.pack(side=tk.LEFT)

                var.trace_add("write", lambda *_,
                            v=var, f=frame, l=file_label, c=color, bg=bg_color:
                            self._handle_check(v, f, l, c, bg_color))

                self.checkbox_refs.append((var, frame, file_label, color, file_path))
                self._handle_check(var, frame, file_label, color, bg_color)

    def _show_image(self, path):
        from PIL import Image, ImageTk
        try:
            image = Image.open(path)
            image.thumbnail((1000, 600))  # Maxgröße der Vorschau
            photo = ImageTk.PhotoImage(image)


            self.preview_label.configure(image=photo)
            self.preview_label.image = photo  # Verhindert Garbage Collection
        except Exception as e:
            print("Bild konnte nicht geladen werden:", e)

    def _update_folder_tags(self):
        for widget in self.folder_tag_container.winfo_children():
            widget.destroy()
        for folder in self.selected_folders:
            name = os.path.basename(folder)
            tag_frame = ttk.Frame(self.folder_tag_container)
            tag_frame.pack(side=tk.LEFT, padx=4)
            ttk.Label(tag_frame, text=name, background="#dddddd", padding=(6, 2)).pack(side=tk.LEFT)
            ttk.Button(tag_frame, text="❌", width=2,
                       command=lambda f=folder: self._remove_folder(f)).pack(side=tk.LEFT)

    def _remove_folder(self, folder):
        if folder in self.selected_folders:
            self.selected_folders.remove(folder)
            self._update_folder_tags()

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder and folder not in self.selected_folders:
            self.selected_folders.append(folder)
            self._update_folder_tags()

    def scan_for_duplicates(self):
        if not self.selected_folders:
            messagebox.showwarning(self.texts["warning"], self.texts["no_folder_selected"])
            return

        self._clear_results()

        groups = find_duplicate_groups(self.selected_folders)
        structured = classify_duplicates(groups)
        self._show_results(structured)

    def delete_selected(self):
        if not hasattr(self, "checkbox_refs") or not self.checkbox_refs:
            messagebox.showwarning(self.texts["warning"], "Keine Dateien ausgewählt.")
            return


        # Markierte Dateien sammeln
        files_to_delete = []
        for item in self.checkbox_refs:
            if len(item) == 5:
                var, frame, label, color, file_path = item
                if var.get():  # Checkbox angehakt
                    files_to_delete.append(file_path)


        if not files_to_delete:
            messagebox.showinfo(self.texts["info"], "Keine Dateien markiert.")
            return


        # Sicherheitsabfrage
        confirm = messagebox.askyesno(
            "Bestätigen",
            f"Möchten Sie wirklich {len(files_to_delete)} Datei(en) löschen?\nDiese Aktion kann nicht rückgängig gemacht werden!"
        )


        if not confirm:
            return


        deleted = 0
        errors = 0


        for path in files_to_delete:
            try:
                if os.path.exists(path):
                    os.remove(path)
                    deleted += 1
            except Exception as e:
                print("Fehler beim Löschen:", e)
                errors += 1


        # UI zurücksetzen
        self._clear_results()
        self.preview_label.configure(text="[ " + self.texts["placeholder_info"] + " ]", image="")
        self.preview_label.image = None


        # Rückmeldung
        messagebox.showinfo(
            self.texts["info"],
            f"{deleted} Datei(en) gelöscht.\nFehler: {errors}"
        )

        # Nach dem Löschen: Duplikate neu scannen und anzeigen
        groups = find_duplicate_groups(self.selected_folders)
        structured = classify_duplicates(groups)
        if structured:
            self._show_results(structured)
        else:
            self._clear_results()
            no_dupes_label = ttk.Label(self.left_frame, text=self.texts["no_duplicates_found"], foreground="gray")
            no_dupes_label.pack(pady=20)

    def toggle_language(self):
        self.language = "de" if self.language == "en" else "en"
        self.texts = load_language(self.language)
        self._refresh_texts()

    def _refresh_texts(self):
        self.btn_select_folder.config(text=self.texts["select_folder"])
        self.btn_scan.config(text=self.texts["scan_duplicates"])
        self.btn_delete.config(text=self.texts["delete_selected"])
        self.btn_language.config(text=self.texts["language"])
        self.btn_exit.config(text=self.texts["exit"])

        self.enlarge_button.config(text="🔍 " + self.texts["enlarge"])     
        self.preview_label.config(text=self.texts["placeholder_info"])

        self.preview_label.config(text="[ " + self.texts["placeholder_info"] + " ]")
        self.enlarge_button.config(text="🔍 " + self.texts["enlarge"])

        # Legendentexte dynamisch aktualisieren
        for widget in self.legend_frame.winfo_children():
            widget.destroy()
        tk.Label(self.legend_frame, bg="#fff5cc", width=2, height=1, relief="solid").pack(side=tk.LEFT, padx=5)
        tk.Label(self.legend_frame, text="= " + self.texts["legend_yellow"].split("=", 1)[-1], bg="#f9f9f9").pack(side=tk.LEFT, padx=(0, 20))
        tk.Label(self.legend_frame, bg="#cce0ff", width=2, height=1, relief="solid").pack(side=tk.LEFT, padx=5)
        tk.Label(self.legend_frame, text="= " + self.texts["legend_blue"].split("=", 1)[-1], bg="#f9f9f9").pack(side=tk.LEFT)


    def _refresh_placeholder(self):
        for widget in self.results_frame.winfo_children():
            if isinstance(widget, ttk.Label):
                widget.config(text=self.texts["placeholder_info"])

    def _enlarge_image(self):
        messagebox.showinfo("Zoom", "Bildvergrößerung folgt bald...")
