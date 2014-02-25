'''
Created on Feb 24, 2014

@author: albedith
'''
import converting_seconds

def convert_to_Mb(num,unit):
    num = float(num)
    if unit == 'kb':
        num = num / 1000 #converting kb to Mb
    elif unit == 'kB':
        num = (num * 8)/ 1000 #converting kb to Mb
    elif unit == 'Mb':
        num = num
    elif unit == 'MB':
        num = num * 8  #converting MB to Mb
    elif unit == 'Gb':
        num = num * 1000 #converting Gb to Mb
    elif unit == 'GB':
        num = (num*8) * 1000  #converting GB to Mb
    elif unit == 'Tb':
        num = num * 1000000  #converting Tb to Mb
    elif unit == 'TB':
        num = (num*8) * 1000000 #converting TB to Mb
    else:
        return "invalid unit"

    return num

def download_time(file_size, file_unit, bandwidth, bandwidth_unit):
    file_Mb = convert_to_Mb(file_size,file_unit)
    bandwidth_Mb = convert_to_Mb(bandwidth, bandwidth_unit)
    download_secs = file_Mb/bandwidth_Mb
    result = converting_seconds.convert_seconds(download_secs)

    return result





print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


