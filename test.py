import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(s)
server = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=ed8d552708ddfec051327961892c9ee3"
port = 80

request = "GET /data/2.5/weather?q=CITY&APPID=KEY&units=metric HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n"

s.connect((server,port))
s.sendall(b"hello")
result = s.recv(4096)
print(repr(result))