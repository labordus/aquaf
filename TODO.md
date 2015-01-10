- [x] HTML/CSS/Javascript/JSON vanuit code genereren en in 1 bestand houden.
- [x] Oude archive.html blijven aanbieden.
- [x] DateTime-stamp per foto opslaan in DB
- [x] size/dimensie per foto opslaan in DB
- [ ] Beschrijving per foto opslaan in DB
- [ ] Windows -> Klikken op Archief met lege DB laat geen melding zien.
- [x] add to history to db
- [ ] Fetch foto van remote URL? Flickr, Picasa etc..
- [x] foutafhandeling bij het importeren. (wat als JSON nog steeds niet kan worden verwerkt? Test!!)
- [x] dubbele entries verwijderen uit DB versie 0.84 voordat ik importeer .. DISTINCT?
- [x] dubbele entries voorkomen tijdens de import vanuit JSON en bij het toevoegen van een URL
- [x] Progressindicatie bij.. genereren preview, uploaden
- [x] alpha eruit slopen.
- [ ] Archive-dialog sizable.
- [x] Beginpad configuratie functioneel maken
- [x] met dubbelklik en Enter-toets foto in uploadlijst zetten
- [x] Previewknop -> preview tonen van geselecteerde foto
- [ ] Werken met toetsenbord (tab/enter) is een chaos.
- [ ] taborder.. Moet getest op Windows, Xfce laat veelal niet zien of een control focus heeft. (hangt af van 'the theme')
- [x] Na upload listFiles wissen
- [x] Bij "geen Preview" .. preview-bitmap verwijderen.
- [x] Tooltips aan/uit
- [ ] Alleen GTK2/3? (Windows gaat prima) Alleen bij eerste keer sluiten confdialog wordt mainframe iets groter .. self.fit()
- [ ] bij Preview = False wil ik de knoppen in het midden van het scherm.
- [x] bij sluiten confdialog niet het treeview-pad verzetten.
- [x] Windows -- tooltips zijn AAN bij UIT
- [x] Image/Plaatje wordt FOTO en folder/directory wordt MAP.. overal aanpassen.
- [ ] Maak huidige/actieve directory default. Knoppie of context-sensitive popupmenu op right-click?
- [x] Archive.html wil ik aanpakken.. is lastige K-klus.
- [ ] Gebruikershandleiding cq. stappenoverzicht met plaatjes maken.
- [x] Tijdens installatie "aquaf v0.84" verwijderen uit het Windows-startmenu.
- [ ] Moet iets verzinnen op de listctrl, setitemdata/getitemdata etc..
- [x] Bij afsluiten app: als er bestanden in listFiles staan.. vragen of die nog moeten worden ge-upload of niet.
- [ ] Plaatjes van server downloaden om de dimensies op te slaan in DB?

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
