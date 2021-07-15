import requests
from decouple import config

if __name__ == "__main__":
    # Request two days of data (today and tomorrow) from openweather at the location used in environmental variables.
    response = requests.get('https://api.openweathermap.org/data/2.5/onecall'+
        f"?lat={config('LATITUDE')}" +
        f"&lon={config('LONGITUDE')}" +
        "&units=imperial" +
        "&cnt=2" +
        f"&APPID={config('OPEN_WEATHER_API')}"
        )
    # Access the second day temperatures and the associated maximum
    maxtemp = response.json()['daily'][1]['temp']['max']
    print(f"Tomorrow's max temp is {maxtemp}F")
