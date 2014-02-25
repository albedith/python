'''
Created on Feb 24, 2014

@author: albedith
'''


speed_of_light = 300000. # km per second

def speed_fraction(ms,km):
    #returns speed data travels as a decimal fraction of speed of light
    speed_of_data = (km)/(ms*1000.) #km/s round-trip
    speed_of_data = (speed_of_data/2.) # one-way

    result = speed_of_data/speed_of_light
    return result




print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?