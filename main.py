import time
def datetime_timestamp(dt):
    try:
        t  = time.strptime(dt, '%Y-%m-%d %H:%M:%S')
        year = t.tm_year
        if(year>2020 or year < 1900):
            return -1
        s = time.mktime(t)
    except Exception:
        return -1
    return int(s)
if __name__ == '__main__':
    while(True):
        dts = input("Enter a datetime like YYYY-MM-DD HH:MM:SS(year is between 1900 and 2020)\n")
        # dts = '2012-03-28 06:55:40'
        d = datetime_timestamp(dts)

        if(d != -1):
            print('timestamp', d)
            print('datetime', dts)
            break
        else:
            print('invalid input')
