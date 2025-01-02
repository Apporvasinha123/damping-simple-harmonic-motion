import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.widgets import TextBox, Button

"""
this program will take a range of inputs and plot the displacement against time 

inputs we will be considering - 

x_0 - initial displacement 
v_0 - initial velocity
c - damping constant
m - mass
k - spring constant

we first have to find out if the discriminant is more than 0, equal to 0 or less than 0
"""

x_0 = float(input("initial displacement (m): "))
v_0 = float(input("initial velocity (ms^-1): "))
c = float(input("damping constant (Nsm^-1): "))
m = float(input("mass (kg): "))
k = float(input("spring constant (Nm^-1): "))
time_end = int(input("how long should the simulation last (seconds): "))


#displacement vs time functions 

def underdamping_x(time, alpha, beta, x_0, v_0):
    inter1 = math.exp(alpha*time)
    inter2 = x_0 * math.cos(beta * time)
    inter3 = (v_0 - (x_0 * alpha))/beta 
    inter3 *= math.sin(beta * time)
    value = inter1 * (inter2 + inter3)
    return value


def criticaldamping_x(time,x_0,v_0,c,m,k):
    inter1 = v_0 + ((c/(2*m)) * x_0 )
    inter2 = math.exp((-c/(2*m))*time)
    value = (inter1 * time) + v_0
    value *= inter2
    return value

def heavydamping_x(time,x_0, v_0, c,m,k):
    a = (2*m*v_0 + x_0*c + x_0*math.sqrt(discriminant))/(2*math.sqrt(discriminant))
    b = x_0/2
    e = -c/(2*m)
    d = math.sqrt(discriminant)/(2*m)
    value = ((a+b) * math.exp((e + d)*time)) - ((a-b)*math.exp((e-d)*time))

    return value

# the discriminant here is c^2 - 4mk

discriminant = c**2 - 4*m*k

damping = ""

if discriminant > 0:
    damping = "heavy damping"
elif discriminant == 0:
    damping  = "critical damping"
else:
    damping  = "under damping"

times = list(np.linspace(0,time_end,1000))
displacements = []

if damping == "under damping":
    alpha  = -(c/(2*m))
    beta  = math.sqrt(-(discriminant))/(2*m)
    for i in times:
        displacements.append(underdamping_x(i, alpha, beta, x_0, v_0))
        
elif damping == "critical damping":
    for i in times:
        displacements.append(criticaldamping_x(i, x_0, v_0, c, m,k))

else:
    for i in times:
        displacements.append(heavydamping_x(i,x_0,v_0, c,m,k))


plt.plot(times, displacements)
plt.grid(True)
plt.title("displacement vs time")
plt.xlabel("time/s")
plt.ylabel("displacement/m")
plt.show()