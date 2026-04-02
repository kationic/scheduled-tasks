import datetime as dt
import pandas as pd
import random
import smtplib
import os

my_email = "os.environ.get("my_email")"
my_password = "os.environ.get("my_password")"

current = dt.datetime.now()
current_month = current.month
current_day = current.day

birthdays_df = pd.read_csv('birthdays.csv')
birthdays = birthdays_df.to_dict('records')

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthday_persons = []

for birthday in birthdays:
    if current_month == birthday["month"] and current_day == birthday["day"]:
        birthday_persons.append({"name": birthday["name"], "email":birthday["email"]})


chosen_letter_template = random.choice(letters)

with open(f"letter_templates/{chosen_letter_template}", "r") as f:
    old_letter = f.read()

    for names in birthday_persons: #names is a dictionary inside a list
        new_letter = old_letter.replace("[NAME]", names["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(from_addr=my_email, to_addrs=names["email"], msg = f"Subject: It's your birthday!\n\n{new_letter}")

