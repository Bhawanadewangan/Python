# Python program to find yesterday,
# today and tomorrow


# Import datetime and timedelta
# class from datetime module

from datetime import datetime, timedelta

# Get Today's date
presentday = datetime.now()

# Get Yesterday date
yesterday = presentday-timedelta(1)

# Get Tomorrow date
tomorrow = presentday+timedelta(1)

print("yesterday = ", yesterday.strftime("%d-%m-%y"))
print("today = ", presentday.strftime("%d-%m-%y"))
print("tomorrow = ", tomorrow.strftime("%d-%m-%y"))