# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:53:10 2020

@author: jadab
"""

import hashlib
import sqlite3
import getpass

DB_NAME = "ppab6.db"

#import users.yaml file
#for use with config file
# import yaml
# with open('users.yaml', 'r') as f:
#     VALID_CREDENTIALS = yaml.safe_load(f)



# def hash_passwords():
#     """

#     Returns sha256 hexi hash for stored passwords
#     -------
#     VALID_CREDENTIALS : TYPE
#         DESCRIPTION.

#     """
#     for user in VALID_CREDENTIALS:
#         temp = VALID_CREDENTIALS[user]
#         temp = hashlib.sha256(temp.encode())
#         VALID_CREDENTIALS[user] = temp.hexdigest()
    
#     return VALID_CREDENTIALS

def hash_given(password):
    """

    Parameters
    ----------
    password : string
        DESCRIPTION.

    Returns sha256 hexidecimal hash
    -------
    result : string sha256 hash
        helper function for is_valid_credentials

    """
    result = hashlib.sha256(password.encode())
    result = result.hexdigest()
    return result

def is_valid_credentials(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    password_hash = hash_given(password)
    
    result = c.execute("""
              SELECT *
              FROM users
              WHERE username=? AND
              password_hash=?
              """,(username, password_hash)).fetchone()

    return result is not None

# def is_valid_credentials(username, password):
#     """
#     Returns true if username and password credentials are valid.
#     Returns false otherwise.
#     for use with config file

#     Parameters
#     ----------
#     username : string
#         True if in key of VALID_CREDENTIALS
#     password : string
#         True if in value if VALID_CREENTIALS

#     Returns
#     -------
#     Darkest Secret if true, access denied else

#     """
#     for users in VALID_CREDENTIALS:
#         #see if username is in credential dictionary
#         if username == users:
#             #if found, check if password matches
#             if VALID_CREDENTIALS[users] == hash_given(password):
#                     return True

            
                       
    

        
                
'''
--------------
data structures
'''

if __name__ == "__main__":
    # hash_passwords()
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")
    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
        print("NOW, TIME FOR THE SECRET")
        print("I don't like dogs that much")
        
    else:
        print("ACCESS DENIED")