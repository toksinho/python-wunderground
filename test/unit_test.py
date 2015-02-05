from wunderground import *
import unittest
import time
import datetime

class TestFunctions(unittest.TestCase):

    def setUp(self):
        APIkey="put your api key here"
        self.conditions = Conditions(APIkey,"zagreb","croatia")
        self.forecast = Forecast(APIkey,"zagreb","croatia")
        self.astronomy = Astronomy(APIkey,"zagreb","croatia")
   
        

    #check if day from Conditions same as today
    def test_conditions_day(self):
        self.today = self.conditions.date()
        self.today = self.today[:3]
        self.assertEqual(self.today,time.strftime("%a"))


    def test_conditions_humidity(self):
        humidity = self.conditions.humidity()
        humidity = humidity[:2]
        self.assertTrue(humidity>0,'humidity must be greather than 0')


    def test_conditions_wind_speed(self):
        wind_speed = self.conditions.wind_speed()
        self.assertTrue(wind_speed>=0,'wind speed must be greather or equal to 0')

    #check does 8th day is Sunday
    def test_forecast_is_day(self):
        some_day=self.forecast.weekday(8)
        weekday=datetime.date(2015,2,8)     
        self.assertEqual(some_day,weekday.strftime("%A"))

    #take sunrise from some other weather website and check is it equal
    # to the sunrise from  wunderground data
    def test_astronomy_sunrise(self):
        sunrise = "7:13"
        self.assertEqual(sunrise,self.astronomy.sunrise())
        
if __name__=='__main__':
    unittest.main()
