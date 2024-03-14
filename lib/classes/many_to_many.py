class NationalPark:

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self ,name):
        if not isinstance(name , str) or not len(name) >= 3:
            raise Exception("Invalid input")
        if hasattr(self, "_name"):
            raise Exception("Name cannot be changed")
        self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set(trip.visitor for trip in self.trips()))
    
    def total_visits(self):
        count = 0
        for trip in self.trips():
            if trip.national_park == self:
                count += 1
        return count if count > 0 else None

    
    def best_visitor(self):
        best_visitor = None
        max_visits = 0

        for visitor in self.visitors():
            visit_count = sum(1 for trip in self.trips() if trip.visitor == visitor)
            if visit_count > max_visits:
                max_visits = visit_count
                best_visitor = visitor
        
        return best_visitor

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if not isinstance(start_date, str) or not len(start_date) >= 7:
            raise Exception("Invalid input")
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if not isinstance(end_date, str) or not len(end_date) >= 7:
            raise Exception("Invalid input")
        self._end_date = end_date

    def visitor(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_park(self):
        return [trip for trip in Trip.all if trip.national_park == self]

class Visitor:

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not 1 <= len(name) <= 15:
            raise Exception("Invalid input")
        self._name = name 

    def trips(self):
        # list of all trips
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set(trip.national_park for trip in self.trips()))
    
    def total_visits_at_park(self, park):
        count = 0

        for trip in self.trips():
            if trip.park == park:
                count += 1

        return count if count > 0 else None