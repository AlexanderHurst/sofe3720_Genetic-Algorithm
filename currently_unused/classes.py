# CLASS: Salesman <-- dont think i need or use this..
class Salesman:
    destination_cities = []

    # to trip add a city
    def add_city(self, city):
        self.destination_cities.append(city)

    # return the route
    def get_salesman_route(self, index):
        return self.destination_cities[index]

    # get the number of cities on route
    def get_number_of_cities(self):
        return len(self.destination_cities)    
