# Martin Kersner, m.kersner@gmail.com
# 2016/12/31

import sqlite3

class sqliteDB:
  db_name = "db.sqlite3"
  conn = None
  danawa10_tablename  = "DANAWA10"
  danawa100_tablename = "DANAWA100"

  def __init__(self):
    self.conn = sqlite3.connect(self.db_name)
    self.CreateTable(self.danawa10_tablename)
    self.CreateTable(self.danawa100_tablename)

  def ExistTable(self, tablename):
    c = self.conn.cursor()
    c.execute('''SELECT name
                 FROM sqlite_master
                 WHERE type='table' AND name='{0}';'''.format(tablename))

    if c.fetchone() == None:
       return False
    else:
      return True

  def CreateTable(self, tablename):
    if not self.ExistTable(tablename):
      self.conn.execute('''CREATE TABLE {0}
        (ID    INTEGER PRIMARY KEY  AUTOINCREMENT,
         DATE  DATETIME         NOT NULL,
         RANK  TEXT             NOT NULL);'''.format(tablename))
      self.conn.commit()

  def Insert(self, tablename, data):
    if data == None:
      return

    c = self.conn.cursor()
    data_str = str(data).replace("'", "''")
    print(data_str)
    c.execute('''INSERT INTO {0} (DATE, RANK)
                 VALUES (DATETIME('now'), '{1}');'''.format(tablename, data_str))
    self.conn.commit()

  def AddToDanawa10(self, data):
    self.Insert(self.danawa10_tablename, data)

  def AddToDanawa100(self, data):
    self.Insert(self.danawa100_tablename, data)
