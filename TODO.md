- De wxpython (3.0.1.1-8.1) versie die ik gebruik werkt niet meer met Windows 9*
- jpeg's worden met quality=60 opgeslagen.. dat verminderd de kwaliteit drastisch.
- taborder
- resizeFile() is te traag, moet sneller kunnen
- Voorbeeld: per foto doen? Of gewoon een totaal overzicht van de gekozen foto's in de geselecteerde scale? -> m.b.v. test.jpg
- gebruikersnaam-invoer eisen? Het nut hiervan is alleen voor het genereren van een bestandsnaam? -> FIXED.. invoer nu vereist
- Hoe wordt je account eigenlijk gekoppeld aan de foto's? Worden ze wel gekoppeld?
- 1 instance
- bij laden test.jpg.. moet ik eerst ook het pad zoeken? (OnbtnVoorbeeldClick)
########### demo.py
                  'GetUserConfigDir',
                  'GetDataDir',
                  'GetLocalDataDir',
                  'GetUserDataDir',
                  'GetUserLocalDataDir',
                  'GetDocumentsDir',
                  'GetAppDocumentsDir',
                  'GetPluginsDir',
                  'GetInstallPrefix',
                  'GetResourcesDir',
                  'GetTempDir',
                  'GetExecutablePath',
############
- voorbeelddialoog midden in mainform -> aanroepen vanuit mainform?
- voorbeeld dynamisch dimensie laten zien in de tekst boven de image -> FIXED
- Preview-bitmap moet meteen test.jpg zijn, maar dan moet ie eerst geresized.
- Bug! Er kunnen ook directories worden toegevoegd! -> FIXED

-- data --
- Ik zou wat gegevens willen opslaan.. zoals ingevoerde username of laatst gekozen directory etc.. Hoe?
- Archief zou niet voor iedereen werken blijkbaar.
