import time

ticks=time.time()
print("Number of ticks:",ticks,"\n\n")

Localtime=time.localtime(time.time())
print("Local time is:",Localtime,"\n\n")

currentime=time.asctime(time.localtime(time.time()))

print("Formatted time is :",currentime,"\n\n")