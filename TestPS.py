from address import Address
from booking.booking_for_display import BookingForDisplay
from parking_manager import ParkingManager

"""
1 - register a user
2 - book a parking spot
3 - park a car
4 - exit a parking spot
5 - show all parking garages
6 - show my bookings
7 - show all users
8 - exit

"""

b = BookingForDisplay("Garage 1", "LAE 170", "11/26/24 11:00AM", "11/26/24 2:00PM", "Booked", 1)
print(b)

my_list = list()
my_list.append('A')
my_list.append('B')
my_list.append('C')
my_list.append('D')
my_list.append('E')

l = filter(lambda v: v == 'C', my_list)
print(list(l)[0])

print(list(filter(lambda v: v == 'B', my_list))[0])





cmd = 0
pm = ParkingManager()

while cmd != 8:
    print("1 - register a user")
    print("2 - book a parking spot")
    print("3 - park a car")
    print("4 - exit a parking spot")
    print("5 - show all parking garages")
    print("6 - show my bookings")
    print("7 - Show all users")
    print("8 - exit")
    cmd = int(input("Enter a command: "))

    if cmd == 1:
        a = Address("2311 York Road", "Timonium", "MD", "21030")
        registered = pm.register_customer("first", "last", "abc.1@test.com", a)
        if registered:
            print("Customer registered")
        else:
            print("Customer not registered")
    elif cmd == 2:
        booked = pm.book("PG1", "CS3", "11/10/2024 10:00", "11/10/2024 12:00")
        if booked:
            print("Parking spot booked")
        else:
            print("Parking spot not booked")
    elif cmd == 3:
        pm.park("BK5")
    elif cmd == 4:
       pm.exit("BK5")
    elif cmd == 5:
       for g in pm.get_parking_garages():
           print(g)
    elif cmd == 6:
        for b in pm.get_bookings_by_customer("CS3"):
            print(b)
    elif cmd == 7:
        for u in pm.get_all_customers():
            print(u)
    elif cmd == 8:
        print("Exit")
    else:
        print("Invalid command")