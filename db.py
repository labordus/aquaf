import sqlite3


def get_username():
    try:
        conn = sqlite3.connect('aquaf.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblApp(
                      USERID INT PRIMARY KEY    NOT NULL  DEFAULT (1),
                      USERNM VARCHAR(30))''')
        conn.commit()
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
    conn = sqlite3.connect('aquaf.db')
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO tblApp(USERID,USERNM)
                  VALUES(?,?)''', (1, userName))
    except sqlite3.IntegrityError:
        c.execute('''UPDATE tblApp SET USERNM = ? WHERE USERID = ? ''',
                  (userName, 1))
    conn.commit()
    conn.close()
    print "Gebruikersnaam is nu " + userName

#         firstrow = str(c.fetchone()[0])
# if firstrow is not "None":  # niet leeg
#             c.execute('''UPDATE tblApp SET USERNM = ? WHERE ROWID = ? ''',
#                       ("nieuwenaamviaupdate", 1))
#             conn.commit()
#         else:
#             c.execute('''INSERT INTO tblApp(USERNM)
#                   VALUES(?)''', (userName,))
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
