#http://api.openweathermap.org/data/2.5/weather?q=Ostrava,cz&APPID=tvujklic
#You will need to find your particular city ID number and put it in the two URLs Below
# search for your city by name on this site:
#http://openweathermap.org/help/city_list.txt

import urllib2
import json
def gettemp():
    """ call openweathermap api"""
    response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Ostrava,cz&APPID=tvujklic') #put your city ID number at the end
    mydata = response.read()
    return mydata
 
weather = gettemp()
w = json.loads(weather)

#CURRENT TEMPERATURE
#print w['main']['temp'] #in kelvin
temperature = float(w['main']['temp'])
temperature = ((temperature - 273) ) #convert from kelvin to Farenheit
print ("Current Temp:")
print (round(temperature))

####################################################################
