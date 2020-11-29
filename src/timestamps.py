timestamps = []
def create_timestamps():
    date_day = range(26, 27+1)
    time_seconds = 22
    time_minutes = range(0, 60)
    time_hours = range(0, 24)
    for d in date_day:
        for h in time_hours:
            for m in time_minutes:
                if len(str(h)) == 1:
                    opt_h = '0' + str(h)
                else:
                    opt_h = h
                if len(str(m)) == 1:
                    opt_m = '0' + str(m)
                else:
                    opt_m = m
                timestamps.append(f'2020-11-{d} {opt_h}:{opt_m}:{time_seconds}')
    timestamps[315:-663]

def get_timestamp(count):
    return timestamps[315+count]
