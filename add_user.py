# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:13:12 2020

@author: jadab
"""

import hashlib
import sqlite3
import getpass
from login import *

DB_NAME = "ppab6.db"



def name_available(username):
    conn = sqlite3.connect(DB_NAME)        
    c = conn.cursor()
    
    result = c.execute("""
              SELECT username
              FROM users
              WHERE username=?""",
              (username,)).fetchone()
    return result is None
    
def add_user(username, password):
    conn = sqlite3.connect(DB_NAME)        
    c = conn.cursor()
    
    password = hash_given(password)
        
    sql_insert = """
    INSERT INTO users(username, password_hash)
    VALUES(?,?);
    """
    login = (username, password)
    
    try:
        c.execute(sql_insert, login)
    except:
        conn.rollback()
    
    print("User created")
    conn.commit()
    conn.close()        
    
    
    
    
if __name__ == "__main__":
    print("Hello. Let's create a new account.")
    while True:
        username = input("Please enter your username: \n")
        if name_available(username):
            print("Username is available")
            break
        else:
            print("Username is taken. Choose another one.")
            
    password = getpass.getpass("Please enter your password: \n")

        
    add_user(username, password)
    print("Sucessfully added %s to the database!" % username)
    
    
    
            
