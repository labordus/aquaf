import sqlite3
import os
import appdirs
import json
from diversen import APP_VERSION  # , PREVIEW
import diversen
import datetime

old_urls = []
old_username = None
old_preview = None
old_dim = None

default_username = ''
default_dim = 2
default_firstrun = 1
default_datetimestamp = datetime.datetime(year=1968, month=8, day=27)  # Time wordt 0:00

default_dimensies = [['800x600'], ['640x480'], ['320x240'], ['160x120']]


def DBVersion():
    filepath = path_to_db()

    if os.path.exists(filepath):
        try:
            conn = sqlite3.connect(filepath)
            cursor = conn.cursor()
            cursor.execute("SELECT VERSIE FROM tblApp")
            rows = cursor.fetchall()
            s = str(rows[0][0])
            if s != '0.85':
                # DISTINCT om eventueel aanwezige dubbele entries uit te filteren.
                cursor.execute("SELECT DISTINCT linkURL FROM tblLink")
                rows = cursor.fetchall()
                for row in rows:
                    sUrl = str((row[0]))
                    old_urls.append(sUrl)
                    conn.close()
                try:
                    os.remove(filepath)
                except OSError as e:
                    print ("Error: %s - %s." % (e.filename, e.strerror))
        except Exception as e:
            conn.rollback()
            conn.close()
            raise e
#        finally:
#            conn.close()


def Initialize_db():
    DBVersion()

    returnvalue = True
    filepath = path_to_db()
    try:
        #        conn = sqlite3.connect(filepath, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn = sqlite3.connect(filepath, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblApp(
                      VERSIE VARCHAR(7),
                      USERNM VARCHAR(30),
                      FIRSTRUN BOOLEAN DEFAULT (1),
                      IMPORTED BOOLEAN DEFAULT (0),
                      PREVIEW BOOLEAN DEFAULT (1),
                      TOOLTIP BOOLEAN DEFAULT (1),
                      FOLDER VARCHAR(120),
                      DIMID INTEGER REFERENCES tblDim(dimID))''')
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblLink(
                      linkID INTEGER PRIMARY KEY NOT NULL,
                      linkURL VARCHAR(200) UNIQUE,
                      linkDATETIME TIMESTAMP,
                      linkOM VARCHAR(200))''')
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblDim(
                      dimID INTEGER PRIMARY KEY AUTOINCREMENT,
                      dimOM TXT)''')
        conn.commit()
# geen record/row gevonden in tblDIM
        c.execute('SELECT * FROM tblDim')
        if not c.fetchone():
            c.executemany('''INSERT INTO tblDim(dimOM)
                    VALUES(?)''', default_dimensies)
# geen record/row gevonden in tblApp
        c.execute('SELECT * FROM tblApp')
        data = c.fetchall()
        if len(data) == 0:
            c.execute('''INSERT INTO tblApp(VERSIE,USERNM,FIRSTRUN,dimID)
                    VALUES(?,?,?,?)''', (APP_VERSION, default_username, default_firstrun, default_dim))
# if len(rowarray_list_url[0]) != 0:
        if old_urls is not None:  # Er zijn nog urls weg te schrijven
            for r in old_urls:
                c.execute("INSERT INTO tblLink(linkURL,linkDATETIME) VALUES(?,?)", (r, default_datetimestamp))
#                c.executemany('''INSERT INTO tblLink(linkURL)
#                    VALUES(?)''', rowarray_list_url)
            conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
        returnvalue = False
    finally:
        conn.close()
    return returnvalue


def path_to_db():
    path = appdirs.user_data_dir('aquaf', False, False, False)
    check_path_exists(os.path.join(path, 'aquaf.db'))
    filepath = os.path.join(path, 'aquaf.db')
    return filepath


def check_path_exists(path):
    d = os.path.dirname(path)
    if not os.path.exists(d):
        os.makedirs(d)


def first_run():
    filepath = path_to_db()
#    Initialize_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('SELECT FIRSTRUN FROM tblApp')
        firstrun = int(c.fetchone()[0])
        if firstrun == 1:
            c.execute('''UPDATE tblApp SET FIRSTRUN = ? WHERE ROWID = ? ''', (0, 1))
            conn.commit()
        else:
            firstrun = 0
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

    return firstrun


def getUsername():
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('SELECT USERNM FROM tblApp')
        try:
            userName = str(c.fetchone()[0])
        except:  # leeg veld
            userName = ""
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

    return userName


def setUsername(userName):
    filepath = path_to_db()
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    try:
        c.execute('''UPDATE tblApp SET USERNM = ? WHERE ROWID = ? ''',
                  (userName, 1))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.rollback()
        raise sqlite3.IntegrityError
    finally:
        conn.close()
    print "Gebruikersnaam is nu " + userName


def DB2Webfile():
    import string
    from archive_template import webpage

    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'archive.html')
    dbpath = path_to_db()
    connection = sqlite3.connect(dbpath, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('''SELECT linkURL, linkDATETIME as "[timestamp]" FROM tblLink ORDER BY linkDATETIME''')
    rows = cursor.fetchall()
    if len(rows) == 0:  # Geen data? Return False
        connection.close()
        return False

    rowarray_list = []
    for row in rows:
        t = str((row[0]))  # link
        d = (row[1])  # stamp
        if d == default_datetimestamp:
            d = "onbekend"
        else:
            d = d.strftime("%d %B %Y")
        rowarray_list.append({"img": t, "stamp": d})

    html_json = json.dumps({'data': rowarray_list}, indent=2, separators=(',', ': '))

    tpl = string.Template(webpage)
    d = {'jsoncontent': html_json}

    html_alles = tpl.safe_substitute(d)

    try:
        fp = open(filepath, "w")
    except IOError:
        # If not exists, create the file
        fp = open(filepath, "w+")
    fp.write(html_alles)
    fp.close()

    connection.close()

    return True


def IfAlreadyImported():
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('SELECT IMPORTED FROM tblApp')
        imported = int(c.fetchone()[0])
        if imported == 1:
            return True
        else:
            return False
    except Exception as e:
        raise e
    finally:
        conn.close()


def SetImported():
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''UPDATE tblApp SET IMPORTED = ? WHERE ROWID = ? ''', (1, 1))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def ImportJSON2DB(fileJSON):
    dbpath = path_to_db()

# ### FIX (oude) JSON.. het is namelijk geen valid JSON. ### #
# Hier zet ik 'items' tussen double quotes.

    try:
        # read in raw data
        raw_objs_string = open(fileJSON).read()
        # insert a comma between each object
        raw_objs_string = raw_objs_string.replace('items:', '"items":')
        # wrap in a list, to make valid json
        objs_string = '[%s]' % (raw_objs_string)
        # parse json
        data = json.loads(objs_string)
    #    data = json.loads("[%s]" % (open(fileJSON).read().replace('items:', '"items":')))
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        #        print 'Decoding JSON has failed'
        raise ValueError

    conn = sqlite3.connect(dbpath, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    totaal = 0
    mislukt = 0
    for line in data[0]["items"]:
        try:
            totaal += 1
            c.execute("INSERT INTO tblLink(linkURL,linkDATETIME) VALUES(?,?)", (line["link"], default_datetimestamp))
            conn.commit()
        except sqlite3.IntegrityError:
            # Zullen dubbele entries zijn.. dus laat maar waaien.
            mislukt += 1
            pass
    conn.close()

    return totaal, mislukt
#    json_data.close()


def addDATA2DB(url):
    dbpath = path_to_db()
    conn = sqlite3.connect(dbpath, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    vandaag = datetime.datetime.now()
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    try:
        c.execute("INSERT INTO tblLink(linkURL, linkDATETIME) VALUES(?,?)", (url, vandaag))
        conn.commit()
    except sqlite3.IntegrityError:
        # Zal dubbele entry zijn.. dus laat maar waaien.
        pass

    conn.close()


def getUserName():
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''SELECT USERNM FROM tblApp''')
        username = c.fetchone()[0]
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

    return username


def getUserPreview():
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''SELECT PREVIEW FROM tblApp''')
        bPreview = c.fetchone()[0]
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

    return bPreview


def setUserPreview(bPreview):
    filepath = path_to_db()
    diversen.PREVIEW = bPreview
    if bPreview:
        bPreview = 1
    else:
        bPreview = 0

    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''UPDATE tblApp SET PREVIEW = ? ''', (bPreview,))
#        bPreview = c.fetchone()[0]
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def getUserTooltip():
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''SELECT TOOLTIP FROM tblApp''')
        bTooltip = c.fetchone()[0]
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

    return bTooltip


def setUserTooltip(bTooltip):
    filepath = path_to_db()
    diversen.USER_TOOLTIP = bTooltip
    if bTooltip:
        bTooltip = 1
    else:
        bTooltip = 0

    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''UPDATE tblApp SET TOOLTIP = ? ''', (bTooltip,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def getUserFolder():
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''SELECT FOLDER FROM tblApp''')
        sFolder = c.fetchone()[0]
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

    return sFolder


def setUserFolder(sFolder):
    filepath = path_to_db()
    diversen.USER_FOLDER = sFolder

    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''UPDATE tblApp SET FOLDER = ? ''', (sFolder,))
#        bPreview = c.fetchone()[0]
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def setUserDimensie(sDim):
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''SELECT dimID FROM tblDim WHERE dimOM = ? ''', (sDim, ))
        iDim = c.fetchone()[0]
        c.execute('''UPDATE tblApp SET dimID = ? WHERE ROWID = ? ''', (iDim, 1))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def getUserDimensieID():
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
#        conn.text_factory = str
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''SELECT dimID FROM tblApp''')
        iDim = c.fetchone()[0]
    except Exception as e:
        raise e
    finally:
        conn.close()

    return iDim


def getDimensies():  # return list of dims.. en return listindex?
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        conn.text_factory = str
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
#        c.execute('SELECT dimID FROM tblApp')
#        dimID = int(c.fetchone()[0])
#        c.execute('''SELECT dimOM FROM tblDim WHERE dimID = ? ''', (dimID))
        c.execute('''SELECT dimOM FROM tblDim''')
        dims = [r[0] for r in c.fetchall()]  # convert list of tuples to a list
    except Exception as e:
        raise e
    finally:
        conn.close()

    return dims
