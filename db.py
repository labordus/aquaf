import sqlite3
import os
import appdirs
import json


def Initialize_db():
    returnvalue = True
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblApp(
                      VERSIE INTEGER,
                      USERNM VARCHAR(30),
                      FIRSTRUN BOOLEAN DEFAULT (1),
                      IMPORTED BOOLEAN DEFAULT (0),
                      DIMID INTEGER REFERENCES tblDim(dimID))''')
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblLink(
                      linkID INTEGER PRIMARY KEY NOT NULL,
                      linkURL VARCHAR(200))''')
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblDim(
                      dimID INTEGER PRIMARY KEY AUTOINCREMENT,
                      dimOM TXT)''')
        conn.commit()
        c.execute('SELECT USERNM FROM tblApp')
        if not c.fetchone():  # geen record/row gevonden
            sDims = [['800x600'], ['640x480'], ['320x240'], ['160x120']]
            c.executemany('''INSERT INTO tblDim(dimOM)
                    VALUES(?)''', sDims)
#            conn.commit()
            c.execute('''INSERT INTO tblApp(VERSIE,USERNM,FIRSTRUN,dimID)
                    VALUES(?,?,?,?)''', (int(84), '', 1, 2))
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
#        firstrun = bool(c.fetchone()[0])
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


def get_username():
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


def set_username(userName):
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


def DB2JSON():
    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'aquaf.json')
    dbpath = path_to_db()
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("SELECT * FROM tblLink")
    rows = cursor.fetchall()
    if len(rows) == 0:  # Geen data? Return False
        return False

    rowarray_list = []
    for row in rows:
        t = str((row[1]))
        rowarray_list.append({"link": t})
    j = json.dumps({'items': rowarray_list}, indent=2, separators=(',', ': '))

    try:
        fp = open(filepath, "w")
    except IOError:
        # If not exists, create the file
        fp = open(filepath, "w+")
    fp.write(j)
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
#        c.execute('SELECT IMPORTED FROM tblApp')
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
        raw_objs_string = open(fileJSON).read()  # read in raw data
        raw_objs_string = raw_objs_string.replace('items:', '"items":')  # insert a comma between each object
        objs_string = '[%s]' % (raw_objs_string)  # wrap in a list, to make valid json
        data = json.loads(objs_string)  # parse json
    #    data = json.loads("[%s]" % (open(fileJSON).read().replace('items:', '"items":')))
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        #        print 'Decoding JSON has failed'
        raise ValueError

    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    aantal = 0
    for line in data[0]["items"]:
        try:
            aantal += 1
            c.execute("INSERT INTO tblLink(linkURL) VALUES(?)", (line["link"],))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.rollback()
            raise sqlite3.IntegrityError
    conn.close()
    return aantal
#    json_data.close()


def addURL2DB(url):
    dbpath = path_to_db()
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    try:
        c.execute("INSERT INTO tblLink(linkURL) VALUES(?)", (url,))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.rollback()
        raise sqlite3.IntegrityError

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


def getUserDimensie():
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
#        conn.text_factory = str
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''SELECT dimID FROM tblApp''')
        iDim = c.fetchone()[0]
#        c.execute('''SELECT dimOM FROM tblDim WHERE dimID = ? ''', (iDim, ))
#        Dimensie = c.fetchone()[0]
    except Exception as e:
        raise e
    finally:
        conn.close()

    return iDim


def getDimensies():  # return list of dims en return listindex?
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
