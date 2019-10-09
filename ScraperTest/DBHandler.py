import os
import sqlite3

def connectToDB():
    db_filename = 'scraper.db'
    dbIsNew = not os.path.exists(db_filename)

    conn = sqlite3.connect(db_filename)
    return conn

def addURLTable(url):
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO RecipeURL(RecipeURL) Values (?)", (url, ))
    conn.commit()
    cursor.close()
    conn.close()

def clearURLTable():
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM RecipeURL")
    conn.commit()
    cursor.close()
    conn.close()

def showURLTable():
    conn = connectToDB()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM RecipeURL").fetchall()
    print("rows in showDB URL: "+str(len(rows)))
#    for row in rows:
#       print(row)
    cursor.close()
    conn.close()