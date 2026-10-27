# Phil Splash — Würzburg Portraits

Mehrsprachige Landingpage für Reisegruppen und Foto-Porträts. Statische HTML-Seiten: Englisch, vereinfachtes/traditionelles Chinesisch, Japanisch, Deutsch. Alle Inhalte sind bereits ohne JavaScript lesbar.

## Vorschau und Änderungen

Voraussetzung: Python 3. Keine Bibliotheken, Paketinstallation oder kostenpflichtigen Dienste nötig.

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 4173 --directory docs
```

- **Preis, Mindestgruppengröße und E-Mail:** `site.config.json`. Der Startpreis ist 30 EUR pro Foto-Porträt, Live-Termine ab 10 Personen mit individuellem Gruppenangebot. Anschließend neu bauen.
- **Texte:** `content.json` (EN/DE), `content-asian.json` (ZH/JA).
- **Gestaltung:** `style.css`; **Anfrage/Video-Verhalten:** `app.js`.
- **Domain:** `baseUrl` in `site.config.json` anpassen oder beim Bauen `SITE_URL=https://example.com` setzen. Eine neue Domain muss separat registriert und beim Hoster verbunden werden. Es wurde keine Domain gekauft. Empfehlung als Marke: `wuerzburgportraits.de` oder `portraits.phil-splash.de`; Verfügbarkeit nicht geprüft.

## Veröffentlichung

GitHub Pages veröffentlicht den erzeugten Ordner `docs/` bei jedem Push auf `main`. Nach einer Text- oder Preisänderung zuerst lokal bauen und prüfen, danach die aktualisierten Quelldateien und `docs/` gemeinsam committen und pushen. In GitHub unter Settings → Pages ist `main` / `docs` als Quelle ausgewählt.

Vercel ist als Alternative vorbereitet: Repository importieren, `vercel.json` wird erkannt. Bei einem Wechsel `baseUrl`, Anbieterangaben zum Hosting in allen Sprachen und ggf. Domain aktualisieren. Kein Backend und keine Geheimnisse erforderlich.

## Auffindbarkeit

Eigene Sprach-URLs, vollständiges statisches HTML, gegenseitige hreflang-Verweise, selbstreferenzierende Canonicals, Sitemap, Social-Metadaten und strukturierte Daten (Person, Services, Preis, FAQ). `facts.json` und `llms.txt` ergänzen die öffentlich lesbaren Informationen; sie sind kein Rankingversprechen.

Die `robots.txt` ist für einen späteren Betrieb auf einer eigenen Domain vorbereitet. Bei GitHub-Projektseiten unter `/wuerzburg-portraits/` gilt die robots.txt der Host-Domain, nicht die Datei im Projekt-Unterordner. Inhalte werden nicht mit `noindex` blockiert.

Nach der Veröffentlichung: Von der bestehenden Künstlerwebsite auf die Sprachseiten verlinken. Eigene Domain in Google Search Console und Bing Webmaster Tools verifizieren und Sitemap einreichen. Das setzt Zugriff auf diese Konten bzw. DNS voraus und erfolgt nicht automatisch durch dieses Projekt. Für Festlandchina bietet die Seite lokale Bilder, Systemschriften und eine direkte E-Mail-Anfrage; YouTube bleibt optional. Erreichbarkeit aus Festlandchina wurde nicht vor Ort geprüft. Muttersprachliche Endredaktion wird für die Übersetzungen empfohlen.

## Besucherfunktionen

Die Buttons wählen das passende Angebot vor. Die Maske bereitet eine strukturierte englische E-Mail inklusive bevorzugter Korrespondenzsprache vor. Keine automatische Zusendung, keine Foto-Uploads und keine serverseitige Speicherung. Kopierfunktion und sichtbarer Text als Alternative zum E-Mail-Programm. Fotos werden nach Vereinbarung als E-Mail-Anhang geschickt.

YouTube lädt erst nach expliziter Zustimmung im Video-Dialog. Beim Schließen wird die Verbindung beendet; die Zustimmung wird nicht gespeichert. Keine Analysewerkzeuge oder externen Fonts.

## Quellen und Bildrechte

- Künstlerbiografie und Anbieteranschrift: https://www.phil-splash.de/ und https://www.phil-splash.de/contactimpressum/
- Würzburg-Bezug: https://zugabedigital.wuerzburg.de/portraits-gegen-rechts-in-der-langen-kulturspeichernacht/
- Originalporträts: vom Nutzer bereitgestellte eigene Galerie https://phil-splash.imgbb.com/albums (Vietnam 2026, VR Bank Würzburg, ServiceNow).
- Live-Bild und erster Film: https://www.youtube.com/watch?v=4OF5U2tFSXY
- Zweiter Film/Vorschaubild: https://www.youtube.com/watch?v=YGdoD-1dvJ4
- Stadtmotiv: eigens erstellte KI-Illustration, entsprechend beschriftet; keine Dokumentarfotografie. Die Postkartenansicht ist eine CSS-Montage mit einer Originalzeichnung als ausdrücklich bezeichnete Gestaltungsidee, keine zugesicherte Arbeit oder fertige Produktprobe.
- Tourismus: https://www.wuerzburg.de/en/

Impressum und Datenschutzhinweise verwenden vorhandene öffentliche Anbieterangaben und beschreiben die implementierte Funktion. Ggf. vorhandene USt-IdNr./W-IdNr., aktuelle Anbieterangaben sowie die steuerliche Behandlung des Endpreises sind vom Betreiber zu ergänzen bzw. zu bestätigen. Nicht bestätigte Leistungsversprechen (feste Dauer, Liefergarantie, regelmäßiger Standplatz, enthaltene Live-Übersetzung) werden nicht gemacht.

Inhalte und Kunstwerke © Phil Splash. Keine offene Lizenz für Kunstwerke oder Marketingmaterial.
