from parse import parse_data

class Conditions(object):
    def __init__(self,key,city,state):
        self.key = key
        self.city = city
        self.state = state

               
            
        self.data = parse_data(self.key,"conditions",self.city,self.state)
        self.rjecnik  = {}
            
        if 'error' in self.data["response"]:
            print "Error! Check your API key or city/state name"

        else:

            try:
                
                self.rjecnik['location'] = self.data["current_observation"]["display_location"]["full"]
                self.rjecnik['weather'] = self.data["current_observation"]["weather"]
                self.rjecnik['local time'] = self.data["current_observation"]["local_time_rfc822"]
                self.rjecnik['temperature(C)'] = self.data["current_observation"]["temp_c"]
                self.rjecnik['temperature(F)'] = self.data["current_observation"]["temp_f"]
                self.rjecnik['humidity'] = self.data["current_observation"]["relative_humidity"]
                self.rjecnik['wind direction'] = self.data["current_observation"]["wind_dir"]
                self.rjecnik['wind speed(kph)'] = self.data["current_observation"]["wind_kph"]
                self.rjecnik['pressure'] = self.data["current_observation"]["pressure_mb"]
                self.rjecnik['precipitation(mm)'] = self.data["current_observation"]["precip_today_metric"]

            except  (ValueError, KeyError, TypeError) as e:
                print type(e)
                print "Check is data for that city available"
 
        
  
    def weather(self):
        for k,v in self.rjecnik.items():
            print k,':',v
            
    def condition(self):
        return self.rjecnik['weather']
    
    def date(self):
        return self.rjecnik['local time']
        
    def wind_direction(self):
        return self.rjecnik['wind direction']
     

    def temperature_celsius(self):
        return self.rjecnik['temperature(C)']

    def temperature_fahrenheit(self):
        return self.rjecnik['temperature(F)']

    def wind_speed(self):
        return self.rjecnik['wind speed(kph)']

    def pressure(self):
        return self.rjecnik['pressure']
    
    def humidity(self):
        return self.rjecnik['humidity']
    
    def precipitation(self):
        return self.rjecnik['precipitation(mm)']



class Forecast(object):
    def __init__(self,key,city,state):
        self.key = key
        self.city = city
        self.state = state
        
    
    
            
        self.data = parse_data(self.key,"forecast10day",self.city,self.state)
        self.rjecnik  = {}
            
        if 'error' in self.data["response"]:
              print "Error! Check your API key or city/state name"

        else:
            
            try:
                
                for day in self.data['forecast']['simpleforecast']['forecastday']:
                    if 'day' in day['date']:
                        x=day['date']['day']
                        self.rjecnik[x]=[day['conditions']]
                        self.rjecnik[x].append(day['high']['celsius'])
                        self.rjecnik[x].append(day['high']['fahrenheit'])
                        self.rjecnik[x].append(day['low']['celsius'])
                        self.rjecnik[x].append(day['low']['fahrenheit'])
                        self.rjecnik[x].append(day['qpf_allday']['mm'])
                        self.rjecnik[x].append(day['avewind']['kph'])
                        self.rjecnik[x].append(day['avewind']['dir'])
                        self.rjecnik[x].append(day['avehumidity'])
                        self.rjecnik[x].append(day['date']['weekday'])
                            
            except  (ValueError, KeyError, TypeError) as e:
                print type(e)
                print "Check is data for that city available"
                
       
  
    def ten_day_weather(self):
        for k,v in self.rjecnik.items():
            print k,':',v
            

    def condition(self,day):
        if day in self.rjecnik.keys():
            return self.rjecnik[day][0]
        else:
            print "Day %s doesn't exist!" %day
                
        
    def temperature(self,day):
        if day in self.rjecnik.keys():
            temperature = {}
            temperature['celsius high']=self.rjecnik[day][1]
            temperature['celsius low']=self.rjecnik[day][3]
            temperature['fahrenheit high']=self.rjecnik[day][2]
            temperature['fahrenheit low']=self.rjecnik[day][4]
            return temperature
        else:
            print "Day %s doesn't exist!" %day


    def humidity(self,day):
        if day in self.rjecnik.keys():
            return self.rjecnik[day][8]
        else:
            print "Day doesn't exist!"
        
    def wind(self,day):
        if day in self.rjecnik.keys():
            wind = {}
            wind['direction']=self.rjecnik[day][7]
            wind['speed']=self.rjecnik[day][6]
            return wind
        else:
            print "Day %s doesn't exist!" %day

    def precipitation(self,day):
        if day in self.rjecnik.keys():
            return self.rjecnik[day][5]
        else:
            print "Day %s doesn't exist!" %day

    #just for testing purposes to see is it day in dictionary        
    def weekday(self,day):
        if day in self.rjecnik.keys():
            return self.rjecnik[day][9]
        else:
            print "Day %s doesn't exist!" %day

class Astronomy(object):
    def __init__(self,key,city,state):
        self.key = key
        self.city = city
        self.state = state
        
 
        
       

        
        self.data = parse_data(self.key,"astronomy",self.city,self.state)
        self.rjecnik  = {}
        if 'error' in self.data["response"]:
            print "Error! Check your API key or city/state name"

        else:
            try:
                
                sunset = self.data["sun_phase"]["sunset"]["hour"] + ':' + self.data["sun_phase"]["sunset"]["minute"]
                sunrise = self.data["sun_phase"]["sunrise"]["hour"] + ':' + self.data["sun_phase"]["sunrise"]["minute"]
                self.rjecnik['sunrise'] = sunrise
                self.rjecnik['sunset'] = sunset
                
            except  (ValueError, KeyError, TypeError) as e:
                print type(e)
                print "Check is data for that city available"
                
 

  
    def sunrise(self):
        return self.rjecnik['sunrise']

    def sunset(self):
        return self.rjecnik['sunset']

    
 
    
