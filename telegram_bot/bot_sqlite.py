#!/usr/bin/python

import sqlite3
import datetime
from config import *
def create():
    conn = sqlite3.connect('scut_gugugu_bot.db')
    print("Opened database successfully")
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS TODO;')
    c.execute('CREATE TABLE TODO' +
                '(ID         INTEGER PRIMARY KEY AUTOINCREMENT,'+
                'NAME           TEXT     NOT NULL,'+
                'CONTENT        TEXT     NOT NULL,'+
                'DDL            DATE             ,'+
                'OK             BOOL     NOT NULL);')
    c.execute('DROP TABLE IF EXISTS DO;')
    c.execute('CREATE TABLE DO ' +
                '(ID         INTEGER PRIMARY KEY AUTOINCREMENT,'+
                'NAME           TEXT     NOT NULL,'+
                'CONTENT        TEXT             ,'+
                'TIME           DATE     NOT NULL;')
    c.execute('DROP TABLE IF EXISTS CONTENTS;')
    c.execute('CREATE TABLE CONTENTS '+
                '(ID         INTEGER PRIMARY KEY AUTOINCREMENT,'+
                'NAME           TEXT     NOT NULL,'+
                'LINK           TEXT     NOT NULL,'+
                'CONTENT        TEXT             ,'+
                'TIME           DATE);')
    conn.commit()
    c.close()
    conn.close()

def get_todo_resc(msg_argv):
    try:
        _name = msg_argv[0]
        _name = NAMETR[_name]
    except Exception:
        return ['Err',['<p> <font color=red> error command argv or no uesr </font> </p>']]
    try:
        conn = sqlite3.connect('scut_gugugu_bot.db')
        c = conn.cursor()
        resc = c.execute('SELECT * FROM TODO WHERE '+
                        'NAME = "'+_name+'";').fetchall()
        conn.commit()
        c.close()
    except Exception:
        return ['Err', ['<p> <font color=red>sql error, please contact Admin </font> </p>']]
    return [_name, resc]

def get_todo(msg_argv):
    resc = get_todo_res(msg_argv[1:])
    if(resc[0] == 'Err') return resc[1][0]
    res = '<table> <caption> ['+resc[0]+'] todo list: </caption>'
    for i in resc[1]:
        if(i[4] == 'no') :
            res = res + '<tr> <th>' + str(i[0])+'</th> <th>'+str(i[2])+'</th> <th><font color = red>'+str(i[3])+'</font></th> </tr>'
    res = res + '</table>'
    return res

def set_todo(msg_argv):
    if(len(msg_argv) != 3):return '<p> <font color=red> wrong number of command argv </font> </p>'
    try:
        msg_argv = msg_argv[1:]
        msg_argv[0] = NAMETR[msg_argv[0]]
    except Exception:
        return '<p> <font color=red> no user </font> </p>'
    try:
        conn = sqlite3.connect("scut_gugugu_bot.db")
        c = conn.cursor()
        DDL = str(datetime.date.today() + datetime.timedelta(days=30))
        c.execute('INSERT INTO TODO(NAME, CONTENT, DDL, OK) VALUES ('+
                    '"'+msg_argv[0]+'", '+
                    '"'+msg_argv[1]+'", '+
                    '"'+DDL+'", "no");')
        conn.commit()
        c.close()
    except Exception:
        return '<p> <font color=red> sql error, please contact Admin </font> </p>'
    return '<p> <font color=green> ok </font> </p>'

def get_done(msg_argv):
    resc = get_todo_res(msg_argv[1:])
    if(resc[0] == 'Err') return resc[1][0]
        res = '<table> <caption> ['+resc[0]+'] todo list: </caption>'
    for i in resc[1]:
        if(i[4] == 'yes') :
            res = res + '<tr> <th>' + str(i[0])+'</th> <th>'+str(i[2])+'</th> <th><font color = red>'+str(i[3])+'</font></th> </tr>'
    res = res + '</table>'
    return res

def set_done(msg_argv):
    if(len(msg_argv) != 2 and len(msg_argv) != 3) : 
        return '<p> <font color=red> wrong number of command argv </font> </p>'
    try:
        msg_argv[0] = NAMETR[msg_argv[0]]
    except Exception:
        return '<p> <font color=red> no user </font> </p>'
    if(len(msg_argv) == 2) :
        try:
            conn = sqlite3.connect("scut_gugugu_bot.db")
            c = conn.cursor()
            c.execute('INSERT INTO TODO(NAME, CONTENT, DDL, ok) VALUES ('+
                        '"'+msg_argv[0]+'", '+
                        '"'+msg_argv[1]+'", '+
                        '"'+str(datetime.date.today())+'", "yes");')
            conn.commit()
            c.close()
        except Exception:
            return '<p> <font color=red> sql error, please contact Admin </font> </p>'
    if(len(msg_argv) == 3) :
        try:
            conn = sqlite3.connect("scut_gugugu_bot.db")
            c = conn.cursor()
            res = c.execute('UPDATE TODO SET ok == "yes" where ' +
                            'name = '+msg_argv[0]+'and id = "' + msg_argv[2]+'";')
            conn.commit()
            c.close()
        except Exception:
            return '<front><p> <font color=red> sql error, please contact Admin </font> </p>'
    return '<p> <font color=red> ok </font> </p>'

def getContest(name):
    pass

def setContest(name):
    pass

def main():
    pass
#    create()
    
if __name__ == '__main__':
    main()
