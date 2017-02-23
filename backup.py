""" Backup and Restore Mongo_DB"""


import datetime
import shutil
import os
import subprocess
import zipfile
import argparse
import logging
import urlparse


__author__ = 'Francis Al Victoriano'
__email__ = 'francis.victoriano@owasp.org'
__version__ = '1.0'
__license__ = 'BSD'

global host
global port
global database

def dump_db(): #Database Name
    #backup_path = '/Users/matt/Documents/mongobackup/'
    print "Default Backup Path =\tC:/database_backups" 
    backup_path = 'C:/database_backups'
    host = str(raw_input("Host: "))
    port = str(raw_input("Port: "))
    database = str(raw_input("Database: "))
    mongoexport_path = 'C:/MongoDB/Server/bin/mongodump'
    now = datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
    this_backup = os.path.join(backup_path, now)
    os.mkdir(this_backup)
    print('Created new backup: %s' % this_backup)

    backup_output = subprocess.check_output(
        [mongoexport_path, 
        '-h', host ,
        '--port', port, 
        '-d', database,
        '-oplog --gzip',
        '--out', this_backup + "/"])

    logging.info(backup_output)

    return
    
def restore_db(): #Database Name
    host = str(raw_input("Host: "))
    port = str(raw_input("Port: "))
    database = str(raw_input("Database: "))
    restore_path  = str(raw_input("Backup Path: "))
    mongoimport_path = 'C:/MongoDB/Server/bin/mongorestore'
    restore_output = subprocess.check_output(
        [mongoimport_path, 
        '-h', host ,
        '--port', port, 
        '-d', database, restore_path + "/" + database])

    logging.info(restore_output)
    return  

def main(): #menu goes here
    opt_list = [dump_db, 
                restore_db]
    
    while(True):            
        print "SELECT OPTION:"
        print "1\tDumb Mongo DB"
        print "2\tRestore Mongo DB"
        opt_choice = int(raw_input("SELECTION: "))
        opt_choice -= 1
        opt_list[opt_choice]()
        
    return

main()