# Description
Quick and dirty script to give me a heads up that I need to prepare for weather problems in the next day. In particular, overly warm, smoggy, and rainy days are of interest. It pulls data from the Open Weather API and Air Now API. Windows Notifications are sent (the script is intended to be scheduled) and an email is sent from EMAIL_USER to MAIN_EMAIL with the next day's forecast.

# Current State
The script will email the maximum temperature and air quality rating to the user with limited suggestions in the body of the email. Notifications are also sent on Windows, though this will likely be removed in future versions to increase portability.

# Setup
## Email
You will need an email account setup to allow access via SMTP. In Gmail, this will require you to allow access to less secure access methods. For security purposes you should set up a disposable email to use for this instead of your main one.

## APIs
Both of the APIs you will need for this are free, though they have daily usage limits. Using this script once a day will keep you from getting anywhere close to those limits.
### Open Weather API
This is where we get our temperature data. [Click here to register](https://home.openweathermap.org/users/sign_up) Once you have signed up, you should be  able to find your API key from your account page.
### Air Now API
This is where we get our air quality data. [Click here to request an API account](https://docs.airnowapi.org/login) Once you have signed up, you should be  able to find your API key from your account page.


## Environmental Variables
This script makes use of the decouple library for storing credentials and personal information. In order for it to work for you, you'll need to define each of the following in a file named .env in the root directory of your project. I recommend using a code editor like Sublime Text or Atom to create this file as other text editors often add hidden file extensions.
* LATITUDE
* LONGITUDE
* ZIPCODE
* OPEN_WEATHER_API
* AIR_NOW_API
* EMAIL_USER
* EMAIL_PASS
* MAIN_EMAIL
* COMFY_TEMP

## Modules to Install
* python-decouple
* requests
* plyer
* datetime
* smtplib
* ssl
