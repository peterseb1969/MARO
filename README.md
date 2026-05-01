

# **Dokumentation – Jump'n'Run Projekt**

**Autor:** MARO  **Datum (letzte Aktualisierung):** 01.05.2026 **Projektname:** MaRo Gaming – Jump'n'Run **Aktuelle Version:** 0.2.0 **Repository:** https://github.com/peterseb1969/MARO

---

## **1\. Projektidee**

Ziel des Schulprojekts ist die Entwicklung eines klassischen Jump'n'Run-Spiels in Python. Die Spielfigur soll über 30 Stockwerke nach oben gelangen, indem sie von Plattform zu Plattform springt. Leitern oder andere Hilfsmittel gibt es nicht.

Das Projekt wird **inkrementell** entwickelt: Jede Version fügt eine klar abgegrenzte Funktion hinzu, wird per Git committet, mit einem Tag (z. B. `v0.2.0`) markiert und im `CHANGELOG.md` festgehalten. So lässt sich der Entwicklungsverlauf jederzeit nachvollziehen.

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
| Versionskontrolle | Git \+ GitHub |

### **Hinweis zur Python-Version**

Ein erster Versuch mit **Python 3.14** scheiterte: Pygame 2.6.1 ist noch nicht vollständig kompatibel mit Python 3.14. Beim Import des `pygame.font`\-Moduls trat ein zirkulärer Importfehler auf. Nach einem Wechsel auf **Python 3.13.13** lief das Programm problemlos.

---

## **3\. Projekt-Setup**

### **3.1 Projektstruktur**

* PythonProject/  
* ├── .venv/              \# Virtuelle Umgebung (nicht in Git)  
* ├── .gitignore          \# Ausschluss von venv, Caches, IDE-Dateien  
* ├── CHANGELOG.md        \# Änderungsprotokoll  
* ├── README.md           \# Diese Dokumentation  
* └── main.py             \# Hauptprogramm


  ### **3.2 Schritt-für-Schritt-Einrichtung**

1. **Python 3.13 installieren** (z. B. `brew install python@3.13`).  
2. **Projektordner anlegen** und in den Ordner wechseln.  
3. **Virtuelle Umgebung erstellen:** `python3.13 -m venv .venv`  
4. **Aktivieren:** `source .venv/bin/activate`  
5. **Pygame installieren:** `pip install pygame`  
6. In **PyCharm** unter *Settings → Project → Python Interpreter* den Interpreter aus `.venv/bin/python` wählen.

   ### **3.3 Probleme bei der Installation**

Während der Einrichtung im Zug schlug `pip install pygame` fehl, weil das Hotspot-Netzwerk keine Verbindung zu `pypi.org` zuließ (`No route to host`). In einem stabileren Netzwerk funktionierte die Installation sofort.

---

## **4\. Versionsverwaltung mit Git und GitHub**

### **4.1 Erstmalige Einrichtung**

* git init \-b main  
* git add .gitignore main.py README.md CHANGELOG.md  
* git commit \-m "Initial commit"  
* git remote add origin https://github.com/peterseb1969/MARO.git  
* git push \-u origin main


Authentifizierung über einen **Personal Access Token**. Wichtig: Bei *Fine-grained Tokens* muss die Permission **Contents: Read and write** für das Repository gesetzt werden – sonst gibt es einen 403-Fehler beim Push.

### **4.2 Workflow für jede neue Version**

* git add .  
* git commit \-m "vX.Y.Z: Kurze Beschreibung"  
* git push  
* git tag \-a vX.Y.Z \-m "Version X.Y.Z: Beschreibung"  
* git push origin vX.Y.Z


Versionsnummern folgen dem Schema **MAJOR.MINOR.PATCH** (Semantic Versioning).

### **4.3 `.gitignore`**

* .venv/  
* \_\_pycache\_\_/  
* \*.pyc  
* .idea/  
* .DS\_Store


Die virtuelle Umgebung darf **niemals** ins Repo – sie ist groß, plattformspezifisch und auf jedem Rechner neu erzeugbar.

---

## **5\. Versionshistorie**

### **Version 0.1.0 – Grundgerüst**

**Funktionen:**

* Pygame-Fenster (800 × 600 Pixel) wird geöffnet.  
* Hauptschleife mit Event-Verarbeitung.  
* Anzeige der zuletzt gedrückten Taste mittig auf dem Bildschirm.  
* Frame-Begrenzung auf 60 FPS.

**Zweck:** Etablierung der zentralen Pygame-Bausteine (Fenster, Event-Schleife, Zeichenroutine, Frame-Timer) als Basis für alles Weitere.

### **Version 0.2.0 – Spielfigur und Bewegung *(aktuell)***

**Funktionen:**

* Spielfigur als rotes Rechteck (40 × 60 Pixel), Startposition mittig am unteren Bildschirmrand.  
* Horizontale Bewegung mit den Pfeiltasten **links** und **rechts**, Geschwindigkeit 5 Pixel pro Frame.  
* Begrenzung der Figur am linken und rechten Fensterrand: Sie kann das Spielfeld nicht verlassen.  
* Anzeige der zuletzt gedrückten Taste wurde entfernt (war reine Testfunktion).  
  ---

  ## **6\. Programmaufbau (Stand v0.2.0)**

Das Programm besteht aus vier logischen Abschnitten in `main.py`:

### **6.1 Setup**

* `pygame.init()` initialisiert alle Pygame-Module.  
* `pygame.display.set_mode((800, 600))` erstellt das Fenster.  
* `pygame.time.Clock()` regelt die Bildwiederholrate.  
* Konstanten für Farben (RGB-Tupel), Spielfigur-Größe und Geschwindigkeit werden zentral definiert. So lassen sich Werte später leicht anpassen.  
* Die Spielfigur wird als `pygame.Rect(x, y, breite, höhe)` angelegt. Ein `Rect` ist Pygames eingebauter Rechteck-Datentyp und speichert Position und Größe in einem Objekt. Er ist die Grundlage für späteres Zeichnen, Bewegen und Kollisions­prüfen.

  ### **6.2 Hauptschleife**

Die Schleife läuft bis zu 60-mal pro Sekunde und führt jedes Mal fünf Aufgaben aus:

1. **Events abarbeiten** – nur noch das Schließen des Fensters (`pygame.QUIT`) wird hier behandelt.  
2. **Tastatur abfragen** – `pygame.key.get_pressed()` liefert den **aktuellen Zustand aller Tasten**. Anders als das `KEYDOWN`\-Event, das nur einmalig beim Drücken feuert, eignet sich `get_pressed()` perfekt für gedrückt-gehaltene Tasten (Bewegung).  
3. **Position begrenzen** – `player.left` und `player.right` werden so korrigiert, dass die Figur den sichtbaren Bereich nicht verlässt.  
4. **Zeichnen** – Hintergrund mit `screen.fill(...)` löschen, dann die Figur mit `pygame.draw.rect(screen, farbe, rect)` zeichnen.  
5. **Frame anzeigen und FPS begrenzen** – `pygame.display.flip()` macht das neue Bild sichtbar, `clock.tick(60)` deckelt die Bildrate auf 60 FPS.

   ### **6.3 Aufräumen**

Nach Verlassen der Schleife wird Pygame mit `pygame.quit()` sauber heruntergefahren und das Programm mit `sys.exit()` beendet.

### **6.4 Wichtige Designentscheidungen**

* **`KEYDOWN` vs. `get_pressed()`:** Für kontinuierliche Bewegung (links/rechts) wird `get_pressed()` verwendet. Für punktuelle Aktionen (z. B. Springen in Version 0.3) wird später `KEYDOWN` zum Einsatz kommen, damit ein einzelner Tastendruck genau einen Sprung auslöst.  
* **`Rect` als zentrale Datenstruktur:** Die Spielfigur wird konsequent als `pygame.Rect` geführt. Dadurch lassen sich später Kollisionen mit Plattformen ohne zusätzlichen Code bewerkstelligen (`player.colliderect(plattform)`).  
* **Konstanten am Anfang:** Werte wie `PLAYER_SPEED` oder `PLAYER_WIDTH` werden ganz oben als Konstanten in Großbuchstaben definiert. Das ist Python-Konvention und macht spätere Änderungen einfach.  
  ---

  ## **7\. Bedienung (Stand v0.2.0)**

| Taste | Wirkung |
| ----- | ----- |
| Pfeil **←** | Spielfigur nach links bewegen |
| Pfeil **→** | Spielfigur nach rechts bewegen |
| Fenster **schließen** | Programm sauber beenden |

Start: `python main.py` im aktivierten venv, oder grüner Run-Button in PyCharm.

---

## **8\. Getestete Funktionen**

| Test | v0.1.0 | v0.2.0 |
| ----- | ----- | ----- |
| Fenster öffnet sich in 800 × 600 Pixel | OK | OK |
| 60 FPS werden eingehalten | OK | OK |
| Schließen des Fensters beendet das Programm | OK | OK |
| Tastenanzeige zeigt korrekten Tastennamen | OK | — |
| Spielfigur wird gezeichnet | — | OK |
| Bewegung mit ← und → funktioniert flüssig | — | OK |
| Figur stoppt am linken Fensterrand | — | OK |
| Figur stoppt am rechten Fensterrand | — | OK |

---

## **9\. Ausblick (geplante nächste Schritte)**

| Version | Geplanter Inhalt |
| ----- | ----- |
| **v0.3.0** | Schwerkraft, Sprungfunktion (Leertaste) und ein fester Boden |
| **v0.4.0** | Mehrere statische Plattformen mit Kollisionserkennung |
| **v0.5.0** | Vertikal scrollende Kamera, die der Spielfigur folgt |
| **v0.6.0** | Prozedurale Generierung von 30 Stockwerken |
| **v0.7.0** | Spielende: Sieg auf Stockwerk 30, Game Over beim Herunterfallen |
| **v0.8.0** | Visuelle Aufwertung (Sprite-Grafiken, Parallax-Hintergrund) |
| **v0.9.0** | Soundeffekte und Hintergrundmusik |
| **v1.0.0** | Erste vollständig spielbare Fassung |

---

## **10\. Quellen**

* Offizielle Pygame-Dokumentation: https://www.pygame.org/docs/  
* Python-Dokumentation zu `venv`: https://docs.python.org/3/library/venv.html  
* Semantic Versioning: https://semver.org/lang/de/

