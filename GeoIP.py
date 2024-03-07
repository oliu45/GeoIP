import requests
import sys

if len(sys.argv) != 2:
    print("Expected Arguments: \"geoipimg\" \"IPAddress\"")
    exit()
else:
    ip = sys.argv[1]

access_key = '?access_key=3de4ebda5316500113f20900d15dfe02'

fields = '&fields=latitude,longitude'

geoip_response = requests.get('http://api.ipstack.com/' + ip + access_key + fields)

response_content = geoip_response.json()

latitude = str(response_content['latitude'])

longitude = str(response_content['longitude'])

print('The latitude of the IP Address is ' + latitude)

print('The longitude of the IP Address is ' + longitude)