"""Zet titel, metabeschrijving, canonical, Open Graph en schema.org (JSON-LD) in de <head> van elke pagina.

Gebruik, vanuit de map van de repo:  python3 tools/seo.py

Het script is herhaalbaar: het haalt het bestaande blok weg en zet het opnieuw.
Verandert er een feit op de site (leeftijd, prijs, programma, contactgegeven),
pas het dan hier aan en draai het script opnieuw. Zet in de JSON-LD alleen wat
ook zichtbaar op de pagina staat. Een nieuwe pagina krijgt hieronder een eigen
regel in PAGES, en een regel in sitemap.xml en llms.txt.
"""
import json, re, html

BASE = "https://kleinwild.nl/"
ORG_ID = BASE + "#organisatie"
SITE_ID = BASE + "#website"
PERSON_ID = BASE + "over.html#timon"
OG_IMAGE = BASE + "img/og-image.jpg"

ORG = {
    "@type": "Organization",
    "@id": ORG_ID,
    "name": "Klein Wild",
    "url": BASE,
    "logo": BASE + "img/logo-fox.png",
    "slogan": "Buiten leren. Samen groeien.",
    "description": "Buitenprogramma voor BSO's in de Gooi en Vechtstreek, op basis van scouting en survival: begeleide bosmiddagen en seizoensdozen. Landelijk losse speldozen en draaiboeken, en boskinderfeestjes met feestboxen.",
    "email": "info@kleinwild.nl",
    "founder": {"@id": PERSON_ID},
    "address": {"@type": "PostalAddress", "addressLocality": "Kortenhoef", "addressCountry": "NL"},
    "areaServed": {"@type": "Place", "name": "Gooi en Vechtstreek"},
    "knowsAbout": ["buitenspelen", "scouting", "survival", "risicovol spelen", "buitenschoolse opvang"],
}

AUDIENCE = {"@type": "Audience", "audienceType": "BSO's (buitenschoolse opvang) en pedagogisch medewerkers"}

PROGRAMMAS = [
    ("Expeditie Wildernis", "Vaardigheden en competentie. Het vlaggenschip.", "6-12", "Hele jaar"),
    ("De Vuurmeesters", "Risicocompetentie en focus, rond vuur.", "9-12", "Herfst en winter"),
    ("Het Belegerde Kasteel", "Strategie en sportiviteit.", "6-12", "Hele jaar"),
    ("De Woudlopers", "Waarnemen en impulscontrole.", "6-12", "Lente tot herfst"),
    ("Rangers van het Reservaat", "Natuurkennis en zorg.", "6-12", "Lente en zomer"),
    ("De Grote Oversteek", "Samenwerken en reflectie.", "9-12", "Hele jaar"),
    ("Het Smokkelaarspad", "Strategisch denken.", "10-12", "Hele jaar"),
    ("De Nachtwacht", "Emotieregulatie en durf. Korter, omdat spanning energie kost.", "9-12", "Oktober tot maart"),
    ("Bouwmeesters van het Bos", "Techniek en eigenaarschap. Het bouwen is het hoofdblok.", "6-12", "Hele jaar"),
    ("Het Verdwenen Bosgeheim", "Logica en verhaal. Werkt ook bij slecht weer.", "6-12", "Hele jaar"),
]


def crumbs(name, path):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": name, "item": BASE + path},
        ],
    }


def webpage(path, name, typ="WebPage", extra=None):
    d = {
        "@type": typ,
        "@id": BASE + path + "#pagina",
        "url": BASE + path,
        "name": name,
        "inLanguage": "nl-NL",
        "isPartOf": {"@id": SITE_ID},
        "publisher": {"@id": ORG_ID},
    }
    if extra:
        d.update(extra)
    return d


PAGES = {
    "index.html": {
        "path": "",
        "title": "Klein Wild, buitenprogramma voor BSO's in de Gooi en Vechtstreek",
        "desc": "Bosmiddagen en seizoensdozen voor BSO's in de Gooi en Vechtstreek, op basis van scouting en survival. Met draaiboek, materiaal en een plan B.",
        "graph": lambda: [
            {"@type": "WebSite", "@id": SITE_ID, "url": BASE, "name": "Klein Wild", "inLanguage": "nl-NL", "publisher": {"@id": ORG_ID}},
            ORG,
            webpage("", "Klein Wild, buitenprogramma voor BSO's", extra={"about": {"@id": ORG_ID}}),
        ],
    },
    "bosmiddag.html": {
        "path": "bosmiddag.html",
        "title": "Bosmiddag voor BSO's in de Gooi en Vechtstreek, Klein Wild",
        "desc": "Een begeleide middag van drie uur in een bos bij jou in de buurt, voor BSO-kinderen van 6 tot 12. Gedraaid door gecertificeerde scoutingleiders, met draaiboek en plan B.",
        "graph": lambda: [
            {
                "@type": "Service",
                "@id": BASE + "bosmiddag.html#dienst",
                "name": "De begeleide bosmiddag",
                "serviceType": "Begeleid buitenprogramma voor de BSO",
                "description": "Een programma van drie uur in een bos bij de BSO in de buurt, voor kinderen van 6 tot 12 jaar, het hele jaar door. Gecertificeerde scoutingleiders van een lokale scoutinggroep draaien de middag. Klein Wild regelt programma, draaiboek, leiding, materiaal, veiligheidsprotocol en een plan B voor slecht weer. Medewerkers van de BSO lopen mee en houden het draaiboek.",
                "provider": {"@id": ORG_ID},
                "areaServed": {"@type": "Place", "name": "Gooi en Vechtstreek"},
                "audience": AUDIENCE,
                "url": BASE + "bosmiddag.html",
            },
            webpage("bosmiddag.html", "De bosmiddag", extra={"mainEntity": {"@id": BASE + "bosmiddag.html#dienst"}}),
            crumbs("De bosmiddag", "bosmiddag.html"),
        ],
    },
    "seizoensdoos.html": {
        "path": "seizoensdoos.html",
        "title": "Seizoensdoos met buitenactiviteiten voor de BSO, Klein Wild",
        "desc": "Eén doos per BSO-vestiging per kwartaal, met zes tot acht uitgewerkte buitenactiviteiten, materiaal, instructiekaarten en veiligheidsprotocol.",
        "graph": lambda: [
            {
                "@type": "Service",
                "@id": BASE + "seizoensdoos.html#dienst",
                "name": "De seizoensdoos",
                "serviceType": "Seizoensabonnement met buitenactiviteiten voor de BSO",
                "description": "Eén doos per vestiging per kwartaal met zes tot acht volledig uitgewerkte buitenactiviteiten, ongeveer één per twee weken. In de doos zitten het materiaal (vooral verbruiksmateriaal), een instructiekaart per activiteit en een veiligheidsprotocol. Groepen op dezelfde locatie delen de doos; een extra groepsset is los te bestellen.",
                "provider": {"@id": ORG_ID},
                "audience": AUDIENCE,
                "url": BASE + "seizoensdoos.html",
            },
            webpage("seizoensdoos.html", "De seizoensdoos", extra={"mainEntity": {"@id": BASE + "seizoensdoos.html#dienst"}}),
            crumbs("De seizoensdoos", "seizoensdoos.html"),
        ],
    },
    "programmas.html": {
        "path": "programmas.html",
        "title": "Tien buitenprogramma's voor kinderen van 6 tot 12, Klein Wild",
        "desc": "Tien uitgewerkte buitenprogramma's voor BSO-kinderen van 6 tot 12, met leeftijd, seizoen en risiconiveau per programma.",
        "graph": lambda: [
            webpage("programmas.html", "Programma's", typ="CollectionPage", extra={"mainEntity": {"@id": BASE + "programmas.html#lijst"}}),
            {
                "@type": "ItemList",
                "@id": BASE + "programmas.html#lijst",
                "name": "De tien programma's van Klein Wild",
                "numberOfItems": len(PROGRAMMAS),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "item": {
                            "@type": "CreativeWork",
                            "name": n,
                            "description": d + " Seizoen: " + s.lower() + ".",
                            "typicalAgeRange": a,
                            "inLanguage": "nl-NL",
                            "author": {"@id": ORG_ID},
                        },
                    }
                    for i, (n, d, a, s) in enumerate(PROGRAMMAS)
                ],
            },
            crumbs("Programma's", "programmas.html"),
        ],
    },
    "speldozen.html": {
        "path": "speldozen.html",
        "title": "Speldozen en draaiboeken voor buitenspel op de BSO, Klein Wild",
        "desc": "Een kant-en-klare buitenactiviteit voor je BSO, waar je ook zit in Nederland. Als speldoos met het materiaal erbij, of als digitaal draaiboek.",
        "graph": lambda: [
            {
                "@type": "Service",
                "@id": BASE + "speldozen.html#dienst",
                "name": "Losse speldozen en digitale draaiboeken",
                "serviceType": "Kant-en-klare buitenactiviteit voor de BSO",
                "description": "Eén buitenactiviteit om zelf te draaien, als speldoos met draaiboek en materiaal of als digitaal draaiboek. Elk draaiboek bevat een tijdlijn, een materiaallijst, een veiligheidsprotocol en een plan B. De speldoos wordt in heel Nederland bezorgd.",
                "provider": {"@id": ORG_ID},
                "areaServed": {"@type": "Country", "name": "Nederland"},
                "audience": AUDIENCE,
                "url": BASE + "speldozen.html",
            },
            webpage("speldozen.html", "Speldozen en draaiboeken", extra={"mainEntity": {"@id": BASE + "speldozen.html#dienst"}}),
            crumbs("Speldozen", "speldozen.html"),
        ],
    },
    "kinderfeestje.html": {
        "path": "kinderfeestje.html",
        "title": "Boskinderfeestje in de Gooi en Vechtstreek, Klein Wild",
        "desc": "Een verjaardagsfeestje in het bos voor kinderen van 6 tot 12, begeleid en met al het materiaal. Doe je het liever zelf, dan is er de feestbox.",
        "graph": lambda: [
            {
                "@type": "Service",
                "@id": BASE + "kinderfeestje.html#dienst",
                "name": "Boskinderfeestje",
                "serviceType": "Kinderfeestje in het bos",
                "description": "Een begeleid verjaardagsfeestje in een bos in de Gooi en Vechtstreek voor kinderen van 6 tot 12 jaar, of een feestbox met draaiboek en materiaal om het feestje zelf te geven. De feestjes komen uit dezelfde programma's als de BSO-middagen, met een veiligheidsprotocol en een plan B voor slecht weer.",
                "provider": {"@id": ORG_ID},
                "areaServed": {"@type": "Place", "name": "Gooi en Vechtstreek"},
                "audience": {"@type": "PeopleAudience", "audienceType": "Ouders", "suggestedMinAge": 6, "suggestedMaxAge": 12},
                "url": BASE + "kinderfeestje.html",
            },
            webpage("kinderfeestje.html", "Boskinderfeestje", extra={"mainEntity": {"@id": BASE + "kinderfeestje.html#dienst"}}),
            crumbs("Kinderfeestje", "kinderfeestje.html"),
        ],
    },
    "veiligheid.html": {
        "path": "veiligheid.html",
        "title": None,
        "desc": None,
        "graph": lambda: [
            webpage("veiligheid.html", "Veiligheid en risicovol spelen", extra={"about": ["risicovol spelen", "veiligheid bij buitenspel"]}),
            crumbs("Veiligheid", "veiligheid.html"),
        ],
    },
    "over.html": {
        "path": "over.html",
        "title": None,
        "desc": None,
        "graph": lambda: [
            webpage("over.html", "Over Timon Kool", typ="AboutPage", extra={"mainEntity": {"@id": PERSON_ID}}),
            {
                "@type": "Person",
                "@id": PERSON_ID,
                "name": "Timon Kool",
                "jobTitle": "Oprichter van Klein Wild",
                "worksFor": {"@id": ORG_ID},
                "description": "Gaf jarenlang scoutingleiding en zette Klein Wild op om buitenprogramma voor BSO's te maken.",
            },
            crumbs("Over", "over.html"),
        ],
    },
    "contact.html": {
        "path": "contact.html",
        "title": "Kennismaken met Klein Wild, buitenprogramma voor de BSO",
        "desc": "Vraag een vrijblijvend kennismakingsgesprek aan over buitenprogramma op je BSO. Vertel iets over je vestiging, dan stel ik een programma voor dat past.",
        "graph": lambda: [
            webpage("contact.html", "Kennismaken", typ="ContactPage", extra={"about": {"@id": ORG_ID}}),
            crumbs("Kennismaken", "contact.html"),
        ],
    },
    "nieuwsbrief.html": {
        "path": "nieuwsbrief.html",
        "title": "Gratis draaiboek voor een buitenactiviteit op de BSO, Klein Wild",
        "desc": "Elke twee weken één uitgewerkte buitenactiviteit voor pedagogisch medewerkers op de BSO. Bij aanmelding krijg je meteen een gratis draaiboek.",
        "graph": lambda: [
            webpage("nieuwsbrief.html", "Gratis draaiboek en nieuwsbrief"),
            crumbs("Nieuwsbrief", "nieuwsbrief.html"),
        ],
    },
    "privacy.html": {
        "path": "privacy.html",
        "title": None,
        "desc": None,
        "graph": lambda: [
            webpage("privacy.html", "Privacyverklaring"),
            crumbs("Privacy", "privacy.html"),
        ],
    },
}


def esc(s):
    return html.escape(s, quote=True).replace("&#x27;", "'")


for fname, p in PAGES.items():
    s = open(fname, encoding="utf-8").read()
    # Bestaand blok weghalen, zodat het script herhaalbaar is
    s = re.sub(r'<link rel="canonical".*?</script>\n', "", s, count=1, flags=re.S)

    if p["title"]:
        s = re.sub(r"<title>.*?</title>", "<title>" + esc(p["title"]) + "</title>", s, count=1)
    if p["desc"]:
        s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + esc(p["desc"]) + '">', s, count=1)

    title = html.unescape(re.search(r"<title>(.*?)</title>", s).group(1))
    desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
    url = BASE + p["path"]

    nodes = p["graph"]()
    if ORG not in nodes:
        nodes.append(ORG)  # elke pagina draagt de bedrijfsgegevens zelf
    graph = {"@context": "https://schema.org", "@graph": nodes}
    ld = json.dumps(graph, ensure_ascii=False, indent=1)

    block = "\n".join([
        '<link rel="canonical" href="' + url + '">',
        '<meta property="og:type" content="website">',
        '<meta property="og:locale" content="nl_NL">',
        '<meta property="og:site_name" content="Klein Wild">',
        '<meta property="og:title" content="' + esc(title) + '">',
        '<meta property="og:description" content="' + esc(desc) + '">',
        '<meta property="og:url" content="' + url + '">',
        '<meta property="og:image" content="' + OG_IMAGE + '">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<script type="application/ld+json">',
        ld,
        "</script>",
    ])
    s = s.replace('<meta name="theme-color"', block + '\n<meta name="theme-color"', 1)

    open(fname, "w", encoding="utf-8").write(s)
    print("ok", fname, len(title), len(desc))
