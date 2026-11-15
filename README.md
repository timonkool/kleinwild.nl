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
| `programmas.html` | Programma's |
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

GitHub Pages, vanaf de branch `main`. Elke push staat binnen een minuut of twee online.

## Vindbaarheid voor Google en AI-assistenten

| Bestand of onderdeel | Waarvoor |
|---|---|
| `robots.txt` | Laat alle zoekmachines en AI-crawlers toe en wijst naar de sitemap |
| `sitemap.xml` | Lijst van alle pagina's voor zoekmachines |
| `llms.txt` | Samenvatting van Klein Wild in gewone taal, voor AI-assistenten |
| JSON-LD in elke `<head>` | Gestructureerde gegevens (schema.org): organisatie, diensten, programma's, kruimelpad |
| Open Graph-tags in elke `<head>` | Titel, tekst en afbeelding (`img/og-image.jpg`) bij het delen van een link |

Alle absolute adressen gaan uit van `https://kleinwild.nl/`. `robots.txt`, `sitemap.xml` en `llms.txt` werken pas als ze in de root van het domein staan. Zolang de site op `timonkool.nl/kleinwild.nl/` draait, lezen crawlers ze niet.

Houd deze bestanden gelijk met de pagina's. Verandert er een feit op de site (een prijs, een leeftijd, een programma), pas het dan ook aan in `llms.txt` en in de JSON-LD van die pagina. Zet nooit iets in de gestructureerde gegevens dat niet zichtbaar op de pagina staat, zoals beoordelingen die er niet zijn.

## Voor livegang nog te doen

- Teksten goedkeuren en de placeholders invullen
- Formulieren koppelen aan een nieuwsbrief- en formuliertool met verwerkersovereenkomst
- Privacyverklaring laten schrijven
- Eigen foto's in plaats van de Unsplash-placeholders, ook `img/og-image.jpg` (1200 bij 630 pixels)
- Domein `kleinwild.nl` koppelen: een bestand `CNAME` met `kleinwild.nl` in de repo, en de DNS-records bij de registrar
- De `noindex`-regel uit alle pagina's halen
- Prijzen, e-mailadres, telefoonnummer en KvK-nummer ook toevoegen aan de JSON-LD (`email`, `telephone`, `offers`) en aan `llms.txt`; de regel over de conceptversie uit `llms.txt` halen
- `lastmod` in `sitemap.xml` op de livegangdatum zetten
- Site aanmelden bij Google Search Console en Bing Webmaster Tools, en daar de sitemap indienen
- Een Google Bedrijfsprofiel aanmaken als servicebedrijf zonder bezoekadres, met werkgebied Gooi en Vechtstreek. Naam, telefoon en adres moeten letterlijk gelijk zijn aan de site.
