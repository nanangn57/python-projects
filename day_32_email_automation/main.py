import smtplib
import json

with open("config.json", "r") as f:
    config = json.load(f)

my_email = config['email']
pw = config['password']

# simple mail transfer protocol
with smtplib.SMTP("smtp.gmail.com") as connection:
    # secure the connection
    connection.starttls()
    # login
    connection.login(user=my_email, password=pw)
    connection.sendmail(from_addr=my_email,
                        to_addrs="anhnguyen.workmail@gmail.com",
                        msg="Subject:Hello again\n\n"
                            "This is the body of my email")
