import sys
import csv
from opencage.geocoder import OpenCageGeocode

key = '5a88f4a37fc744678ad049d7bb869bf1'
geocoder = OpenCageGeocode(key)
addressfile = 'add_file.txt'

try:
    with open("/home/chen/PycharmProjects/part1_no_dups.txt", 'r') as f:
        with open('/home/chen/PycharmProjects/addr1.csv', 'w') as new_f:
            writer = csv.writer(new_f)
            writer.writerow(["Latitude", "Longitude", "Name"])
            for line in f:
                address = line.strip()
                result = geocoder.geocode(address, no_annotations='1')
                if result and len(result):
                    longitude = result[0]['geometry']['lng']
                    latitude = result[0]['geometry']['lat']
                    writer.writerow([latitude, longitude, address])
                else:
                    sys.stderr.write("not found: %s\n" % address)
except IOError:
    print('Error: File %s does not appear to exist.' % addressfile)




try:
    with open("/home/chen/PycharmProjects/part2_no_dups.txt", 'r') as f:
        with open('/home/chen/PycharmProjects/addr2.csv', 'w') as new_f:
            writer = csv.writer(new_f)
            writer.writerow(["Latitude", "Longitude", "Name"])
            for line in f:
                address = line.strip()
                result = geocoder.geocode(address, no_annotations='1')
                if result and len(result):
                    longitude = result[0]['geometry']['lng']
                    latitude = result[0]['geometry']['lat']
                    writer.writerow([latitude, longitude, address])
                else:
                    sys.stderr.write("not found: %s\n" % address)
except IOError:
    print('Error: File %s does not appear to exist.' % addressfile)




try:
    with open("/home/chen/PycharmProjects/part3_no_dups.txt", 'r') as f:
        with open('/home/chen/PycharmProjects/addr3.csv', 'w') as new_f:
            writer = csv.writer(new_f)
            writer.writerow(["Latitude", "Longitude", "Name"])
            for line in f:
                address = line.strip()
                result = geocoder.geocode(address, no_annotations='1')
                if result and len(result):
                    longitude = result[0]['geometry']['lng']
                    latitude = result[0]['geometry']['lat']
                    writer.writerow([latitude, longitude, address])
                else:
                    sys.stderr.write("not found: %s\n" % address)
except IOError:
    print('Error: File %s does not appear to exist.' % addressfile)
# Your rate limit has expired. It will reset to 2500 at midnight UTC timezone
# Upgrade on https://opencagedata.com/pric
