# Würzburg Moments

Mehrsprachige Reiseinspiration für Besucher aus China und Japan: Würzburger Sehenswürdigkeiten entdecken und Porträt-Erlebnisse bei Phil Splash anfragen. Statische HTML-Seiten: Englisch, vereinfachtes/traditionelles Chinesisch, Japanisch, Deutsch. Alle Inhalte sind bereits ohne JavaScript lesbar.

## Vorschau und Änderungen

Voraussetzung: Python 3. Keine Bibliotheken, Paketinstallation oder kostenpflichtigen Dienste nötig.

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 4173 --directory docs
```

- **Preis, Mindestgruppengröße und E-Mail:** `site.config.json`. Der Startpreis ist 30 EUR pro Foto-Porträt, Live-Termine ab 10 Personen mit individuellem Gruppenangebot. Anschließend neu bauen.
- **Texte:** `content.json` (EN/DE), `content-asian.json` (ZH/JA).
- **Kampagnentexte und Motivauswahl:** `campaign.json` (alle fünf Sprachen).
- **Gestaltung:** `style.css`; **Kampagnenlayout:** `scripts/campaign.py`; **Anfrage/Video-Verhalten:** `app.js`.
- **Domain:** `baseUrl` in `site.config.json` anpassen oder beim Bauen `SITE_URL=https://example.com` setzen. Eine neue Domain muss separat registriert und beim Hoster verbunden werden. Es wurde keine Domain gekauft. Empfehlung als Marke: `wuerzburgportraits.de` oder `portraits.phil-splash.de`; Verfügbarkeit nicht geprüft.

## Veröffentlichung

GitHub Pages veröffentlicht den erzeugten Ordner `docs/` bei jedem Push auf `main`. Nach einer Text- oder Preisänderung zuerst lokal bauen und prüfen, danach die aktualisierten Quelldateien und `docs/` gemeinsam committen und pushen. In GitHub unter Settings → Pages ist `main` / `docs` als Quelle ausgewählt.

Vercel ist als Alternative vorbereitet: Repository importieren, `vercel.json` wird erkannt. Bei einem Wechsel `baseUrl`, Anbieterangaben zum Hosting in allen Sprachen und ggf. Domain aktualisieren. Kein Backend und keine Geheimnisse erforderlich.

## Auffindbarkeit

Eigene Sprach-URLs, vollständiges statisches HTML, gegenseitige hreflang-Verweise, selbstreferenzierende Canonicals, Sitemap, Social-Metadaten und strukturierte Daten (Person, Services, Preis, FAQ). `facts.json` und `llms.txt` ergänzen die öffentlich lesbaren Informationen; sie sind kein Rankingversprechen.

Der Name **Würzburg Moments** stellt das Reiseziel in den Vordergrund. Der bestehende GitHub-Pages-Pfad wird erhalten; es wurde keine neue Domain registriert. Seitentitel, Beschreibungen, WebSite-Daten und Agenteninformationen verwenden die neue Marke. Der Betreiber wird klar als Phil Splash benannt; es besteht keine Darstellung als offizielle Tourist-Information.

Die `robots.txt` ist für einen späteren Betrieb auf einer eigenen Domain vorbereitet. Bei GitHub-Projektseiten unter `/wuerzburg-portraits/` gilt die robots.txt der Host-Domain, nicht die Datei im Projekt-Unterordner. Inhalte werden nicht mit `noindex` blockiert.

Nach der Veröffentlichung: Von der bestehenden Künstlerwebsite auf die Sprachseiten verlinken. Eigene Domain in Google Search Console und Bing Webmaster Tools verifizieren und Sitemap einreichen. Das setzt Zugriff auf diese Konten bzw. DNS voraus und erfolgt nicht automatisch durch dieses Projekt. Für Festlandchina bietet die Seite lokale Bilder, Systemschriften und eine direkte E-Mail-Anfrage; YouTube bleibt optional. Erreichbarkeit aus Festlandchina wurde nicht vor Ort geprüft. Muttersprachliche Endredaktion wird für die Übersetzungen empfohlen.

## Besucherfunktionen

Die Buttons wählen das passende Angebot vor. Die Maske bereitet eine strukturierte englische E-Mail inklusive bevorzugter Korrespondenzsprache vor. Keine automatische Zusendung, keine Foto-Uploads und keine serverseitige Speicherung. Kopierfunktion und sichtbarer Text als Alternative zum E-Mail-Programm. Fotos werden nach Vereinbarung als E-Mail-Anhang geschickt.

Die Motivauswahl bietet City Color, City Ink und Original. Die aktuellen Stadtmotive zeigen eine einzige graue Markerlinien-Ansicht von Brücke und Festung als schmalen Streifen unten. Das Porträt bleibt das Hauptmotiv. Die früheren Collagen bleiben archiviert. Das gewählte Motiv erscheint in der E-Mail-Anfrage. City Color und City Ink sind als KI-Gestaltungskonzepte gekennzeichnet; fertige Hintergründe und Mehrarbeit werden vor einer Bestellung vereinbart.

YouTube lädt erst nach expliziter Zustimmung im Video-Dialog. Beim Schließen wird die Verbindung beendet; die Zustimmung wird nicht gespeichert. Keine Analysewerkzeuge oder externen Fonts.

## Quellen und Bildrechte

- Künstlerbiografie und Anbieteranschrift: https://www.phil-splash.de/ und https://www.phil-splash.de/contactimpressum/
- Würzburg-Bezug: https://zugabedigital.wuerzburg.de/portraits-gegen-rechts-in-der-langen-kulturspeichernacht/
- Originalporträts: vom Nutzer bereitgestellte eigene Galerie https://phil-splash.imgbb.com/albums (Vietnam 2026, VR Bank Würzburg, ServiceNow).
- Live-Bild und erster Film: https://www.youtube.com/watch?v=4OF5U2tFSXY
- Zweiter Film/Vorschaubild: https://www.youtube.com/watch?v=YGdoD-1dvJ4
- Aktuelle Bildwelt: referenzgestützt mit dem eingebauten Bildgenerator erzeugte Motive. Die vier aktuellen Erlebnisszenen (`assets/experience-*-v3.webp`) zeigen iPad und Apple Pencil; die zwei aktuellen Porträtkonzepte (`assets/portrait-city-*-v3.webp`) eine schmale graue Stadtlinie. Der Header verwendet weiterhin die geografisch korrigierte Stadtansicht v2. Die drei ursprünglichen reinen KI-Sehenswürdigkeitenbilder sind wieder im Reiseabschnitt eingebunden. Reale Ortsansichten geben Silhouetten und Perspektiven vor; Phil ist anhand eigener Künstlerbilder dargestellt. Kleine runde AI-Overlays verweisen auf die Bildhinweise. Die Galerie zeigt mögliche Buchungsszenen, keine dokumentierten Veranstaltungen. Prompts: `CREATIVE_NOTES.md`. Ortsreferenzen, Bearbeitungen und Lizenzen: `image-references.json`; auch im Bildernachweis jeder Sprachseite genannt. Die auf DXR-Ansichten beruhenden Bilddateien werden unter CC BY-SA 3.0 veröffentlicht. Das gilt nicht pauschal für Website oder unveränderte Originalporträts.
- Die vorherigen fremden Stadtfotografien wurden aus dem aktuellen Webauftritt entfernt. Ihre früheren Quellen und Lizenzangaben bleiben zur Dokumentation unter `archive/previous-photo-credits.json` erhalten. Dies ist kein aktuelles Bilderverzeichnis der Website.
- Frühere Bildkonzepte (erhalten, derzeit nicht eingesetzt): `assets/phil-mainbridge-engraving.webp`, `assets/portrait-city-color.webp`, `assets/portrait-city-ink.webp`. Mit dem eingebauten Bildgenerator entwickelt; auf der Seite klar als Illustration bzw. Gestaltungsidee gekennzeichnet. Keine historischen Nachweise, dokumentierten Termine oder zugesicherten fertigen Produktproben. Referenzen und vollständige Prompts: `CREATIVE_NOTES.md`.
- Lokal eingebundene Schriften: Barlow Condensed und Space Grotesk, Lizenztexte in `assets/fonts/`.
- Tourismus: https://www.wuerzburg.de/en/

Impressum und Datenschutzhinweise verwenden vorhandene öffentliche Anbieterangaben und beschreiben die implementierte Funktion. Die USt-IdNr. wurde von der veröffentlichten Vercel-Referenzseite übernommen; Herkunft und Anpassungen sind in `LEGAL_NOTES.md` dokumentiert. Anbieterangaben und Preisangaben sind bei Änderungen aktuell zu halten. Nicht bestätigte Leistungsversprechen (feste Dauer, Liefergarantie, regelmäßiger Standplatz, enthaltene Live-Übersetzung) werden nicht gemacht.

Inhalte und Originalkunstwerke © Phil Splash. Ausgenommen sind ausdrücklich lizenzierte Referenzen und daraus abgeleitete Bilddateien gemäß `image-references.json`. Alle früheren Motive bleiben unverändert erhalten; Übersicht: `archive/visual-history.md`.

## Touristische Fakten

Die Texte richten sich ausdrücklich an Reisende aus China und Japan. Fakten zu UNESCO-Welterbe, Mainbrücke, Altstadt und Romantischer Straße sind von den KI-Bildwelten getrennt. Quellen:
- https://whc.unesco.org/en/list/169/
- https://www.wuerzburg.de/tourismus/wuerzburg-entdecken/sehenswuerdigkeiten/alte-mainbruecke/index.html
- https://www.wuerzburg.de/tourismus/wuerzburg-entdecken/sehenswuerdigkeiten/festung-marienberg/index.html
- https://romantischestrasse.de/en/wuerzburg/

Eintritte und Stadtführungen sind keine eingeschlossenen Produkte der Seite. Öffnungszeiten und Zugänglichkeit werden an die offiziellen Stellen verwiesen.

## iPad-Überarbeitung

Die bisherigen Papier-Szenen und Collagen sind zusätzlich in `archive/2026-10-27-before-ipad-and-line-panorama/` gesichert, ohne die alten Dateien zu löschen. Neue Bilder haben eigene v3-Dateinamen. Impressum weiterhin unten als aufklappbarer Bereich, mit vollständigen ergänzenden Texten in allen fünf Sprachen.

## Neue Souvenir-Porträts · 28. Oktober 2026

Vier aktuelle KI-Layoutstudien nach Phils eigenem Original IMG_0352.JPG sind als optimierte lokale WebP-Dateien unter `assets/souvenir-*.webp` eingebunden. Die beiden Männerfassungen enthalten keine roten Kragenmarkierungen. City Color und City Ink verwenden die ostasiatischen Beispiele mit durchgehender grauer Stadtansicht und überlagernden Porträtlinien; die frühere kleine Stadtlinie wird in dieser Auswahl nicht mehr angezeigt. Eine offene Galerie zeigt alle vier Motive in vier Desktop- bzw. zwei Mobilspalten, mit Bildlinks, AI-Kennzeichnung und direkter Fotoanfrage. Texte in allen fünf Sprachen in `campaign.json`. Die Originalkunst-Galerie bleibt separat erhalten. Die Bilder sind KI-Gestaltungsideen, keine von Phil persönlich gezeichneten Kundenporträts.

## Vereinfachtes Angebot · 29. Oktober 2026

Eine dunkle Produktsektion zeigt ein großes Würzburg-Porträt und vier anklickbare Vorschaubilder. Keine Stil- oder Produktauswahl zwischen City Color, City Ink und Original mehr, auch nicht im Anfrageformular. Einzelporträts nach Foto kosten 30 EUR; Live-Gruppen ab 10 Personen erhalten ein individuelles Angebot. Die doppelte Souvenir-Galerie und die separate Originalgalerie entfallen. Frühere Dateien bleiben erhalten.

Nur das Vietnam-Video wird groß dargestellt. Zwei aktualisierte KI-Erlebnisszenen zeigen die entwickelten Würzburg-Porträts auf dem iPad (`experience-handover-v5`, `experience-market-v5`). Einheitliche Zweispaltenraster für Bild/Text, gestapelte Abschnittsüberschriften, helle Flächen im Wechsel mit dunklem Produktabschnitt und einer Lime-Anfragefläche. Der Header wächst mit seinem Inhalt statt Buttons abzuschneiden. Geprüft: 2560px-Header ohne Überlauf, 390px-Handyansicht, Vorschaubildwechsel, Fotoanfrage mit Minimum 1, Gruppenanfrage mit Minimum 10, fünf Sprachrouten.
