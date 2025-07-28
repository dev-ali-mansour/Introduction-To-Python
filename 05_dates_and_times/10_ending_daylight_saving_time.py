from datetime import datetime

from dateutil.tz import tz

eastern = tz.gettz('US/Eastern')
# 2017-11-05 01:00:00
first_1am = datetime(2017, 11, 5, 1, 0, 0,
                     tzinfo=eastern)
print(tz.datetime_ambiguous(first_1am))

# 2017-11-05 01:00:00 again
second_1am = datetime(2017, 11, 5, 1, 0, 0,
                      tzinfo=eastern)
second_1am = tz.enfold(second_1am)
print((first_1am - second_1am).total_seconds())

first_1am=first_1am.astimezone(tz.UTC)
second_1am=second_1am.astimezone(tz.UTC)
print((second_1am-first_1am).total_seconds())
