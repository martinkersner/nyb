# Martin Kersner, m.kersner@gmail.com
# 2016/12/31

import sqlite3

class db:
  db_name = "db.sqlite3"
  conn = None
  danawa10_tablename  = "DANAWA10"
  danawa100_tablename = "DANAWA100"

  def __init__(self, data):
    self.conn = sqlite3.connect(self.db_name)

    if not self.Danawa10Exist():
      self.conn.execute('''CREATE TABLE {0}
        (ID    INTEGER PRIMARY KEY  AUTOINCREMENT,
         DATE  DATETIME         NOT NULL,
         RANK  TEXT             NOT NULL);'''.format(self.danawa10_tablename))
      self.conn.commit()

    if data != None:
      self.AddToDanawa10(data)

  def Danawa10Exist(self):
    c = self.conn.cursor()
    c.execute('''SELECT name
                 FROM sqlite_master
                 WHERE type='table' AND name='{0}';'''.format(self.danawa10_tablename))

    if c.fetchone() == None:
       return False
    else:
      return True

  def AddToDanawa10(self, data):
    c = self.conn.cursor()
    data_str = str(data).replace("'", "''")
    print(data_str)
    c.execute('''INSERT INTO {0} (DATE, RANK)
                 VALUES (DATETIME('now'), '{1}');'''.format(self.danawa10_tablename, data_str))
    self.conn.commit()
