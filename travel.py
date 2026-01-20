class Travel:
    def __init__(self, country, travel_month, travel_type):
        self.country = country
        self.travel_month = travel_month
        self.travel_type = travel_type
        self.flight_cost = 0

    def trip_info(self):
        if self.travel_month in ['oct', 'nov', 'dec', 'jan', 'feb', 'mar']:
            print("winter trip!")
        elif self.travel_month in ['apr', 'may', 'jun', 'jul', 'aug', 'sep']:
            print("summer trip!")
        else:
            print("invalid month")
        print(self.country)
        print(self.travel_type)

    def calc_cost(self, flight_cost):
        additional_cost = int(input("enter any additional cost: "))
        #print(f"{str(self.flight_cost + additional_cost)}")
        msg = self.advice(self.flight_cost+additional_cost)
        print(msg)

    def advice(self, cost):
        if cost < 500:
            msg = "great price"
        else:
            msg = "expensive"

        return msg

trip1 = Travel('spain','dec', 'leisure')
trip1.trip_info()
trip1.calc_cost(250)

