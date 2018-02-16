# ublox-agps
Sample how to send A-GPS data from u‑blox to U7 module  

This is a simple exaple on pyton to write a Assist GPS data downloaded from de u-blox serer to out GPS Module.
First we need to get an access tokken. To do go to this web: https://www.u-blox.com/en/assistnow-service-registration-form and summit the form. In 24 hours you will received an a similar menssage to this:

## Get an a tokken

Dear XXXXXX

Thank you for your interest in u-blox' online, globally-available assisted GNSS service, AssistNow.
The service ensures a fast Time-To-First-Fix when using u-blox GNSS receivers, even under poor satellite signal conditions.

The token you will require for initial setup of the service is below.

Token: **XXXXXXXXXX**

A description of the AssistNow features and services can be found on the following web page:

http://www.u-blox.com/en/assisted-gps.html


Kind regards
u-blox

# Configure the script

## Add the token to the script
Go to the PyThon file and replace "<< Your tokken >>" with your tokken

## Set the COM port
Go to the PyThon file and replace "<< Your GPS Module COM port >>" with your tokken. In Debian/Ubuntu Linux the COM port usualy is "/dev/ttyACM0"

# Run the script

`python u-blox_agps.py`

# Original Author
The idea of this project is from: https://gist.github.com/veproza/55ec6eaa612781ac29e7


