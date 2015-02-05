# python-wunderground

Simple python wrapper around [Weather Underground](http://www.wunderground.com) API


##Requirements

You need API key to use it. 
You can get it for free [http://www.wunderground.com/weather/api/](http://www.wunderground.com/weather/api)


##Usage

```python
>>>import wunderground
>>>weather = Conditions("APIkey","zagreb","croatia")
>>>print weather.condition()
Mostly Cloudy
>>>print weather.temperature_celsius()
2
>>>forecast = Forecast("APIkey","zagreb","croatia")
>>>print forecast.wind(7)
{'direction': u'NNE', 'speed': 14}
>>>weather.temperature(5)
{'celsius low': u'-1', 'celsius high': u'7', 'fahrenheit low': u'31', 'fahrenheit high': u'45'}
>>>weather.humidity(8)
72
>>>astronomy = Astronomy("APIkey","zagreb","croatia")
>>>print weather.sunset()
17:06
```

##Terms of service

[Weather Underground Terms of Service](http://www.wunderground.com/weather/api/d/terms.html)
