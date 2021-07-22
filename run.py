import requests
from decouple import config
from plyer import notification
import smtplib, ssl
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

port = 465

if __name__ == "__main__":
    # Request two days of data (today and tomorrow) from openweather at the location used in environmental variables.
    weather_response = requests.get(
        'https://api.openweathermap.org/data/2.5/onecall'+
        f"?lat={config('LATITUDE')}" +
        f"&lon={config('LONGITUDE')}" +
        "&units=imperial" +
        "&cnt=2" +
        f"&APPID={config('OPEN_WEATHER_API')}"
        )
    # Access the second day temperatures and the associated maximum
    maxtemp = weather_response.json()['daily'][1]['temp']['max']

    notification.notify(
        title="Weather Alert",
        message=f"Tomorrow's max temp is {maxtemp}F",
        timeout=10
    )

    driver.get('https://www.airnow.gov/?city=Bellevue&state=WA&country=USA')
    soup = BeautifulSoup(driver.page_source, "html.parser")
    print(soup.prettify())
    #day_one_div = soup.find(id='day-1')
    #print(day_one_div.prettify())
    #driver.quit()
    #print(day_one_div.prettify())
    #aqi_class = day_one_div.find(class_="day-aqi-value")
    #print(aqi_class['title'])
    #nextDay = soup.findall(id='day-1')
    #print(nextDay)

    suggestions = ""
    if maxtemp > 72:
        suggestions += "Make sure to open the windows and run the fans."

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(config('EMAIL_USER'), config('EMAIL_PASS'))
        server.sendmail(config('EMAIL_USER'), config('MAIN_EMAIL'), f"Subject: MaxTemp: {maxtemp}F\n\n{suggestions}")
