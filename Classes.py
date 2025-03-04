
# Classes Notes
class Vehicle():
    def __init__(self , vehicle_type):
        self.vehicle_type = vehicle_type




class Car(Vehicle):
    def __init__(self, engine_type , modal):  
        super().__init__('Car')
        self.colur = 'red'
        self.modal = modal

    
class MoterBike(Vehicle):
    def __init__(self, engine_type , modal , color, condition):
        super().__init__('MoterBike')
        self.color = color
        self.condition = condition
        self.modal = modal
    
    def bike_condition(self):
        if self.condition >= 7:
            return 'Good Condition'
        else:
            return 'Bad Condition'

    def bike_modal(self):
        if self.modal <= 2010:
            return 'Old Modal'
        else:
            return 'New Modal'



vehilce_type = input('what is the type of your Vehicle Car / MoterBike (c/m): ').lower()

modal_number = int(input('What is the modal of your: '))
vehilce_color = input('What is the color: ')
vehilce_con = int(input('What is the condition out of 10 : '))
car = Car('car' , modal_number)

MoterBike = MoterBike(vehilce_type , modal_number , vehilce_color , vehilce_con)

if vehilce_type == 'c':
    print (car.modal)
elif vehilce_type == 'm':
    # MoterBike. = modal_number
    # MoterBike.color = vehilce_color
    # MoterBike.condition = vehilce_condition
    condition_status = MoterBike.bike_condition()
    print(condition_status)




