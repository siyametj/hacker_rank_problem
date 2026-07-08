# time_delta.py 

from datetime import datetime 

def time_delta(t1, t2):
    time_format = "%a %b %d %Y %H:%M:%S %z"

    time1 = datetime.strptime(t1, time_format)
    time2 = datetime.strptime(t2, time_format)

    return str(int(abs((time1 - time2).total_seconds())))

