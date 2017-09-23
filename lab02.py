# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 13:37:16 2017

@author: user
"""
# Reyes Ceballos
#  NWS Wind Chill Temperature (WCT) index


# Question 1
#list of temp's and wind speeds

Tair = [10.0, 0.0, -10.0]
Vwind = [15, 25, 35]

# Twc = 35.74 + 0.6215 * Tair - 35.75 * Vwind ** 0.16 + 0.4275 * Tair * Vwind ** 0.16

#Question 2
#user enters air temperature and wind speed. user receives the wind chill index

for x in range(3):
    Twc = 35.74 + 0.6215 * Tair[x] - 35.75 * Vwind[x] ** 0.16 + 0.4275 * Tair[x] * Vwind[x] ** 0.16
    print('\nTemperature (degrees F): ', Tair[x],)
    print('Wind speed (MPH) :  ', Vwind[x])
    print('Wind Chill Temperature Index : ', Twc)

    
Tair1 = float(input('Please enter the Air temp : '))   
Vwind1 = float(input('Please enter the Wind speed : '))
print('Wind Chill Temperature Index : ', Twc)
    
    
