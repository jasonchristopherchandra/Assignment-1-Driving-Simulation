
initialVelocity=-0

Time = int(input("Please enter time spent on the road."))

while Time<0:
    print("Error,time spent can't be below 0.")
    Time = int(input("how much time did you spend on the road"))

Acceleration = int(input("Please enter acceleration."))    #acceleration is (Final Velocity - Initial Velocity) over Time.

while Acceleration<0:
    print("Error,Acceleration can't be below 0")
    Acceleration = int(input("How much was your Acceleration ?"))

Distance = int(input("Please enter distance you want to travel."))

while Distance < 0:
     print("Error,Distance Travelled can't be below 0")
     Distance = int(input("Please enter distance you want to travel."))


speedlimit = 60

maxVelocity = Acceleration * Time

if maxVelocity > speedlimit:
    print("User went over the speed limit. Maximum speed was:", maxVelocity)

else: print("User did not go over the speed limit. Maximum speed was:", maxVelocity)

for j in range (Time + 1):
    z = (Acceleration/2)*(j**2)
    print("Duration: ",j, " Distance: ",'*' * int(z/10))

if maxVelocity>Distance:
    print("You have reached your destination.")
    print("Your maximum speed was: " , int(maxVelocity) , "m")
else  :
    print("You did not reach your destination.")
    print("Your maximum speed was:" , int(maxVelocity) , "m")



