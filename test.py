import datetime
import os
import time
import pytz
from django.utils.timezone import localtime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


def format_duration(duration):
    hours = int(duration.total_seconds() // 3600)
    minutes = int(duration.total_seconds() % 3600 // 60)
    if hours == 0:
        return "{} мин".format(minutes)
    else:
        return "{} ч {} мин".format(hours, minutes)


print("datetime.datetime.now():", datetime.datetime.now())
print("time.localtime():", time.localtime())
delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(0)
print("delta:", delta)
delta2 = datetime.timedelta(minutes=1000, hours=0)
print("format_duration(delta):", format_duration(delta))
print("format_duration(delta2):", format_duration(delta2))

# print(datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc))
# print(datetime.datetime.fromtimestamp(0))
# tz_moskva = datetime.timezone(datetime.timedelta(hours=3))
# print(datetime.datetime.fromtimestamp(0, tz=tz_moskva))
#
#
# print(localtime())
# print(localtime(timezone=pytz.timezone('Asia/Yekaterinburg')))
