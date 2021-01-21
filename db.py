import os,sqlite3


def init():
    os.system("touch pat.db")
    conn = sqlite3.connect("pat.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE pat
    (name text, desc text, url text, paturl text)''')
    conn.commit()
