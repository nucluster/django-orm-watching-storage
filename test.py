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


def is_visit_long(duration, minutes=60):
    if (duration.total_seconds() // 60) > minutes:
        return True
    else:
        return False


print("datetime.datetime.now():", datetime.datetime.now())
delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(0)
print("delta:", delta)
delta2 = datetime.timedelta(minutes=1000, hours=0)
print("format_duration(delta):", format_duration(delta))
print("format_duration(delta2):", format_duration(delta2))
print(delta2.total_seconds() // 60)
print(is_visit_long(delta2))

# print(datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc))
# print(datetime.datetime.fromtimestamp(0))
# tz_moskva = datetime.timezone(datetime.timedelta(hours=3))
# print(datetime.datetime.fromtimestamp(0, tz=tz_moskva))
#
#
# print(localtime())
# print(localtime(timezone=pytz.timezone('Asia/Yekaterinburg')))
