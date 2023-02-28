import requests
from datetime import datetime
from smtplib import SMTP_SSL
import time

MY_EMAIL = 'devmailbox27@gmail.com'
PASSWORD = "missinghell"
MY_LAT = 12.837463
MY_LONG = 77.647598

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True

def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    #we need to compare sunrise time and sunset time with time now so that we can tell its sunrise or sunset
    #print(sunrise.split("T")[1].split(":")[0])    --- we can use this two line to the above result directly, remove the comment and run to get the exact explanation
    #print(sunset.split("T")[1].split(":")[0])

    #below will give the current time
    time_now = datetime.now().hour
    #print(time_now)
    if time_now <= sunset or time_now >= sunrise:
        return True

while True:
    if is_iss_overhead() and is_night():
        with SMTP_SSL("smtp.gmail.com", port=465) as connection:
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="devmailbox27@gmail.com", msg=f"Subject:ISS is overhead\n\nInternation Space station is above you!")
    time.sleep(60)