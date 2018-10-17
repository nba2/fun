from time import time
seconds = time()
days = int(seconds//(24*60*60))
seconds = seconds%(24*60*60)
hours = int(seconds//(60*60))
seconds = seconds%(60*60)
minutes = int(seconds//60)
if minutes < 10:
    minutes = str(minutes)
    minutes = "0" + minutes
seconds = seconds%60
seconds = int(seconds)
if seconds < 10:
    seconds = str(seconds)
    seconds = "0" + seconds
print("The time is {}:{}:{}, {} days since the epoch.".format(hours,minutes,seconds,days))
