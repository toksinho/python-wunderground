import requests
import sys


def parse_data(key, forecast, city, state):
    
    
    try:
            
        json_data = requests.get("http://api.wunderground.com/api/"+key+"/"+forecast+"/q/"+state+"/"+city+".json")
        json = json_data.json()
        return json
    
    except requests.exceptions.ConnectionError as e:
        print type(e)
        print "Check your network connection!"
        sys.exit(1)
