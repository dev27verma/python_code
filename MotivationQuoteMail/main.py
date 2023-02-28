from smtplib import SMTP_SSL
from datetime import datetime
from random import choice

MY_EMAIL = "devmailbox27@gmail.com"
MY_PASSWORD = "replace the password"
TO_EMAIL = "vinodkumar_0990@ymail.com"

weekday = datetime.now().weekday()
print(weekday)

if weekday == 0:
    with open("quotes.txt", "r") as quote_file:
        all_quote = quote_file.readlines()
        quote = choice(all_quote)

    with SMTP_SSL(host="smtp.gmail.com", port=465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
