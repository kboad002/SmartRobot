"""
Lab 1- Smart Robot Object-Oriented Design
"""
class ComputerSystem:
    def __init__(self, Software) -> None:
        self._Software = Software
        print("ComputerSystem constructor")

    def gridLocation(self, coordinates):
        self._coordinates = coordinates
        print("location of robot")

    def podLocation(self, coordinates):
        self._coordinates = coordinates
        print("location of pod")

    def batteryLevelDetection(self):    
        print("Detect low level of battery")   

    def systemsCheck(self):
        print("Run a systems check")

    def storeQueue(self):
        print("Queue for remaining pods to transport")

    def communicate(self):
        print("communicate any errors with owner/manufacturer")

"""
Corkscrew to transport pods
"""
class Corkscew:
    def __init__(self, size, weight) -> None:
        self._size = size
        self.weight = weight

    def elevate(self):
        print("elevate pods")

    def spin(self,degrees):
        self._degrees = degrees
        print("robot can spin a certain amount of degrees")

    def descend(self):
        print("descends to drop off pods")     

"""
Power system powers the computer system
"""               
class PowerSystem:
    def __init__(self, BatteryType, BatteryPercentage) -> None:
        self._BatteryType = BatteryType
        self._BatteryPercentage= BatteryPercentage
        print(f"show level of batterycentage{BatteryPercentage}")

    def Charging(self):
        print("charging capability") 

    def Timer(self, minutes):
        self._minutes = minutes
        print("Timer for charging")

    def turnOn(self):
        print("turn on robot")

    def turnOff(self):
        print("turn off the robot")

"""
Wi-Fi signals the Computer system
"""
class WiFi:
    def __init__(self, Command, SignalType) -> None:
        self._Command = Command
        self._SignalType = SignalType

    def sendAlert(self):
        print("sends an alert to the computer system if Wi-Fi is not activated")

    def makeVisibile(self):
        print("make connection visible to the public")

    def turnOn(self):
        print("turn Wifi on")

    def turnOff(self):
        print("turn WiFi off")    

"""
Computer System Manages the Driving System
""" 
class DrivingSystem:
    def __init__(self, motorType) -> None:
        self._motorType = motorType
        self._speed = 3

    def start(self):
        print("start the motor")

    def stop(self):
        print("stop the motor")

    def setMaxSpeed(self, miles):
        self._speed = miles
        print("set maximum speed of robot")

"""
The Driving System operates the Middle wheels and the side wheels
"""
class MiddleWheel:
    def __init__(self, size, position) -> None:
        self._size = size
        self._position = position

    def spin(self, degrees):
        print("middle wheel spins to change directions")
        self._degrees = degrees

class SideWheels:
    def __init__(self, size, position) -> None:
        self._size = size
        self._position = position

    def MoveForward(self):
        print("wheels can go forward")

    def MoveBackwards(self):
        print("wheels can go back")

"""
The Cameras alert the driving system
"""
class Cameras:
    def __init__(self, DirectionFacing) -> None:
        self._DirectionFacing = DirectionFacing
        print("the camera could be pointing up or down")

    def readBarcode(self):
        print("read the barcodes on the floor and on the pods")

    def detectMotion(self):
        print("cameras can detect motion")

    def sendAlert(self):
        print("alert computer system if motion detected")

"""
Night Vision is a subclass of Cameras
"""
class NightVision(Cameras):
    def __init__(self,DirectionFacing) -> None:
        super().__init__(DirectionFacing)

    def turnOn(self):
        print("turn on Night Vision when it is dark")

    def turnOff(self):
        print("turn off night vision when it is day")

    def visibility(self, level):
        self._level = level
        print("level of visibility")

"""
The Bumpers alert the computer system
"""
class Bumper:
    def __init__(self, sensors, position) -> None:
        self._sensors = sensors
        self._position = position

    def stop(self):
        print("alert computer to stop robot")

    def collionDetection(self):
        print("touch sensors to detect collision")

