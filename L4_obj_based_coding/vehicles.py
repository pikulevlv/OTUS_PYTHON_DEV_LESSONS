class BaseVehicle:
    SOUND = ''

class Car(BaseVehicle):
    SOUND = 'beep'
    WHEELS = 4
    # FUEL_CONSUMPTION = 100 #единиц на единицу расстояния
    MAX_FUEL = 10_000

    def __init__(self, fuel=5000, fuel_consumption=100):
        self.__fuel = fuel
        self._fuel_consumption = fuel_consumption

    @property # позволяет обратиться к методу в экземпляре класса без скобок в конце
    def fuel(self):
        return self.__fuel

    def go(self, distance):
        fuel_to_spend = distance * self._fuel_consumption
        if fuel_to_spend > self.fuel:
            print(f"Cannot go, not enough fuel {self.fuel}, need {fuel_to_spend}")
            return
        self.__fuel -= fuel_to_spend # name mandling __smth
        print(f"Going {distance}, spent {fuel_to_spend}, left {self.fuel}")

    def add_fuel(self, value):
        print("Adding", value, 'of fuel')
        self.__fuel += value
        if self.__fuel > self.MAX_FUEL:
            print(f"lost {self.__fuel - self.MAX_FUEL} of fuel")
            self.__fuel = self.MAX_FUEL
        return self.__fuel

class Truck(Car):
    WHEELS = 6
    MAX_FUEL = 20_000

    def __init__(self, *args, luggage, **kwargs): # вот так переопределяем метод инит и добавляем новый аттрибут
        super().__init__(*args, **kwargs)
        self.luggage = luggage

    # def add_fuel(self, value):
    #     res = super().add_fuel(value)
    #     print("max distance now", res//self._fuel_consumption)
    #     print("but drops 100")
    #     self._Car__fuel -= 100
    #     return self._Car__fuel

    def add_fuel(self, value):
        res = super().add_fuel(value)
        return res


c = Car()
print("Car c consumption", c._fuel_consumption)
# c._fuel_consumption -= 50
c.go(20)
c.go(20)
print(c.fuel)
print("Adding fuel. Now:", c.add_fuel(2000))
# c.__fuel += 1000
# c._Car__fuel += 1000
c.go(20)
print("Adding fuel. Now:", c.add_fuel(20_000))

print('*'*30)

t = Truck(fuel_consumption=200, luggage=object())
t.add_fuel(5000)
t.go(30)
print("Adding fuel. Now:", t.add_fuel(20_000))
print(Truck.__mro__) # список наследования