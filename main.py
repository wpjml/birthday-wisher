import smtplib
import random
import datetime as dt
import pandas

data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")
now = dt.datetime.now()
day = now.day
month = now.month

my_email = "AAAA@gmail.com"
password = "AAAAA"

today_birthday_persons = [birthday_dict[num] for num in range(len(birthday_dict))
                          if birthday_dict[num]["month"] == month and birthday_dict[num]["day"] == day]

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    for _ in range(len(today_birthday_persons)):
        name = today_birthday_persons[_]["name"]
        email = today_birthday_persons[_]["email"]
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file:
            template = file.read()
        letter = template.replace("[NAME]", name)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{email}",
            msg=f"subject:HAPPY BIRTHDAY!!!\n\n{letter}"
        )
