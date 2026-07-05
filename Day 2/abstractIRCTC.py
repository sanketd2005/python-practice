from abc import ABC,abstractmethod

class IRCTC(ABC):
    @abstractmethod
    def bookTicket(self):
        pass

# class PayTM(IRCTC):
#     def bookTicket(self):
#         print('-'*20)
#         print("Booking done via Paytm")
#         print('-'*20)

# class whereIsMyTrain(IRCTC):
#     def bookTicket(self):
#         print('*'*20)
#         print("Booking done via whereIsMyTrain")
#         print('*'*20)

# class PhonePe(IRCTC):
#     def bookTicket(self):
#         print("Booking done via PhonePe")

class MakeMyTrip(IRCTC):
    def bookTicket(self):
        print('='*30)
        print("Booking via MakeMyTrip")
        print('='*30)
        self.name = input("Enter Name : ")
        self.arrival = input("Enter Arrival : ")
        self.destination = input("Enter Destination : ")
        print('-'*30)
        print(f'Ticket Booked From :{self.arrival} to {self.destination} ')
        print('-'*30)
    
class Goibibo(IRCTC):
    def bookTicket(self):
        print('*'*30)
        print("Booking via Goibibo")
        print('*'*30)
        self.name = input("Enter Name : ")
        self.arrival = input("Enter Arrival : ")
        self.destination = input("Enter Destination : ")
        print('^'*30)
        print(f'Ticket Confirmed From :{self.arrival} to {self.destination} ')
        print('^'*30)
    
m = MakeMyTrip()
m.bookTicket()

g = Goibibo()
g.bookTicket()