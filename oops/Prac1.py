class Cars:
    total_car = 0  # Class variable to count total cars

    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model  # Public attribute
        Cars.total_car += 1  # Increment total car count

    def get_brand(self):
        return self.__brand  # Return the private brand attribute , incapsulation 

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    #polymorphism
    def fualtype(self):
        return "petrol or deasel"
    
    @staticmethod
    def general():
        return "Cars are means of transport"


# class ElectricCars(Cars):
#     def __init__(self, brand, model, battery):
#         super().__init__(brand, model)  # Call parent constructor
#         self.battery = battery  # Battery attribute
        
#     def fualtype(self):
#         return "electric"
    

# # Example usage:
# car1 = Cars("Toyota", "Corolla")
# print(car1.full_name())  # Output: Toyota Corolla
# print(Cars.total_car)    # Output: 1

# electric_car = ElectricCars("Tesla", "Model S", "100 kWh")
# print(electric_car.full_name())  # Output: Tesla Model S
# print(electric_car.battery)      # Output: 100 kWh
# print(Cars.total_car)            # Output: 2
# print(car1.general()) 
# print(Cars.general())

# #isinstance check 
# print(isinstance(electric_car,ElectricCars))
# print(isinstance(electric_car,Cars))                        

#multiple Inheritance 
class Battery:
    def battery_into(self):
        return "This has battery"

class engine:
    def enigne_info(self):
        return "no engine" 

class ElectricCarTwo(Battery,engine,Cars):
    pass 

my_new_tesla = ElectricCarTwo("Hummer","HV")
print(my_new_tesla.enigne_info())
print(my_new_tesla.battery_into())