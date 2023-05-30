from typing import List
import math


class Container:
    def __init__(self, ID: int, Weight: float):
        self.ID = ID
        self.Weight = Weight

    def __str__(self):
        return f'ID = {self.ID} , Weight = {self.Weight}'

    def consumption(Value):
        global Rate
        ConsumptionValues = {RefrigeratedContainer: 5.0, LiquidContainer: 4.0, HeavyContainer: 3.00,
                             NormalContainer: 2.50}
        for i in ConsumptionValues.keys():
            if isinstance(Value,i):
                Rate = ConsumptionValues[i]
                break
        return Value.Weight * Rate

    def equals(self,other):
        if self.ID == other.ID and self.Weight == other.Weight and self.__eq__(other):
            return True
        else:
            return False


class NormalContainer(Container):
    def __init__(self, ID: int, Weight: float):
        super().__init__(ID, Weight)


class HeavyContainer(Container):
    def __init__(self, ID: int, Weight: float):
        super().__init__(ID, Weight)


class RefrigeratedContainer(HeavyContainer):
    def __init__(self, ID: int, Weight: float):
        super().__init__(ID, Weight)


class LiquidContainer(HeavyContainer):
    def __init__(self, ID: int, Weight: float):
        super().__init__(ID, Weight)


class Station:
    def __init__(self, ID: int, X: float, Y: float):
        self.ID = ID
        self.X = X
        self.Y = Y
        self.containers = []
        self.history = []
        self.current = []

    def __str__(self):
        return f'ID = {self.ID}, X = {self.X}, Y = {self.Y}'

    def Getcontainers(self):
        return self.containers

    def AddContainers(self,container):
        self.containers.append(container)

    def RemoveContainers(self,container):
        self.containers.remove(container)

    def Gethistory(self):
        return self.history

    def AddHistory(self,car):
        self.history.append(car)

    def RemoveHistory(self,car):
        self.history.remove(car)

    def RemoveCurrent(self,car):
        self.current.remove(car)

    def Getcurrent(self):
        return self.current

    def Addcurrent(self,car):
        self.current.append(car)

    def getDistance(self, other):
        distance = math.sqrt(((self.X - other.X) ** 2) + ((self.Y - other.Y) ** 2))
        return round(distance, 2)


class FreightCar:
    def __init__(self, ID: int, station: int, totalWeightCapacity: int,
                 maxNumberOfAllContainers: int,maxNumberOfHeavyContainers: int, maxNumberOfRefrigeratedContainers: int,
                 maxNumberOfLiquidContainers: int, fuelConsumptionPerKM: float):
        self.ID = ID
        self.station = station
        self.totalWeightCapacity = totalWeightCapacity
        self.maxNumberOfAllContainers = maxNumberOfAllContainers
        self.maxNumberOfHeavyContainers = maxNumberOfHeavyContainers
        self.maxNumberOfRefrigeratedContainers = maxNumberOfRefrigeratedContainers
        self.maxNumberOfLiquidContainers = maxNumberOfLiquidContainers
        self.fuelConsumptionPerKM = fuelConsumptionPerKM
        self.FrieghtCarContainers: List[Container] = []
        self.FuelAmount = 0

    def __str__(self):
        return f'ID = {self.ID}, station = {self.station}, ' \
               f'totalWeightCapacity = {self.totalWeightCapacity}, ' \
               f'maxNumberOfAllContainers = {self.maxNumberOfAllContainers}, maxNumberOfHeavyContainers = {self.maxNumberOfHeavyContainers}, ' \
               f'maxNumberOfRefrigeratedContainers = {self.maxNumberOfRefrigeratedContainers}, ' \
               f'maxNumberOfLiquidContainers = {self.maxNumberOfLiquidContainers}, fuelConsumptionPerKM = {self.fuelConsumptionPerKM}, ' \
               f'FrieghtCarContainers = {self.FrieghtCarContainers}, FuelAmount = {self.FuelAmount}'

    def SetFuel(self, amount):
        self.FuelAmount = amount

    def FuelTank(self):
        return self.FuelAmount

    def AddFuel(self, amount):
        self.FuelAmount += amount

    def RemoveFuel(self,Amount):
        self.FuelAmount -= Amount

    def Setstation(self, num):
        self.station = num

    def GetStation(self):
        return self.station

    def getCurrentContainers(self):
        return self.FrieghtCarContainers

    def AddContainer(self,container):
        self.FrieghtCarContainers.append(container)

    def RemoveContainer(self,container):
        self.FrieghtCarContainers.remove(container)

    def GetFuelConsumptionPerKm(self):
        return self.fuelConsumptionPerKM





ContainerID = 0
FreightCarID = 0
StationID = 0
CONTAINERS = dict()
CARS = dict()
STATIONS = dict()

class Main:
    def Creating_Container(self,user_input):
        weight = float(user_input[2])
        global CONTAINERS
        global ContainerID
        global STATIONS

        ContainerID += 1

        if weight < 3000:
            New_Container = NormalContainer(ContainerID, weight)
        else:
            container_type = user_input[3] if len(user_input) == 4 else ""
            if container_type == "R":
                New_Container = RefrigeratedContainer(ContainerID, weight)
            elif container_type == "L":
                New_Container = LiquidContainer(ContainerID, weight)
            else:
                New_Container = HeavyContainer(ContainerID, weight)

        CONTAINERS[ContainerID] = New_Container
        stationID = int(user_input[1])
        StoringStation = STATIONS[stationID]
        StoringStation.AddContainers(New_Container)

    def Create_Car(self, user_input):
        global FreightCarID
        global CARS

        FreightCarID += 1
        args = [int(x) if x.isdigit() else float(x) for x in user_input[1:]]
        stationID = int(user_input[1])
        New_Car = FreightCar(FreightCarID, *args)
        CARS[FreightCarID] = New_Car
        StationCar = STATIONS[int(stationID)]
        StationCar.Addcurrent(New_Car)
        StationCar.AddHistory(New_Car)




    def Create_Station(self, user_input):
        global StationID
        global STATIONS
        StationID += 1
        args = [float(x) for x in user_input[1:]]
        New_Station = Station(StationID, *args)
        STATIONS[StationID] = New_Station


    def Loading_Container(self,user_input):
        global CARS
        global CONTAINERS
        car = CARS[int(user_input[1])]
        container = CONTAINERS[int(user_input[2])]
        car.AddContainer(container)


    def Remove_Container(self, user_input):
        global CARS
        global CONTAINERS
        car = CARS[int(user_input[1])]
        container = CONTAINERS[int(user_input[2])]
        car.RemoveContainer(container)

    def Car_travelling(self,user_input):
        car = CARS[int(user_input[1])]
        FuelAvailable = car.FuelTank()
        CarContainers = car.getCurrentContainers()
        CurrentStationID = car.GetStation()
        CurrentStation = STATIONS[CurrentStationID]
        NewStationID = user_input[2]
        NewStation = STATIONS[int(NewStationID)]
        distance = CurrentStation.getDistance(NewStation)

        fuel_consumption = car.GetFuelConsumptionPerKm()
        total_fuel_consumption = fuel_consumption

        for i in CarContainers:
            total_fuel_consumption += Container.consumption(i)

        FuelNeeded = total_fuel_consumption * distance

        if FuelNeeded < FuelAvailable:
            car.RemoveFuel(FuelNeeded)
            for Cont in CarContainers:
                CurrentStation.RemoveContainers(Cont)
                NewStation.AddContainers(Cont)

            car.Setstation(NewStationID)
            CurrentStation.current.remove(car)
            NewStation.current.append(car)
            NewStation.history.append(car)
        else:
            print("Not enough fuel, please add more fuel")

    def addFuel(self,user_input):
        car = CARS[int(user_input[1])]
        car.AddFuel(float(user_input[2]))


objectt = Main()
while True:
    user_input = input("Input a command:\n").lower().split(" ")
    if user_input[0] == "exit":
        break

    elif user_input[0] == "1":
        objectt.Creating_Container(user_input)

    elif user_input[0] == "2":
        objectt.Create_Car(user_input)

    elif user_input[0] == "3":
        objectt.Create_Station(user_input)

    elif user_input[0] == "4":
        objectt.Loading_Container(user_input)

    elif user_input[0] == "5":
        objectt.Remove_Container(user_input)

    elif user_input[0] == "6":
        objectt.Car_travelling(user_input)

    elif user_input[0] == "7":
        objectt.addFuel(user_input)

    else:
        print("Unknown command try again")

# TEST CASES------------------------------------------------------------------------------------------------------------
print("Test case 1 Creating containers")
# Stations had to be created before the containers so the containers can be placed in the stations
test_input9 = ["3","14","1.21"]
test_input10 = ["3","23.78","7.48"]
test_input11 = ["3","1.78","6.35"]
test_input12 = ["3","7.25","9.36"]
objectt.Create_Station(test_input9)
objectt.Create_Station(test_input10)
objectt.Create_Station(test_input11)
objectt.Create_Station(test_input12)
print("------------------------------------------------------------------")
test_input1 = ["1","1","500"]
test_input2 = ["1","1","3500"]
test_input3 = ["1","2","4000", "L"]
test_input4 = ["1","2","5500","R"]
objectt.Creating_Container(test_input1)
objectt.Creating_Container(test_input2)
objectt.Creating_Container(test_input3)
objectt.Creating_Container(test_input4)
print(CONTAINERS)
for i in CONTAINERS.values():
    print(i)
for i in STATIONS.values():
    print(i.Getcontainers())
print("------------------------------------------------------------------")
print("Test case 2 Creating freight cars")
print("------------------------------------------------------------------")
test_input5 = ["2","1","60000","44","8","65","19","2"]
test_input6 = ["2","1","75000","15","8","75","27","16"]
test_input7 = ["2","2","25000","30","8","5","14","35"]
test_input8 = ["2","3","15000","7","7","1","7","5"]
objectt.Create_Car(test_input5)
objectt.Create_Car(test_input6)
objectt.Create_Car(test_input7)
objectt.Create_Car(test_input8)
print(CARS)
for i in CARS.values():
    i.AddFuel(500)
    print(i)
print("------------------------------------------------------------------")
print("Test case 3 Creating stations")
print(STATIONS)
for i in STATIONS.values():
    print(i)
print("------------------------------------------------------------------")
print("Test case 4 Loading containers")
test_input13 = ["4","1","1"]
test_input14 = ["4","1","2"]
test_input15 = ["4","3","3"]
test_input16 = ["4","3","4"]
objectt.Loading_Container(test_input13)
objectt.Loading_Container(test_input14)
objectt.Loading_Container(test_input15)
objectt.Loading_Container(test_input16)
for i in CARS.values():
    print(i.getCurrentContainers())
print("------------------------------------------------------------------")
print("Test case 5 Unloading Containers")
test_input17 = ["5","1","1"]
test_input18 = ["5","1","2"]
test_input19 = ["5","3","3"]
test_input20 = ["5","3","4"]
objectt.Remove_Container(test_input17)
objectt.Remove_Container(test_input18)
objectt.Remove_Container(test_input19)
objectt.Remove_Container(test_input20)
for i in CARS.values():
    print(i.getCurrentContainers())
print("------------------------------------------------------------------")
print("Test case 6 Car travelling")
test_input21 = ["6","1","2"]
test_input22 = ["6","2","4"]
objectt.Car_travelling(test_input21)
objectt.Car_travelling(test_input22)
for i in CARS.values():
    print(i.GetStation())
for i in STATIONS.values():
    print(i.Gethistory())
print("==================")
for i in STATIONS.values():
    print(i.Getcurrent())

for i in CARS.values():
    print(round(i.FuelTank(),2))

print("------------------------------------------------------------------")
print("Test Case 7 Adding Fuel")
test_input23 = ["7","1","600.178"]
test_input24 = ["7","2","300.287"]
test_input25 = ["7","3","50.35"]
objectt.addFuel(test_input23)
objectt.addFuel(test_input24)
objectt.addFuel(test_input25)
for i in CARS.values():
    print(round(i.FuelTank(),2))