import time
from datetime import datetime


def timestamp_using_time():
    return time.time()

def timestamp_using_datetime():
    current_time = datetime.now()
    return current_time.timestamp()

def custom_timestamp(date_string):
    dt_format = datetime.strptime(date_string, '%d.%m.%Y %H:%M:%S')
    return dt_format.timestamp()

def convert_timestamp(time_stamp):
    return datetime.fromtimestamp(time_stamp)


#print("Timestamp using time:", timestamp_using_time())
#print("Timestamp using datetime:", timestamp_using_datetime())
#print("The date and time is:", convert_timestamp(timestamp_using_time()))
#print("The date and time is:", convert_timestamp(timestamp_using_datetime()))
print("23.02.2021 09:12:00 ->", custom_timestamp("23.02.2021 09:12:00"))