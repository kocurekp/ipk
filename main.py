import sys			
import socket
import json

try:
	KEY=sys.argv[1]
	CITY=sys.argv[2]
except IndexError as e:
	print(e)
	exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "api.openweathermap.org" 
port = 80

request = "GET /data/2.5/weather?q="+CITY+"&APPID="+KEY+"&units=metric&munit HTTP/1.1\r\nHost: "+server+"\r\n\r\n"

try:
	s.connect((server,port))			# try connecting to http server
except socket.error as e:
	print(e)
	exit()

s.send(request.encode())				# send request
result = s.recv(4096)					# store received data

httpStatus = ((result.split('\n', 1)[0]).split(" ", 2)[1])		# get http status from first line
httpError = ((result.split('\n', 1)[0]).split(" ", 1)[1])	 

if httpStatus != "200":		#not successfull print error
	print(httpError)
	exit()

jsonReceived = result.split("\r\n\r\n", 1)[-1]				# dump useless data
jsonParse = json.loads(jsonReceived)

speed = 0
deg = 0
msToKmh = 3.6			#convertion

weather = jsonParse["weather"][0]["description"]
temperature = round(jsonParse["main"]["temp"],1)		# round to 1 decimal
humidity = jsonParse["main"]["humidity"]
pressure = jsonParse["main"]["pressure"]

try:
	windSpeed = round((jsonParse["wind"]["speed"])*msToKmh,2)		#take care of missing values
except KeyError:
	speed = 1

try:
	windDeg = jsonParse["wind"]["deg"]
except KeyError:
	deg = 1

degreeSign= u'\N{DEGREE SIGN}'
														#print processed data
print("-----------------------------------")
print("City:\t\t" + CITY)
print("Weather:\t" + weather)
print("Temperature:\t" + str(temperature)+ " " + degreeSign + "C")
print("Humidity:\t" + str(humidity) + " %")
print("Pressure:\t" + str(pressure) + " hPa")

if (speed == 0):
	print("Wind Speed:\t" + str(windSpeed) + " km/h")
else:
	print("Wind Degree:\t0" + " km/h")

if (deg == 0):
	print("Wind Degree:\t" + str(windDeg) + degreeSign)
else:
	print("Wind Degree:\t0" + degreeSign)

print("-----------------------------------")