from sense_hat import SenseHat
import time
import subprocess

s = SenseHat()

highHum = 38
highTemp = 35
g = (0, 255, 0)
r = (255, 0, 0)
b = (0, 0, 255)
mix = [
    r, r, r, r, b, b, b, b,
    r, r, r, r, b, b, b, b,
    r, r, r, r, b, b, b, b,
    r, r, r, r, b, b, b, b,
    r, r, r, r, b, b, b, b,
    r, r, r, r, b, b, b, b,
    r, r, r, r, b, b, b, b,
    r, r, r, r, b, b, b, b
]

s.clear(g)

#change loop to while true when done testing, get rid of all message (msg) variables if not using webpage
#while True:
for x in range (0,2000):
    humidity = round(s.humidity, 2)
    temp = round(s.temp, 2)
    msg = "The temp and humidity are operating at optimal levels"
    if (humidity > highHum or temp > highTemp):
        if (humidity > highHum and temp > highTemp):
            sense.set_pixels(mix)
            msg = "<span style='color:red'>Temp</span> and <span style='color:blue'>Humidity</span> are high"
        elif (temp > highTemp):
            s.clear(r)
            msg = "<span style='color:red'>Temp</span> is high"
        elif (humidity > highHum):
            s.clear(b)
            msg = "<span style='color:blue'>Humidity</span> is high"
        subprocess.call("sshpass -p raspberry ssh pi@192.168.221.188 'python3 /home/pi/picademymotor2.py'", shell=True)#change ip as needed
    else:
        s.clear(g)
    print(humidity)
    print(temp)
    
    #this section creates a webpage every iteration, you will need to change the url and give pi ownership of www
    file = "/var/www/html/index.php"; 
    f = open(file, 'w+');
    Data = "<html><head><meta http-equiv='refresh' content='5; URL=http://192.168.210.240'></head><body><h1>"+msg+"</h1><br><br><h2>Temp: "+str(temp)+" Celsius</h2><br><br><h2>Humidity: "+str(humidity)+"%</h2></body></html>"; 
    f.write(Data);
    f.close(); 
