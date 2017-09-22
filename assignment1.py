initialVelocity=-0

Time = float(input("Please enter time spent on the road."))

while ( Time < 0):
    print("Error,time spent can't be below 0.")
    Time = float(input("how much time did you spend on the road"))

Acceleration = float(input("Please enter acceleration."))    #acceleration is (Final Velocity - Initial Velocity) over Time.

while (Acceleration < 0):
    print("Error,Acceleration can't be below 0")
    Acceleration = float(input("How much was your Acceleration ?"))

Distance = float(input("Please enter distance travelled."))

while (Distance < 0):
    print("Error,Distance Travelled can't be below 0")
    Distance = float(input("Please enter distance travelled."))

speedlimit = 60

maxVelocity = Acceleration * Time

if (maxVelocity > speedlimit):
    print("User went over the speed limit. Maximum speed was:",maxVelocity)

else: print("User did not go over the speed limit. Maximum speed was:",maxVelocity)


