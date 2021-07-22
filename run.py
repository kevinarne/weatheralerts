import requests
from decouple import config
from plyer import notification
import smtplib, ssl
import datetime

port = 465

if __name__ == "__main__":
    # Request two days of data (today and tomorrow) from openweather at the location used in environmental variables.
    weather_response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall"+
        f"?lat={config('LATITUDE')}" +
        f"&lon={config('LONGITUDE')}" +
        "&units=imperial" +
        "&cnt=2" +
        f"&APPID={config('OPEN_WEATHER_API')}"
        )
    # Access the second day temperatures and the associated maximum
    maxtemp = weather_response.json()['daily'][1]['temp']['max']

    suggestions = ""
    if maxtemp > 72:
        suggestions += "Make sure to open the windows and run the fans.\n"

    air_response = requests.get(
        "https://www.airnowapi.org/aq/forecast/zipCode/"+
        "?format=JSON"+
        f"&zipCode={config('ZIPCODE')}"+
        f"&date={(datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')}"+
        f"&API_KEY={config('AIR_NOW_API')}"
        )

    air_quality = air_response.json()[0]['Category']['Name']

    if air_quality != "Good":
        suggestions += "Run air filter and keep windows closed. If ventilation needed, try placing filters over windows.\n"

    notification.notify(
        title="Weather Alert",
        message=
            f"Tomorrow's max temp is {maxtemp}F\n" +
            f"Expected air quality: {air_quality}",
        timeout=10
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(config('EMAIL_USER'), config('EMAIL_PASS'))
        server.sendmail(config('EMAIL_USER'), config('MAIN_EMAIL'), f"Subject: Max Temp: {maxtemp}F Air Quality: {air_quality}\n\n{suggestions}")
