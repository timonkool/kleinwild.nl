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

## Voor livegang nog te doen

- Teksten goedkeuren en de placeholders invullen
- Formulieren koppelen aan een nieuwsbrief- en formuliertool met verwerkersovereenkomst
- Privacyverklaring laten schrijven
- Eigen foto's in plaats van de Unsplash-placeholders
- De `noindex`-regel uit alle pagina's halen
