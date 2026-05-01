# **Dokumentation – Jump'n'Run Projekt (Version 0.1)**

**Autor:** MaRo  **Datum:** 01.05.2026 **Projektname:** MaRo Gaming – Jump'n'Run **Version:** 0.1 (Erste Testversion: Tastatureingabe-Anzeige)

---

## **1\. Projektidee**

Ziel des Schulprojekts ist die Entwicklung eines klassischen Jump'n'Run-Spiels in Python. Die Spielfigur soll über 30 Stockwerke nach oben gelangen, indem sie von Plattform zu Plattform springt. Leitern oder andere Hilfsmittel gibt es nicht.

Diese erste Version (0.1) enthält noch kein Spiel, sondern dient als **Grundgerüst**: Sie öffnet ein Fenster, liest Tastatureingaben ein und zeigt die zuletzt gedrückte Taste mittig auf dem Bildschirm an. Damit werden die zentralen Bausteine eines Pygame-Programms (Fenster, Event-Schleife, Zeichenroutine, Frame-Begrenzung) etabliert, auf denen die spätere Spielmechanik aufbauen kann.

---

## **2\. Entwicklungsumgebung**

| Komponente | Verwendete Version / Werkzeug |
| ----- | ----- |
| Betriebssystem | macOS |
| IDE | PyCharm |
| Programmiersprache | Python **3.13.13** |
| Bibliothek | pygame **2.6.1** (SDL 2.32.10) |
| Paketverwaltung | pip |
| Virtuelle Umgebung | `venv` (Standardmodul von Python) |

### **Hinweis zur Python-Version**

Ein erster Versuch mit **Python 3.14** scheiterte: Pygame 2.6.1 ist noch nicht vollständig kompatibel mit Python 3.14. Beim Import des `pygame.font`\-Moduls trat ein zirkulärer Importfehler auf. Nach einem Wechsel auf **Python 3.13.13** lief das Programm problemlos.

---

## **3\. Projekt-Setup**

### **3.1 Projektstruktur**

PythonProject/  
├── .venv/              \# Virtuelle Umgebung (nicht in Git committen)  
└── main.py             \# Hauptprogramm

### **3.2 Schritt-für-Schritt-Einrichtung**

**1\. Python 3.13 installieren** (z. B. über die offizielle Webseite python.org oder mit Homebrew):

brew install python@3.13

**2\. Projektordner anlegen und in den Ordner wechseln:**

mkdir PythonProject  
cd PythonProject

**3\. Virtuelle Umgebung erstellen:**

python3.13 \-m venv .venv

Eine virtuelle Umgebung ist ein abgeschotteter Python-Bereich nur für dieses Projekt. Bibliotheken, die hier installiert werden, beeinflussen nicht das System-Python und umgekehrt. Das macht Projekte reproduzierbar.

**4\. Virtuelle Umgebung aktivieren** (macOS / Linux):

source .venv/bin/activate

Sobald die venv aktiv ist, erscheint `(.venv)` am Anfang der Eingabezeile.

**5\. Pygame installieren:**

pip install pygame

**6\. In PyCharm den richtigen Interpreter wählen:** *Settings → Project → Python Interpreter →* den Interpreter aus `.venv/bin/python` auswählen. Andernfalls verwendet PyCharm beim Ausführen womöglich ein anderes Python und findet pygame nicht.

### **3.3 Probleme bei der Installation**

Während der Einrichtung im Zug schlug `pip install pygame` fehl, weil das Hotspot-Netzwerk keine Verbindung zu `pypi.org` zuließ (`No route to host`). In einem stabileren Netzwerk funktionierte die Installation sofort. **Lehre:** Pip benötigt eine zuverlässige Internetverbindung; bei Verbindungsproblemen liegt der Fehler meist nicht an Python oder Pygame.

---

## **4\. Programmaufbau (main.py)**

Das Programm besteht aus vier logischen Abschnitten:

### **4.1 Setup**

* `pygame.init()` initialisiert alle Pygame-Module.  
* `pygame.display.set_mode((800, 600))` erstellt das Fenster und liefert eine Zeichenfläche (`screen`).  
* Eine Schriftart wird mit `pygame.font.Font(None, 72)` geladen (Standardschrift, Größe 72 px).  
* `pygame.time.Clock()` regelt später die Bildwiederholrate.  
* Konstanten für Hintergrund- und Textfarbe werden als RGB-Tupel definiert.

### **4.2 Hauptschleife**

Die Hauptschleife (`while running:`) ist das Herzstück jedes Pygame-Programms. Sie wiederholt sich pro Sekunde bis zu 60-mal und führt jedes Mal vier Aufgaben aus:

1. **Events einlesen** – Pygame sammelt alle Ereignisse (Tastendruck, Mausklick, Fenster schließen) in einer Warteschlange. Über `for event in pygame.event.get()` werden sie nacheinander abgearbeitet:

   * `pygame.QUIT` → Schleife verlassen.  
   * `pygame.KEYDOWN` → mit `pygame.key.name(event.key)` den Namen der Taste ermitteln und in der Variablen `last_key` speichern.  
2. **Bildschirm zeichnen** – `screen.fill(BG_COLOR)` löscht das alte Bild, dann wird der Text mit `font.render(...)` in eine Bild-Oberfläche umgewandelt und mit `screen.blit(...)` mittig auf den Bildschirm kopiert.

3. **Frame anzeigen** – `pygame.display.flip()` macht das neu gezeichnete Bild sichtbar.

4. **Bildrate begrenzen** – `clock.tick(60)` sorgt dafür, dass die Schleife maximal 60-mal pro Sekunde läuft. Ohne diese Zeile würde der Prozessor unnötig stark belastet.

### **4.3 Aufräumen**

Nach dem Verlassen der Schleife wird Pygame mit `pygame.quit()` sauber beendet und das Programm mit `sys.exit()` geschlossen.

---

## **5\. Bedienung**

1. Programm in PyCharm starten (oder im Terminal: `python main.py`).  
2. Es öffnet sich ein Fenster (800 × 600 Pixel) mit dem Text *„Press any key…"*.  
3. Beim Drücken einer Taste erscheint deren Name (z. B. `space`, `a`, `left`) zentriert auf dem Bildschirm. Zusätzlich wird der Tastenname in der Konsole ausgegeben.  
4. Schließen des Fensters beendet das Programm.

---

## **6\. Getestete Funktionen**

| Test | Ergebnis |
| ----- | ----- |
| Fenster öffnet sich in 800 × 600 Pixel | OK |
| Buchstabentasten (a–z) werden korrekt erkannt | OK |
| Pfeiltasten werden als `up`/`down`/`left`/`right` angezeigt | OK |
| Leertaste wird als `space` angezeigt | OK |
| Schließen des Fensters beendet das Programm | OK |
| 60 FPS werden eingehalten | OK |

---

## **7\. Ausblick (geplante nächste Schritte)**

1. **Spielfigur** als Rechteck zeichnen, die mit den Pfeiltasten horizontal bewegt werden kann.  
2. **Schwerkraft** und **Sprung** implementieren (Variable `velocity_y`, die jede Frame um einen Gravitationswert erhöht wird).  
3. **Plattformen** als Liste von Rechtecken anlegen und Kollision mit der Figur prüfen.  
4. **Vertikale Kamera**, die der Figur beim Klettern nach oben folgt.  
5. **30 Stockwerke** prozedural generieren.  
6. **Visuelle Aufwertung**: Sprite-Grafiken (z. B. von kenney.nl), Parallax-Hintergrund, Soundeffekte.

---

## **8\. Quellen**

* Offizielle Pygame-Dokumentation: https://www.pygame.org/docs/  
* Python-Dokumentation zu `venv`: https://docs.python.org/3/library/venv.html

