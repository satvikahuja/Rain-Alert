import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "open weather API KEY"
account_sid = "twillo API "
auth_token = "Twillo auth key"
#12.8230
#80.0444
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

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain⛈️ today. Remember to bring an Umbrella☔️🌈",
        from_="+12567276831",
        to="+917483976127"
    )
    print(message.status)


