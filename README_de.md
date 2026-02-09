[🇬🇧 English Version](README.md)  
![AGPL v3 License](https://img.shields.io/badge/license-AGPLv3-blue.svg)
![Windows](https://img.shields.io/badge/platform-Windows-blue)
![Status](https://img.shields.io/badge/status-Prototyp-orange)


# Mamas Photo Cleaner – Einfach. Klar. Lokal.

Mamas Photo Cleaner ist ein benutzerfreundliches Windows-Tool zur Erkennung und sicheren Löschung doppelter Dateien – egal ob Fotos, PDFs, Excel-Dateien oder Systemdaten.  
Die App entstand, weil meine Mutter sich eine einfache Lösung gewünscht hat, um doppelte Dateien loszuwerden – ohne Technikstress. Aus dieser Idee wurde ein voll funktionstüchtiger Prototyp, den jetzt jeder nutzen kann.

---

## 🧰 Hauptfunktionen

- Erkennt doppelte Dateien anhand ihres Inhalts (Hash-Vergleich)
- Unterstützt viele Formate: PNG, JPG, PDF, DOCX, XLSX, JSON uvm.
- Farbige Markierung zur besseren Übersicht:
  - 🟦 Blau = Duplikat im selben Ordner
  - 🟨 Gelb = Duplikat in einem anderen Ordner
  - Weiß = Original, wird nicht gelöscht
- Bildvorschau (für Bildformate)
- Sichere Löschfunktion mit Sicherheitsabfrage
- Sprachumschaltung (Deutsch/Englisch)
- Exportfunktion als ZIP und CSV (optional)

---

## 💻 Systemanforderungen

- Windows-System (getestet ab Windows 10)
- Keine Installation nötig – einfach entpacken und starten
- Keine Internetverbindung erforderlich
- Keine externen Programme oder Python-Abhängigkeiten

---

## ⚙️ Installation

1. Lade das ZIP-Archiv von GitHub herunter  
2. Entpacke es per Rechtsklick → „Alle extrahieren“  
3. Starte die App mit Doppelklick auf `MamasPhotoCleaner.exe`  

**Tipp:** Am besten direkt auf den Desktop legen – das sorgt für stabile Zugriffe auf Ordner.

---

## 🚀 Nutzung – Schritt für Schritt

### 1. Ordner auswählen  
Klicke auf „Ordner auswählen“ und wähle gezielt einen oder mehrere Ordner aus.  
**Wichtig:** Bitte keine riesigen Oberordner wie den Desktop – das kann zum Absturz führen.

### 2. Nach Duplikaten suchen  
Klicke auf „Nach Duplikaten suchen“.  
Die gefundenen Duplikate erscheinen farbig markiert in der Liste.

### 3. Übersicht verstehen  
Die Farben bedeuten:  
- 🟦 Blau: Duplikat im selben Ordner  
- 🟨 Gelb: Duplikat in einem anderen Ordner  
- Weiß: Original, wird nicht gelöscht

Bilddateien erscheinen rechts in der Vorschau.  
Die Vorschau kann per Schieberegler größer oder kleiner dargestellt werden.

### 4. Dateien löschen  
Klicke auf „Löschen“. Es erscheint eine Sicherheitsabfrage, z. B.:  
> „Möchten Sie wirklich 14 Dateien löschen?“  
Nur angehakte Duplikate werden entfernt.  
**Tipp:** Nach dem Löschen die App neu starten.

### 5. Exportfunktion (optional)  
Exportiere markierte Dateien als ZIP-Archiv und CSV-Datei.  
Ideal für Entwickler – normale Nutzer können diesen Schritt ignorieren.

### 6. Sprache wechseln  
Oben rechts kannst du jederzeit zwischen Deutsch und Englisch umschalten.

---

## 🖼️ Screenshots mit Erklärung

### Screenshot 1 – Normale Ansicht  
![Screenshot 1](images/Screenshot%202026-02-09%20143043.png)  
Links sieht man erkannte PNG-Dateien in der Liste, rechts die Bildvorschau.  
🟦 Blau = Duplikat im selben Ordner (angekreuzt)  
🟨 Gelb = Duplikat in anderem Ordner (angekreuzt)  
Weiß = Original

---

### Screenshot 2 – Bild maximiert  
![Screenshot 2](images/Screenshot%202026-02-09%20132432.png)  
Die rechte Seite mit der Bildvorschau wurde ganz nach links gezogen – große Bildansicht.

---

### Screenshot 3 – Liste maximiert  
![Screenshot 3](images/Screenshot%202026-02-09%20132413.png)  
Die linke Seite (Dateiliste) wurde vergrößert – ideal für viele Dateien.

---

### Screenshot 4 – Löschabfrage  
![Screenshot 4](images/Screenshot%202026-02-09%20143110.png)  
Zeigt die Sicherheitsabfrage beim Klick auf „Löschen“.

---

### Screenshot 5 – Sprachwechsel & andere Dateitypen  
![Screenshot 5](images/Screenshot%202026-02-09%20145334.png)  
Sprache wurde auf Englisch gestellt.  
Es sind JSON, .pth, Bilder und Systemdateien sichtbar.

---

### Screenshot 6 – Weitere Formate im Test  
![Screenshot 6](images/Screenshot%202026-02-09%20150130.png)  
Excel, PDF, Markdown, GitKeep, diverse Ordner wie Templates, Workshops, usw.

---

## ⚠️ Technische Hinweise

- Erkennt nur exakte Duplikate (keine Ähnlichkeitssuche)
- PDF-/Office-Dateien haben keine Vorschau
- Große Ordner können die App abstürzen lassen
- Nach größeren Aktionen App neu starten
- Vergrößerung aktuell nur per Schieberegler – Button ist in der Pro-Version geplant

---

## 🧪 Grenzen der kostenlosen Version

- Keine Vorschau für PDFs oder Office-Dateien
- Kein Vergrößerungs-Button für Bilder
- Kein Scan großer Oberordner empfohlen
- Keine automatische Auswahloptimierung

---

## 🔜 Geplante Pro-Version

- Schnellere Verarbeitung großer Ordner
- Vergleich ähnlicher Dateien (nicht nur identisch)
- Vorschau für PDF, Text, Office
- Bildvergrößerung per Button
- Erweiterte Filterfunktionen
- Und vieles mehr

---

## 📜 Lizenz & Offenheit

- Lizenz: AGPLv3  
- Keine Werbung, kein Tracking, kein Konto nötig  
- Kostenlos nutzbar, veränderbar, weitergebbar (mit Namensnennung)  
- Quellcode öffentlich auf GitHub

---

## ✨ Hintergrund

Entstanden aus einem echten Wunsch: Ordnung im Dateichaos – ohne Fachchinesisch.  
Was für meine Mutter gedacht war, hilft heute auch anderen Menschen – privat und beruflich.