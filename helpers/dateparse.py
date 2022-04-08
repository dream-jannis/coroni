from datetime import datetime

def parse(date):
    timestamp = str(date)
    timestamp = timestamp.replace("datetime","")
    timestamp = timestamp.replace(".","")
    timestamp = timestamp.replace("(","")
    timestamp = timestamp.replace(")","")
    timestamp = timestamp.replace(",","")

    timestamp = datetime.strptime(timestamp, '%Y %m %d %H %M')

    return timestamp