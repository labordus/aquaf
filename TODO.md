# Versie 0.87
- [ ] Heel bericht kunnen schrijven vanuit gui + ingevoegde foto's.

# Versie 0.86
- [x] Foto's worden automatisch gedraaid? DSC_0001.JPG -> http://www.aquaforum.nl/gallery/upload/339568kellemes_0_85_download.jpg
      http://stackoverflow.com/questions/4228530/pil-thumbnail-is-rotating-my-image
      Dit ging om iets heel anders.. de browser laat de foto zien zonder rekening te houden met de
      eventueel aanwezige rotatie in de EXIF-data.. een lokale viewer veelal wel, vandaar de verwarring.
- [x] Kunnen draaien van een foto.. en uploaden.
- [x] Onvoorbeeldclick moet voorbeeld tonen van actieve foto in view (bitmapSelectedFile).
- [x] Fetch image van remote URL? Photobucket, Flickr, Picasa, http://postimage.org/ etc..
- [x] "filetype JPG heeft geen JPG-extensie" etc.. etc.. is dit eigenlijk nog nodig? Uitgeschakeld.
- [x] dimensie/rotatie remote image.
- [x] Druk UPLOAD -->> online afwezigheid foto afhandelen.
- [x] Druk UPLOAD -->> local afwezigheid foto afhandelen.
- [x] Na toevoegen online/local-image.. listfiles -> net toegevoegd item selecteren.
- [x] tempfiles wissen.. oa bij afsluiten.
- [x] ook GIF en ICO ondersteunen
- [x] online -> gif doet het niet.. http://www.gsmeets.be/Hengelsport/Vissen_op_blankvoorn/Afbeeldingen/blankvoorn.gif
- [x] foto niet gevonden.. http://www.visaquarium.nl/images/v/98/t1_320x240.jpg ..  response 301 Moved Permanently\
- [ ] Wat als preview = False? Online foto tijdelijk op preview = True .. of niet?
- [x] Bij preview = False -> indeling der componenten wat strakker. + alleen toevoegen/verwijderen?!
- [ ] listfiles editable maken -> dimensies + rotatie
- [x] Bij initialisatie app wat global variabelen zetten, zodat ik ze niet telkens uit de DB hoef te trekken.
- [ ] APP_VERSIE en USER_DIMENSIE moeten nog maar dat ligt lastiger.
- [ ] PreviewKnop laat alleen preview zien van geselecteerde foto links.. ookal is er een foto
      uit de rechter lijst actief in de previewbox.
- [ ] Welke foto is actief? lijsten van kleur doen verschieten bij activeren of zoiets? Focus..
- [ ] Extern opgeslagen DB kunnen gebruiken? Of alleen importeren?
- [ ] DB onderhoud?
- [ ] Context-sensitive popupmenu op tvFiles voor "maak actieve map default"
- [ ] DB kunnen backupen, ook op externe server zoals DropBox of zo..
- [ ] Moet iets verzinnen op de listctrl, setitemdata/getitemdata etc.. nu ben ik 'verplicht' pad te laten zien in een listctrl-column.
- [ ] Foto's van aquaforum-server downloaden om de dimensies op te slaan in DB?
      Opslagdatum lukt niet, alleen (eventueel aanwezige) EXIF-data met de aanmaakdatum, laatste wijzigingsdatum staat op de server? Heb niet voldoende rechten om die in de lezen.
- [ ] "Maar mijn Norton antivirus scanner accepteert hem niet en gooit hem meteen weer van mijn pc af."
- [ ] Gaan deze namen goed?  "Lel!_fi$h" en "?!Aron!?" "Ad " .. zonder aanhalingstekens.
- [ ] Screencast maken.
- [ ] Werken met toetsenbord (tab/enter) is een chaos.
- [ ] taborder.. Moet getest op Windows, Xfce laat veelal niet zien of een control focus heeft. (hangt af van 'the theme')
- [ ] Archive-dialog sizable.
- [ ] Windows -> Klikken op Archief met lege DB laat geen melding zien dat er geen foto's te tonen zijn.
- [ ] Windows -> Sommige PNG's doen het niet in onbtnVoorbeeldClick() .. waaronder ChessMCE.png
- [ ] Beschrijving per foto opslaan in DB
- [x] fotorama 4.6.3 -> 4.6.4

# Versie 0.85
- [x] Als DB-versie = HOGER dan huidige App-versie.. verplicht nieuwste versie van App te installeren.
- [x] diversen.UpdateAvailable() -> timeout=x heeft geen effect bij geen internet.
      Opgelost door eerst te checken voor internet-connectie.. is_connected()
- [x] Meerdere foto's tegelijk kunnen selecteren om toe te voegen in de uploadlijst.
- [x] Meerdere foto's tegelijk in uploadlijst kunnen selecteren.. en wissen.
- [x] Archive.html (nu archivenew.html) wil ik aanpakken.. is lastige K-klus.
- [x] HTML/CSS/Javascript/JSON vanuit code genereren en in 1 bestand houden, zonder HTTPServer.
- [x] Oude archive.html ook blijven aanbieden, met HTTPServer.
- [x] (tvFiles) Actieve (visible) node staat "onderin" de clientarea. Alleen GTK2/3, Windows ok.
- [x] DateTime-stamp per foto opslaan in DB
- [x] size/dimensie per foto opslaan in DB
- [x] Alleen GTK2/3? (Windows gaat prima) Alleen bij eerste keer sluiten confdialog wordt mainframe iets groter ..
      fixed: self.fit() alleen als diversen.USER_PREVIEW is changed.
- [x] listFiles leeg kunnen maken met knop.
- [x] add to history to db
- [x] foutafhandeling bij het importeren. (wat als JSON nog steeds niet kan worden verwerkt? Test!!)
- [x] dubbele entries verwijderen uit DB versie 0.84 voordat ik importeer .. DISTINCT?
- [x] dubbele entries voorkomen tijdens de import vanuit JSON en bij het toevoegen van een URL
- [x] Progressindicatie bij.. genereren preview, uploaden
- [x] Waarschuwen bij dubbele import.
- [x] alpha eruit slopen.
- [x] bij Preview = False wil ik de knoppen in het midden van het scherm.
- [x] Beginpad configuratie functioneel maken
- [x] met dubbelklik en Enter-toets foto in uploadlijst kunnen zetten.
- [x] Previewknop -> preview tonen van eventueel geselecteerde foto, anders front.jpg
- [x] Na upload listFiles wissen
- [x] Bij "geen Preview" .. preview-bitmap verwijderen.
- [x] Tooltips aan/uit
- [x] Check for update (+ automatisch), let op: als er dan is ge-update voorkomen dat er (bij opstart app.) nogmaals wordt aangegeven dat er een update is.. browser-cache?
- [x] Menu -> Afsluiten
- [x] bij sluiten confdialog niet het treeview-pad verzetten.
- [x] Windows -- tooltips zijn AAN bij UIT
- [x] Image/Plaatje wordt FOTO en folder/directory wordt MAP.. overal aanpassen.
- [x] Tijdens installatie "aquaf v0.84" verwijderen uit het Windows-startmenu.
- [x] Bij afsluiten app: als er bestanden in listFiles staan.. vragen of die nog moeten worden ge-upload of niet.
- [x] Context-sensitive popupmenu op tvFiles voor "upload selection"
