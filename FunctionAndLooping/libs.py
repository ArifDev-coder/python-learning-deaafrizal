from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from db_region import region


def welcome(name):
    message = f"Welcome to Function and Looping {name}"
    return message

def helo(region_name):
    try:
        reg = region(region_name)
        dtnw = datetime.now(tz=ZoneInfo(reg))

        message = f"Hello World! Today is {dtnw} in {reg}           ( Ctr + C for Exit )"
        return message
    except:
        return "Unknow Region"
    