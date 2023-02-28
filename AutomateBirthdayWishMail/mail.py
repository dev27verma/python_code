from datetime import datetime
import pandas
from random import randint
from smtplib import SMTP_SSL

MY_EMAIL = "devmailbox27@gmail.com"
PASSWORD = "missinghell"
'''
dt = datetime.now()
month = dt.month()
day = dt.day()
today_tuple=(month,day)

or the below
'''
today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
'''
birthday_dict = {
    (birthday_month, birthday_day): data_row
}
the below birthday_dict will give the above dictionary
'''
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday\n\n{contents}"
        )
