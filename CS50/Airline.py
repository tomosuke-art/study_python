# オブジェクト指向プログラミング 
# 航空便をあらわすクラス
class Flight():
    # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add a passenger to the flight:
    def add_passenger(self, name):
      # 空席があるかどうかの判断
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    # Method to return nimber of seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
# Create a new flight with o=up to 3 passengers
flight = Flight(3)

# Create a list of people
people = ["Harry", "Ron", "Hermione", "Ginny"]

# Attempt to add each person in the list to a flight
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")

# output(出力)↓
# Added Harry to flight successfully
# Added Ron to flight successfully
# Added Hermione to flight successfully
# No available seats for Ginny