- [x] diversen.UpdateAvailable() -> timeout=x heeft geen effect bij geen internet.
      Opgelost door eerst te checken voor internet-connectie.. is_connected()
- [x] Meerdere foto's tegelijk kunnen selecteren om toe te voegen in de uploadlijst.
- [x] Meerdere foto's tegelijk in uploadlijst kunnen selecteren.. en wissen.
- [x] Bij initialisatie app wat global variabelen zetten, zodat ik ze niet telkens uit de DB hoef te trekken.
- [ ] APP_VERSIE en USER_DIMENSIE moeten nog maar dat ligt lastiger.
- [x] HTML/CSS/Javascript/JSON vanuit code genereren en in 1 bestand houden, zonder HTTPServer.
- [x] Oude archive.html ook blijven aanbieden, met HTTPServer.
- [ ] (tvFiles) Actieve (visible) node staat "onderin" de clientarea. Is dit alleen Linux??
- [x] DateTime-stamp per foto opslaan in DB
- [x] size/dimensie per foto opslaan in DB
- [ ] Maak huidige/actieve directory default. Knoppie of context-sensitive popupmenu op right-click?
- [ ] Alleen GTK2/3? (Windows gaat prima) Alleen bij eerste keer sluiten confdialog wordt mainframe iets groter .. self.fit()
- [ ] Windows -> Klikken op Archief met lege DB laat geen melding zien dat er geen foto's te tonen zijn.
- [x] listFiles leeg kunnen maken met knop.
- [x] add to history to db
- [x] foutafhandeling bij het importeren. (wat als JSON nog steeds niet kan worden verwerkt? Test!!)
- [x] dubbele entries verwijderen uit DB versie 0.84 voordat ik importeer .. DISTINCT?
- [x] dubbele entries voorkomen tijdens de import vanuit JSON en bij het toevoegen van een URL
- [x] Progressindicatie bij.. genereren preview, uploaden
- [x] Waarschuwen bij dubbele import.
- [x] alpha eruit slopen.
- [ ] Archive-dialog sizable.
- [ ] bij Preview = False wil ik de knoppen in het midden van het scherm.
- [ ] Gebruikershandleiding cq. stappenoverzicht met plaatjes maken.
- [x] Beginpad configuratie functioneel maken
- [x] met dubbelklik en Enter-toets foto in uploadlijst kunnen zetten.
- [x] Previewknop -> preview tonen van eventueel geselecteerde foto, anders front.jpg
- [ ] Werken met toetsenbord (tab/enter) is een chaos.
- [ ] taborder.. Moet getest op Windows, Xfce laat veelal niet zien of een control focus heeft. (hangt af van 'the theme')
- [x] Na upload listFiles wissen
- [x] Bij "geen Preview" .. preview-bitmap verwijderen.
- [x] Tooltips aan/uit
- [x] Check for update (+ automatisch), let op: als er dan is ge-update voorkomen dat er (bij opstart app.) nogmaals wordt aangegeven dat er een update is.. browser-cache?
- [x] Menu -> Afsluiten
- [x] bij sluiten confdialog niet het treeview-pad verzetten.
- [x] Windows -- tooltips zijn AAN bij UIT
- [x] Image/Plaatje wordt FOTO en folder/directory wordt MAP.. overal aanpassen.
- [x] Archive.html wil ik aanpakken.. is lastige K-klus.
- [x] Tijdens installatie "aquaf v0.84" verwijderen uit het Windows-startmenu.
- [x] Bij afsluiten app: als er bestanden in listFiles staan.. vragen of die nog moeten worden ge-upload of niet.
- [ ] Moet iets verzinnen op de listctrl, setitemdata/getitemdata etc.. nu ben ik 'verplicht' pad te laten zien in een listctrl-column.
- [ ] Foto's van aquaforum-server downloaden om de dimensies op te slaan in DB?
      Opslagdatum lukt niet, alleen (eventueel aanwezige) EXIF-data met de aanmaakdatum, laatste wijzigingsdatum staat op de server? Heb niet voldoende rechten om die in de lezen.
- [ ] Fetch foto van remote URL? Flickr, Picasa etc..
- [ ] Beschrijving per foto opslaan in DB
- [ ] "Maar mijn Norton antivirus scanner accepteert hem niet en gooit hem meteen weer van mijn pc af."

##############
'sceleton' db's bij de releases zetten
Of nee.. staat toch al in de code?
Misschien wel de verschillende DB's in een aparte map bijhouden?
Of... 'juiste-versie Databases' bij de releases op github plaatsen? 
##############

# Punten bij release..
* github release aanmaken.
* alle verwijzingen naar testpaden etc.. terugzetten.
* addURL2DB() en ook uploadblabla() uitvinken/aanzetten.
