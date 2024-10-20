import time

epoch_time = time.time()

current_time = time.ctime(epoch_time)
print(current_time)

structured_time = time.localtime()
print(structured_time)

am_pm_time = time.strftime("%I:%M:%S %p",structured_time)
print(am_pm_time)