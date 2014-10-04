aquaf
=====

Origineel ontwikkeld door Riba.
Riba's aquazone - Aquaforum uploadprogramma: http://aquazone.leeuwen.nu/blog/uploadprogramma

verder ontwikkeld door Mark labordus - kellemes (bordumar@gmail.com)

* Code home page: https://github.com/labordus/aquaf
* Issue tracker: https://github.com/labordus/aquaf/issues

# Building

aquaf maakt gebruik van Python 2.7, wxwidgets, PIL
(python-wxWidgets-3_0) 3.0.1.1-8.1

# gedaan tot nu toe
- Cross-platform.. werkt prima op Linux, moest daarvoor de gui van de logic scheiden. (nog niet kunnen testen op Windows)
- Gui gedeelte wordt nu geregeld door wxformbuilder
- Meerdere foto's tegelijk kunnen uploaden zit er bijna in.
- Wat kleine aanpassinkjes om een eventuele overstap naar Python 3+ mogelijk te maken.
- 

# Opmerkingen, uitzoekpunten en todo's.

- Zinnig om naar Python 3+ over te stappen? Wat zijn de gevolgen voor de install?
- De wxpython (3.0.1.1-8.1) versie die ik gebruik werkt niet meer met Windows 9*
- jpeg's worden met quality=60 opgeslagen.. dat verminderd de kwaliteit drastisch.
- taborder
- default actie voor enter op het mainform?
- resizeFile() is te traag, moet sneller kunnen
- Op mijn systeem (GTK) is resizen van form etc.. lelijk, is dat ook op Windhoos?
- Alles goed afschermen met try/finaly/except etc.. 
- Voorbeeld: per foto doen? Of gewoon een totaal overzicht van de gekozen foto's in de geselecteerde scale?
- Krijg warnings.. Unused import: BmpImagePlugin (en al de anderen).. maar zonder werkt het ook niet, want?
- gebruikersnaam-invoer eisen? Het nut hiervan is alleen voor het genereren van een bestandsnaam?
- Hoe wordt je account eigenlijk gekoppeld aan de foto's? Worden ze wel gekoppeld?

-- data --
- Ik zou wat gegevens willen opslaan.. zoals ingevoerde username of laatst gekozen directory etc.. Hoe?
- Archief naar de applicatie verhuizen? HTML/CSS-file dumpen dus.. Dat hele JSON-gebeuren snap ik niet..
- Archief zou niet voor iedereen werken blijkbaar.
- Data (momenteel JSON) op de 1 of andere manier wat veiliger stellen tegen overschrijven etc..

-- setup --
- Wat moet ik allemaal meeleveren met Inno?
- Precies welke python/wxwidgets/wxpython (etc..) moet ik eisen?
- Hoe werkt dat allemaal.. geen idee wat er standaard op de verschillende Window's versies aanwezig is.. en hoe ik kan garanderen dat er aan de eisen wordt voldaan.

