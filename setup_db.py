# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:19:37 2020

@author: jadab
"""

import os
import sqlite3

DB_NAME = "ppab6.db"

if __name__ == "__main__":
    if os.path.isfile(DB_NAME):
        while True:
            answer = input("Database file %s alread exists. Would you like to overwite it? [yes/no]" % DB_NAME)
            
            if answer == 'yes':
                print("Okay, recreating database.")
                os.remove(DB_NAME)
                break
            elif answer == 'no':
                print("Okay, exiting.")
                exit(0)
            else:
                print("I don't understand you")
    
    conn = sqlite3.connect('ppab6.db')        
    
    c = conn.cursor()

        
    sql_command = """
        CREATE TABLE users (
        username VARCHAR,
        password_hash VARCHAR
        );"""
    try:
        c.execute(sql_command)
        conn.commit()
        
    except:
        conn.rollback()
    
    print("Database recreated.")
    conn.close()
    