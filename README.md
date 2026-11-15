# kleinwild.nl

De website van Klein Wild: buitenprogramma's voor BSO's in de Gooi en Vechtstreek.

**Status: conceptversie.** De teksten zijn concept, prijzen en testimonials staan er als `[placeholder]`, en de foto's zijn Unsplash-placeholders tot er eigen beeld is. De formulieren versturen nog niets. Zoekmachines indexeren de site niet zolang de regel `<meta name="robots" content="noindex">` in de pagina's staat.

## Hoe de site in elkaar zit

Gewone HTML en CSS, zonder buildstap. Wat je in de repo ziet, staat zo online.

| Bestand | Pagina |
|---|---|
| `index.html` | Home |
| `bosmiddag.html` | De bosmiddag |
| `seizoensdoos.html` | De seizoensdoos |
| `speldozen.html` | Speldozen en draaiboeken, voor de landelijke markt (alleen in de voet) |
| `programmas.html` | Programma's |
| `kinderfeestje.html` | Boskinderfeestje en feestbox, voor ouders (alleen in de voet) |
| `veiligheid.html` | Veiligheid |
| `over.html` | Over Timon |
| `contact.html` | Kennismaken |
| `nieuwsbrief.html` | Nieuwsbrief en gratis draaiboek |
| `privacy.html` | Privacyverklaring (placeholder) |

- `css/site.css` bevat wat alle pagina's delen: het menu op de telefoon, focusstijlen en de voet. De stijl per pagina staat in een `<style>`-blok bovenin die pagina.
- `img/` bevat de foto's (verkleind voor het web) en de logo's.
- Lettertypen komen van Google Fonts: Fraunces, Libre Franklin en Caveat.

De pagina's zijn omgezet uit het websiteontwerp in Claude Design (15 november 2026). De teksten volgen `02-website/content/` in de lokale Klein Wild-map.

## Hosting

GitHub Pages, vanaf de branch `main`, op het domein `https://kleinwild.nl` (zie het bestand `CNAME`). Elke push staat binnen een minuut of twee online.

## Vindbaarheid voor Google en AI-assistenten

| Bestand of onderdeel | Waarvoor |
|---|---|
| `robots.txt` | Laat alle zoekmachines en AI-crawlers toe en wijst naar de sitemap |
| `sitemap.xml` | Lijst van alle pagina's voor zoekmachines |
| `llms.txt` | Samenvatting van Klein Wild in gewone taal, voor AI-assistenten |
| JSON-LD in elke `<head>` | Gestructureerde gegevens (schema.org): organisatie, diensten, programma's, kruimelpad |
| `tools/seo.py` | Zet titels, beschrijvingen, Open Graph en JSON-LD in alle pagina's. Draai `python3 tools/seo.py` na elke inhoudelijke wijziging |
| Open Graph-tags in elke `<head>` | Titel, tekst en afbeelding (`img/og-image.jpg`) bij het delen van een link |

Alle absolute adressen gaan uit van `https://kleinwild.nl/`.

Houd deze bestanden gelijk met de pagina's. Verandert er een feit op de site (een prijs, een leeftijd, een programma), pas het dan ook aan in `llms.txt` en in `tools/seo.py`, en draai dat script. Een nieuwe pagina krijgt een regel in `tools/seo.py`, `sitemap.xml` en `llms.txt`, en een link in het voetmenu van alle pagina's. Zet nooit iets in de gestructureerde gegevens dat niet zichtbaar op de pagina staat, zoals beoordelingen die er niet zijn.

## Voor livegang nog te doen

- Teksten goedkeuren en de placeholders invullen
- Formulieren koppelen aan een nieuwsbrief- en formuliertool met verwerkersovereenkomst
- Privacyverklaring laten schrijven
- Eigen foto's in plaats van de Unsplash-placeholders, ook `img/og-image.jpg` (1200 bij 630 pixels)
- De `noindex`-regel uit alle pagina's halen
- Prijzen, telefoonnummer en KvK-nummer ook toevoegen aan `tools/seo.py` (`telephone`, `offers`) en aan `llms.txt`; de regel over de conceptversie uit `llms.txt` halen
- `lastmod` in `sitemap.xml` op de livegangdatum zetten
- Site aanmelden bij Google Search Console en Bing Webmaster Tools, en daar de sitemap indienen
- Een Google Bedrijfsprofiel aanmaken als servicebedrijf zonder bezoekadres, met werkgebied Gooi en Vechtstreek. Naam, telefoon en adres moeten letterlijk gelijk zijn aan de site.
