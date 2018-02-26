#!/usr/bin/env python

# Draws heavily on
# https://stackoverflow.com/a/2888042

import csv, sqlite3, sys, os.path

arg_count = len(sys.argv)
if arg_count != 2:
    print "Must pass geoip filename"
    sys.exit(-1)

filename = sys.argv[1]
if not os.path.isfile(filename):
    print "Could not find file named %s"%(filename)
    sys.exit(-1)

con = sqlite3.connect("geoip.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS geo_ip_country;")
cur.execute("CREATE TABLE geo_ip_country (start_ip, end_ip, numeric_start_ip, numeric_end_ip, country_code, country_name);") # use your column names here

with open(filename,'rb') as fin: # `with` statement available in 2.5+
# csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin, fieldnames=['start_ip', 'end_ip', 'numeric_start_ip', 'numeric_end_ip', 'country_code', 'country_name']) # comma is default delimiter
    to_db = [(i['start_ip'], i['end_ip'], int(i['numeric_start_ip']), int(i['numeric_end_ip']), i['country_code'], i['country_name']) for i in dr]

    cur.executemany("INSERT INTO geo_ip_country (start_ip, end_ip, numeric_start_ip, numeric_end_ip, country_code, country_name) VALUES (?, ?, ?, ?, ?, ?);", to_db)
    con.commit()
    con.close()
