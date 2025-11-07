# Vogue Cover Skin Tone Analysis

## Projektbeschreibung

Dieses Projekt untersucht die **Darstellung von Hauttönen auf Vogue-Covern** über die letzten Jahrzehnte hinweg.
Ziel war es zu analysieren, ob sich die **Helligkeit der dargestellten Hautfarben** im Laufe der Zeit verändert hat und ob dadurch Rückschlüsse auf **Repräsentation und Diversität** gezogen werden können.

Ergebnis:

> Die dargestellte Helligkeit von Hautfarben auf Vogue-Covern ist über die Jahre tendenziell **dunkler geworden** – insbesondere ab dem Jahr 2012.

---

## Kontext

<img width="2000" height="1125" alt="team_vogue (verschoben)" src="https://github.com/user-attachments/assets/2531d565-a4bd-4b99-9562-20bfc2e3be46" />



* **Thema:** Repräsentation von People of Color (POC) auf Mode-Covern
* **Fokus:** Entwicklung der Hautfarbdarstellung über Zeit, Regionen und Modemagazine hinweg

---

## Vorgehen

### 1. Datenbeschaffung

* Quelle: [Vogue’s Covers: ARCHIVES Blog](http://voguescovers.blogspot.com/p/blog-page_1.html)
* 21 Regionen, 4085 Coverbilder (1998–2022)
* Gescraped mit **Python**
* Gespeicherte Metadaten:

  * Bild
  * Dateiname
  * Region
  * URL
  * Jahr (per Hand gemappt)

### 2. Gesichtserkennung

<img width="2000" height="1125" alt="team_vogue (verschoben) 2" src="https://github.com/user-attachments/assets/8f59c7c8-bebd-437e-8a67-0887cd9864cd" />


* Modell: **MTCNN (Multi-Task Cascaded Convolutional Network)**
* Ziel: Erkennung aller Gesichter auf den Covern, unabhängig von Farbe oder Beleuchtung
* Evaluierung:

  * Accuracy: 0.82
  * Precision: 0.95
  * Recall: 0.82
  * F1-Score: 0.87

### 3. Hautfarbenerkennung

<img width="2000" height="1125" alt="team_vogue (verschoben) 3" src="https://github.com/user-attachments/assets/2291333d-673e-4f05-b6e3-cbd056875ce3" />

<img width="10000" height="5625" alt="team_vogue (verschoben) 4" src="https://github.com/user-attachments/assets/4e5a4eed-e04f-41b6-b364-972caff2e01d" />


* Umwandlung in **HSV** und **YCbCr** Farbräume
* Schwellenwerte:

  * HSV: H 0–17, S 15–170, V 0–255
  * YCbCr: Y 0–255, Cr 135–180, Cb 85–135
* Berechnung eines **durchschnittlichen Hautfarbwerts** pro Gesicht

### 4. Ausreißererkennung

<img width="2000" height="1125" alt="team_vogue (verschoben) 7" src="https://github.com/user-attachments/assets/4203e2a4-2bfe-43f3-a22c-e546f0533753" />


* Methoden: **IQR** (Interquartilsabstand) & **MAD** (Mittlere absolute Abweichung)
* Entfernt:

  * Ungewöhnlich gefärbte Gesichter (Make-up, Licht, Filter)
  * Schwarz-Weiß-Bilder
  * Bilder ohne Gesichter

### 5. Analyse & Visualisierung

<img width="2000" height="1125" alt="team_vogue (verschoben) 5" src="https://github.com/user-attachments/assets/c56e2500-bea6-4446-aaa9-a4614d27d67f" />


* Darstellung der Helligkeitsentwicklung über die Jahre
* Regionale Analysen (z. B. Deutschland)
* Ergebnisplots und Boxplots zur Verteilung der Hauttöne

---

## Ergebnisse

* **Trend:** Hautfarben auf Vogue-Covern wurden im Zeitverlauf dunkler.
* **Ursache:** Zunehmende Diversität und bewusste Repräsentation von POC.
* **Einschränkungen:**

  * Hauterkennung bei sehr dunklen Hauttönen teilweise ungenau
  * Helligkeit stark abhängig von Beleuchtung und Nachbearbeitung der Cover

---

## Ausblick

Zukünftige Erweiterungen:

* Interaktive Plots (z. B. mit Plotly oder Dash)
* Fokussierte Analyse auf bestimmte Models
* Einbeziehung anderer Modemagazine 

---

## Technologien

* **Python**
* Bibliotheken:

  * `opencv-python`
  * `mtcnn`
  * `numpy`, `pandas`
  * `matplotlib`, `seaborn`
  * `scikit-learn`
* **Jupyter Notebooks** für EDA & Visualisierung

---

## Quellen

* [Vogue’s Covers Blog](http://voguescovers.blogspot.com/p/blog-page_1.html)
* [MTCNN – Robust Face Detection](https://towardsdatascience.com/robust-face-detection-with-mtcnn-400fa81adc2e)
* [Skin Detection using HSV & YCbCr (GitHub)](https://github.com/CHEREF-Mehdi/SkinDetection)
* [Colorlines: “Rihanna Goes White and Blonde”](https://colorlines.com/article/rihanna-goes-white-and-blonde-new-vogue-uk-cover/)
* [British Vogue – February 2022 Cover Story](https://www.vogue.de/mode/artikel/cover-britische-vogue-zeigt-9-junge-schwarze-frauen-die-model-sein-neu-definieren)

---

## Autoren

Lena: Gesichtserkennung, Hautton-Erkennung, Plots
Susanne: Scraper, EDA, Modell-Evaluation, Anwendung auf gescrapte Daten
