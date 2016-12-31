# Martin Kersner, m.kersner@gmail.com
# 2016/12/31

import sqlite3

class db:
  db_name = "db.sqlite3"
  conn = None
  danawa10_tablename  = "DANAWA10"
  danawa100_tablename = "DANAWA100"

  def __init__(self):
    self.conn = sqlite3.connect(self.db_name)

    if not self.Danawa10Exist():
      conn.execute('''CREATE TABLE {0}
        (ID    INT PRIMARY KEY  NOT NULL,
  	 DATE  DATETIME         NOT NULL,
  	 LIST  TEXT             NOT NULL);'''.format(self.danawa10_tablename))

  def Danawa10Exist(self):
    c = self.conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{0}';".format(self.danawa10_tablename))

    if c.fetchone() == None:
       return False
    else:
      return True
