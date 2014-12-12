import sqlite3
import os
import appdirs
from mechanize._beautifulsoup import Null


def Initialize_db():
    returnvalue = True
    filepath = path_to_db()
    try:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblApp(
                      USERID INT PRIMARY KEY NOT NULL  DEFAULT (1),
                      USERNM VARCHAR(30),
                      FIRSTRUN BOOLEAN DEFAULT (1))''')
        conn.commit()
        c.execute('SELECT USERNM FROM tblApp')
        if not c.fetchone():  # geen record/row gevonden
            c.execute('''INSERT INTO tblApp(USERID,USERNM,FIRSTRUN)
                    VALUES(?,?,?)''', (1, '', 1))

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
        c.execute('SELECT FIRSTRUN FROM tblApp')
#        firstrun = bool(c.fetchone()[0])
        firstrun = int(c.fetchone()[0])
        if firstrun == 1:
            c.execute('''UPDATE tblApp SET FIRSTRUN = ? WHERE USERID = ? ''', (0, 1))
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


def DB2JSON2():
    import json
    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'aquaf.json')
    connection = sqlite3.connect('/home/kelp/.local/share/aquaf/aquaftest.db')
    cursor = connection.cursor()
    cursor.execute("select linkURL from tblLink")
    rows = cursor.fetchall()
    info = ""
    for row in rows:
        info = str(row[0])
        json.dumps({info}, sort_keys=True,
                   indent=4, separators=(',', ': '))
#    print info
#    print json.dumps({'4': info, '6': 7}, sort_keys=True,
#                     indent=4, separators=(',', ': '))
#    print json.dumps(info)
#    parks = []
#    for row in rows:
#        parks.append({
#            'linkURL': row[0],
#        })
#    print json.dump(parks, separators=(',', ':'))

    connection.close()


def DB2JSON():
    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'aquaf.json')
    connection = sqlite3.connect('/home/kelp/.local/share/aquaf/aquaftest.db')
    cursor = connection.cursor()
    cursor.execute("select linkURL from tblLink")
    rows = cursor.fetchall()
    voortext = '''{ "items": [
'''
    linktext = ""
    for row in rows:
        linktext = linktext + '''
        {
      "link":"%s"
    }
,''' % row[0]

    achtertext = '''
]}
'''
    text = voortext + linktext[:-1] + achtertext

    try:
        fp = open(filepath, "w")
    except IOError:
        # If not exists, create the file
        fp = open(filepath, "w+")
    fp.write(text)
    fp.close()
    connection.close()


def JSON2DB():
    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'aquaf.json')

#    f = open(filepath, 'r')
#    content = f.read()
#    f.close()
    import json
    json_data = open(filepath)
    data = json.load(json_data)
#    print(data)
#    foo = json_data[0]["link"]
#    foo = data["items"][0]["link"]
    for line in data["items"]["link"]:
        print line
    json_data.close()
