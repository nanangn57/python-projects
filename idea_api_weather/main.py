import weather
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == "__main__":

    with open("..\config.json", "r") as f:
        config = json.load(f)['auto_mail']

    my_email = config['email']
    pw = config['password']

    # Get today weather
    today_weather = weather.get_today_weather()
    work_hour_df = today_weather[(today_weather['date_hour'] >= 8) & (today_weather['date_hour'] <= 20)]

    if sum(work_hour_df['precipitation_probability'].apply(weather.rain_alert)) > 0:
        hour_rain = list(work_hour_df[work_hour_df['precipitation_probability'] > 60]['date_hour'])
        hour_rain = [str(round(hour, 0))+"h" for hour in hour_rain]

        min_temp = round(work_hour_df['temperature_2m'].min(), 0)
        max_temp = round(work_hour_df['temperature_2m'].max(), 0)

        msg = MIMEMultipart()
        msg['From'] = my_email
        recipients = ["anhnguyen.workmail@gmail.com", "HoangOda@gmail.com"]
        msg['To'] = ", ".join(recipients)

        msg['Subject'] = "Dự báo hôm nay trời mưa"
        body = f"Hôm nay trời sẽ mưa vào những khung giờ sau: {', '.join(hour_rain)}.\n\n" \
               f"Hãy nhớ mang áo mưa và đóng cửa sổ khi ra ngoài. " \
               f"Nhiệt độ trung bình từ {min_temp}°C đến {max_temp}°C.\n\n Have a nice day"

        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Send the email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()  # Secure the connection
                connection.login(my_email, pw)
                connection.send_message(msg)
                print('Email sent successfully!')
        except Exception as e:
            print(f'Error: {e}')