#!/usr/bin/env python

import sqlite3, sys
from socket import inet_aton
from struct import unpack

# http://www.php2python.com/wiki/function.ip2long/
def ip2long(ip_addr):
    return unpack("!L", inet_aton(ip_addr))[0]

arg_count = len(sys.argv)
if arg_count != 2:
    print "Must pass ip address to search"
    sys.exit(-1)

ip_address = sys.argv[1]
ip_as_long = ip2long(ip_address)
print "Searching for ip address %s via long version %d"%(ip_address, ip_as_long)

con = sqlite3.connect("geoip.db")
cur = con.cursor()
for row in cur.execute("SELECT * FROM geo_ip_country WHERE %d BETWEEN numeric_start_ip AND numeric_end_ip" % ip_as_long):
    print row
con.close()
