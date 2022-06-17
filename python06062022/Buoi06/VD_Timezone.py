from datetime import datetime
import pytz

zones = pytz.all_timezones
print(zones)

newYorkTz = pytz.timezone("America/New_York")
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")
print(timeInNewYork)
print(currentTimeInNewYork)
vn_time = datetime.now(pytz.timezone("Asia/Ho_chi_minh"))
print(vn_time)
print(datetime.now(pytz.timezone('UTC')))