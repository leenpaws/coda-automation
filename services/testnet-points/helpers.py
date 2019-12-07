import time
from datetime import datetime
import pytz

def date_in_window(date, window):
    start_time = window[0]
    end_time = start_time + window[1]
    #test_time = datetime.fromtimestamp(int(date[:-3]), tz=pytz.timezone('Etc/UTC'))
    test_time_unaware = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S GMT')
    test_time = pytz.timezone('Etc/UTC').localize(test_time_unaware).replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/Los_Angeles'))
    
    test1 = start_time < test_time 
    test2 = test_time < end_time
    
    if test1 and test2:
        print(f"Testing Block -- Start: {start_time}, End: {end_time} -- Block Time: {test_time} -- {test1}, {test2}")
    return start_time < test_time and test_time < end_time


def in_range(date, window_times):
    return True in [ date_in_window(date, window) for window in window_times ]