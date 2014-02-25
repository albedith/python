'''
Created on Feb 24, 2014

@author: albedith
'''


def convert_seconds(sec):
    sec_to_minutes = (sec/60)
    num_hours = int(sec_to_minutes//60)
    num_minutes = int(sec_to_minutes%60)
    num_seconds = (sec - (num_hours*3600)-(num_minutes*60))

    if type(num_seconds) == float:
        num_seconds = num_seconds * 1.0

    if num_hours == 1:
        hours = str(num_hours)+' hour'
    else:
        hours = str(num_hours)+' hours'

    if num_minutes == 1:
        minutes = str(num_minutes)+' minute'
    else:
        minutes = str(num_minutes)+' minutes'

    if num_seconds == 1:
        seconds = str(num_seconds)+' second'
    else:
        seconds = str(num_seconds)+' seconds'

    return '%s, %s, %s' % (hours, minutes, seconds)




#print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

#print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

#print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds