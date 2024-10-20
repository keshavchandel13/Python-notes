# Time elasped since you born
import time
current_time = time.time()
# print(current_time)

birth_year = int(input("Enter your birth year"))
birth_month = int(input("Enter your birth month"))
birth_day = int(input("Enter your birth date"))

structured_time = time.struct_time((birth_year,birth_month,birth_day,0,0,0,0,0,0))
# structured_time = time.localtime(birth_year)
print(structured_time)
time_in_seconds = time.mktime(structured_time)
seconds_till_now = current_time - time_in_seconds
time_elasped_in_days = seconds_till_now/(24*3600)
time_elasped_in_hrs = seconds_till_now/(3600)
print("Days: ",int(time_elasped_in_days))
print("hrs: ",int(time_elasped_in_hrs))