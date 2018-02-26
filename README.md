# GeoIP import / query tool using sqlite & python 2.x
### https://dev.maxmind.com/geoip/legacy/csv/ for more details on format

* Expects database matching format of: MaxMind GeoIPLite (Legacy) Country CSV database
* Requires:
  - pip install -r requirements.txt (virtualenv or not)
  - wget http://geolite.maxmind.com/download/geoip/database/GeoIPCountryCSV.zip
  - unzip downloaded file
  - run import.py with argument of downloaded filename, generates or refreshes (drop/recreate) database
  - run query.py with argument of IP address and matching row is splatted out
