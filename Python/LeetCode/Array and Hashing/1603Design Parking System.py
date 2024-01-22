class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park = {
            1:big,
            2:medium,
            3:small
        }

    def addCar(self, carType: int) -> bool:
        if self.park[carType]>0:
            self.park[carType]-=1
            return True
        else: return False