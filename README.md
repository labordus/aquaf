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

# Opmerkingen, uitzoekpunten en todo's.

- De wxpython (3.0.1.1-8.1) versie die ik gebruik werkt niet meer met Windows 9*
- jpeg's worden met quality=60 opgeslagen.. dat verminderd de kwaliteit drastisch.
- taborder
- resizeFile() is te traag, moet sneller kunnen
- Voorbeeld: per foto doen? Of gewoon een totaal overzicht van de gekozen foto's in de geselecteerde scale?
- gebruikersnaam-invoer eisen? Het nut hiervan is alleen voor het genereren van een bestandsnaam?
- Hoe wordt je account eigenlijk gekoppeld aan de foto's? Worden ze wel gekoppeld?

-- data --
- Ik zou wat gegevens willen opslaan.. zoals ingevoerde username of laatst gekozen directory etc.. Hoe?
- Archief zou niet voor iedereen werken blijkbaar.

