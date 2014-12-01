aquaf
=====

Origineel ontwikkeld door Riba.
Riba's aquazone - Aquaforum uploadprogramma: http://aquazone.leeuwen.nu/blog/uploadprogramma

verder ontwikkeld door Mark labordus - kellemes (bordumar@gmail.com)

* Code home page: https://github.com/labordus/aquaf
* Issue tracker: https://github.com/labordus/aquaf/issues

# Building

aquaf maakt gebruik van Python 2.7, wxwidgets, Pillow 2.5.1-26.1
(python-wxWidgets-3_0) 3.0.1.1-8.1


[Todo](TODO.md)


# Info

Bij deze een nieuwe versie van Riba's uploadtooltje.. 0.84-Alpha.
De veranderingen 'under the hood' zijn aanzienlijk.. vandaar dat ik er voor kies
om het programma naast de (eventueel aanwezige) versie van Riba te installeren.
Die versie wordt dus niet overschreven.


# Wat is er veranderd?

* T'is nu cross-platform, werkt op posix-besturingssystemen en Windows.
Windows 95/98/ME wordt niet meer ondersteund!
Heb het kunnen testen op..
Linux(64bit)/WindowsXP(32bit)/WindowsVista(64bit)/Windows7(32bit)/Windows8.1(32bit)
* Je kunt nu meerdere plaatjes klaarzetten om in 1 ruk te kunnen uploaden.
Wel is het zo dat de geselecteerde dimensie van de te uploaden plaatjes
geldt voor alle klaargezette plaatjes.. je kunt dat niet per individueel
plaatje aangeven.. (staat op de todo lijst.)
* Kwaliteit van de plaatjes wordt zo maximaal mogelijk gehouden voor upload.
* Gebruikersnaam hoeft niet telkens opnieuw te worden ingevoerd.


# Verdere op/aanmerkingen.
* Bij sommige gebruikers werkte de archiefpagina schijnbaar niet..
vermoedelijk geldt dit alleen voor gebruikers wiens standaard browser
Chrome/Chromium of Opera is. Internet Explorer en Firefox werken hier prima.
Ik ken de oorzaak maar heb momenteel geen makkelijke/werkbare oplossing.
Wat ik momenteel doe is 'vanuit code' checken of Firefox aanwezig is, zo ja.. dan
gebruikt de applicatie die, zo niet dan wordt de standaard browser gebruikt,
idealiter is dat dan Internet Explorer.
Dus.. gebruikers die problemen hebben met de archiefpagina (geen plaatjes zien)
hoeven alleen maar Firefox te installeren, dan is het probleem opgelost.

# Bij problemen.
Laat het me weten.. maar liefst wel met zoveel mogelijk informatie over wat
er mis gaat.. hoe meer informatie ik heb hoe makkelijker ik het kan oplossen.
En ook welk besturingsysteem je gebruikt, liefst ook architectuur (32bit/64bit).

# Instructies voor installatie.
Voor diegenen die de 'oude' versie van Riba in gebruik hebben..
Ik maak gebruik van hetzelfde databestand als waar Riba's versie gebruik
van maakt.. daarvoor dient dat dan wel gekopieerd te worden
naar de nieuwe installatie-map.
Locatie van databestand zal waarschijnlijk zijn:
C:\Program Files\aquaforumuploader\images.json
En die moet hier naartoe (tenzij je een andere locatie hebt gekozen
tijdens de setup):
C:\Program Files\aquaf\ 

Nieuwe gebruikers kunnen gewoon de applicatie opstarten.

# Instructies voor gebruik.. (Hou ik heel kort)
* Voer gebruikersnaam in.
* Selecteer in de lijst links op het scherm een plaatje die je uploaden wilt,
klik op de knop "toevoegen" zodat die wordt toegevoegd aan de lijst aan de rechter kant.
Ga zo door totdat je alle plaatjes hebt toegevoegd die je wilt uploaden.
* Klik op knop "upload naar aquaforum" en wacht op het volgende venster alwaar
je de URL's kunt kopieren om in je forumbericht te plakken.


Deze versie beschouw ik als Alpha..
Download hier het Windows installatiepakket.
......


Als er Linux-gebruikers zijn die hulp willen bij de installatie, laat het me weten.
Als er Apple-gebruikers zijn, die kan ik niet helpen, die hebben pech ;)
