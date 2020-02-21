# The client for OpenWeatherMap API
---

## Description

The client obtains selected information from a data source via HTTP queries.
For free access is required to register at
[OpenWeatherMap](https://openweathermap.org/),
where is obtained so-called *"API key"* which is further used in authentication queries.

The application was written in Python because of its simplicity and uses following libraries:

```
* sys - Used for retrieving input data from params
* socket - Provides access to the BSD socket interface
* json - Helps with extracting selected parts from recieved data
```

### Installation

Application is build via Makefile and requires to be launched using following parametres:

>make run api_key=\<API key> city=\<City>

### Error Codes

* 400 Bad Request - Server cannot process the request due to an client error
* 401 Unauthorized - Authentication has failed
* 403 Forbidden - Request is valid, but the server is refusing action
* 404 Not Found - The requested resource could not be found

### Preview

```
City:           Brno
Weather:        clear sky
Temperature:    -2.4 °C
Humidity:       42 %
Pressure:       1043 hPa
Wind Speed:     18.36 km/h
Wind Degree:    10°
```