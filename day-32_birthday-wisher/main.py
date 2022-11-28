import smtplib
import random
import pandas
import datetime as dt

today = dt.datetime.today()
month = today.month
day = today.day

data = pandas.read_csv("birthdays.csv")
df = pandas.DataFrame(data)

today_list = [[row.name_of_person, row.email] for (index, row) in df.iterrows() if row.month == month
              and row.day == day]
print(today_list)

from_mail = "<your_mail>"
password = "<your_password>"
for i in today_list:
    a = random.randint(1, 3)
    with open(f"letter_templates/letter_{a}.txt") as letter_file:
        data = letter_file.read()
        replaced_string = data.replace("[NAME]", i[0])
        mail = i[1]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(from_mail, password)
        connection.sendmail(from_addr=from_mail, to_addrs=mail,
                            msg=f"Subject: Happy Birthday!\n\n{replaced_string}")

# today_list = []
# for (index, row) in df.iterrows():
#     if row.month == month and row.day == day:
#         new_list = [row.name, row.email]


# with open("birthdays.csv") as file:
#     data = pandas.read_csv(file)
#     df = pandas.DataFrame(data)






