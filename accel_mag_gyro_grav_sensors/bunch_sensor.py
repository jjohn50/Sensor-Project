import requests
import json
import matplotlib.pyplot as plt
import urllib

# http://192.168.29.159:8080
# camera_ipaddress:8080/sensors.json
# response = requests.get('http://ip-api.com/json/192.168.29.159:8080').json()
# response = requests.get('http://192.168.29.159:8080/sensors.html').json()
# print(response) #this means it successful for response [200]

url = 'http://192.168.29.159:8080/sensors.json'
response = urllib.request.urlopen(url)
fdata = json.loads(response.read())    


# f = open('sensors.json')
# fdata = json.load(f)
accel = [] 
mag = []
gyro = [] 
gravity = [] 
proximity = []

# print('accel')         
# print(data['accel'])
# accel = data['accel']  
# print(accel['desc'])    
#print(data['accel'])

#Accelerometer Data: 
Ax = []
Ay = []
Az = [] 
accel = fdata['accel']
data = accel['data']
for element in data:
    #print(element[1])
    #print(element[1][0]) #x
    # print(element[1][1]) #y
    # print(element[1][2]) #
    Ax.append(element[1][0])
    Ay.append(element[1][1])
    Az.append(element[1][2])
# print(Ax)
plt.plot(Ax, label="Ax")  
plt.plot(Ay, label="Ay")
plt.plot(Az, label="Az")
plt.legend()
plt.xlabel("Ax,Ay,Az Data (m/s^2)")
plt.ylabel("Change over Change")
plt.title("Accelerometer Graph")
plt.show() 

#magnetic field data
Mx = []
My = []
Mz = [] 
mag = fdata['mag']
data1 = mag['data']
for element in data1:
    #print(element[1][0]) #mx
    #print(element[1][1]) #my
    #print(element[1][2]) #mz
    Mx.append(element[1][0])
    My.append(element[1][1])
    Mz.append(element[1][2])

plt.plot(Mx, label="Mx")  
plt.plot(My, label="My")
plt.plot(Mz, label="Mz")
plt.legend()
plt.xlabel("Mx,My,Mz Data (µT)") 
plt.ylabel("Change over Change")
plt.title("Magnetic Field Graph")
plt.show() 

#light data   
lightA = []
light = fdata['light']
data2 = light['data']
for element in data2:
    #print(element[1][0])
    lightA.append(element[1][0])

plt.plot(lightA)    
plt.xlabel("Light Data (lx)") 
plt.ylabel("Change over Change")
plt.title("Light Graph") 
plt.show()    

# print("proximity")
# proximity = data['proximity']
# print(proximity)
# prox = []
# proximity = fdata['proximity']   
# data3 = proximity['data']
# for element in data3:
#     #print(element[1][0])
#     prox.append(element[1][0])  
# plt.plot(prox)    
# plt.xlabel("Prox Data (cm)") 
# plt.ylabel("Change over Change")
# plt.title("proximity Graph") 
# plt.show()    

# Gravity Pull Data
Gx = []
Gy = []
Gz = [] 
gravity = fdata['gravity']
data4 = gravity['data']
for element in data4:
    Gx.append(element[1][0])
    Gy.append(element[1][1])
    Gz.append(element[1][2])

plt.plot(Gx, label="Gx")  
plt.plot(Gy, label="Gy")
plt.plot(Gz, label="Gz")
plt.legend()
plt.xlabel("Gx,Gy,Gz Data (m/s^2)") 
plt.ylabel("Change over Change")
plt.title("Gravitational Pull Graph")  
plt.show()                                  