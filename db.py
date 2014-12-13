import sqlite3
import os
import appdirs
from mechanize._beautifulsoup import Null
import json
import re


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
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblLink(
                      linkID INTEGER PRIMARY KEY NOT NULL,
                      linkURL VARCHAR(200))''')
        conn.commit()
        c.execute('SELECT USERNM FROM tblApp')
        if not c.fetchone():  # geen record/row gevonden
            c.execute('''INSERT INTO tblApp(USERID,USERNM,FIRSTRUN)
                    VALUES(?,?,?)''', (1, '', 1))
#            c.execute('''INSERT INTO tblLink(linkURL)
#                    VALUES(?)''', ("testurlie_1"))
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


def DB2JSON():
    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'aquaf.json')
    dbpath = path_to_db()
#    connection = sqlite3.connect('/home/kelp/.local/share/aquaf/aquaftest.db')
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tblLink")
    rows = cursor.fetchall()

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


def ImportJSON2DB(fileJSON):
    dbpath = path_to_db()

# ### FIX (oude) JSON.. het is namelijk geen valid JSON. ### #
# Hier zet ik 'items' tussen double quotes.
    raw_objs_string = open(fileJSON).read()  # read in raw data
    raw_objs_string = raw_objs_string.replace('items:', '"items":')  # insert a comma between each object
    objs_string = '[%s]' % (raw_objs_string)  # wrap in a list, to make valid json
    data = json.loads(objs_string)  # parse json
#    data = json.loads("[%s]" % (open(fileJSON).read().replace('items:', '"items":')))

    conn = sqlite3.connect(dbpath)
    c = conn.cursor()

    for line in data[0]["items"]:
        try:
            c.execute("INSERT INTO tblLink(linkURL) VALUES(?)", (line["link"],))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.rollback()
            raise sqlite3.IntegrityError

    conn.close()
#    json_data.close()
