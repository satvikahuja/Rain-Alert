import tkinter as tk
from tkinter import messagebox
import requests
from twilio.rest import Client


def check_weather_and_send_message():
    OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
    api_key = "openweather api"
    account_sid = "Twillo api"
    auth_token = "twillo api auth key"
    #This is SRM location
    weather_params = {
        "lat": 12.8230,
        "lon": 80.0444,
        "appid": api_key,
        "exclude": "current,minutely,daily"
    }

    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    weather_slice = weather_data["hourly"][:12]
    will_rain = False
    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True

    client = Client(account_sid, auth_token)
    if will_rain:
        message_body = "It's going to rain⛈️ today. Remember to bring an Umbrella☔️🌈"
    else:
        message_body = "It is not going to rain Chill😎☀️"

    message = client.messages \
        .create(
        body=message_body,
        from_="Twillo phone number",
        to="My phone number"
    )
    messagebox.showinfo("Message Status", f"Message sent with status: {message.status}")


window = tk.Tk()
window.title("Weather Alert")

send_msg_button = tk.Button(window, text="Send Message", command=check_weather_and_send_message)
send_msg_button.pack(padx=20, pady=20)

window.mainloop()
