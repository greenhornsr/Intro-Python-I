# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self,lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f"lat: {self.lat}, lat: {self.lon}"


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
    def __str__(self):
        return f'"Location: {self.name}", Lat: {self.lat}, Lon: {self.lon}'

# Instance of Waypoint Class which inherits(lat, lon attributes) from LatLon
location2 = Waypoint("Seattle, WA", 47.6062,122.3321)
# Print by calling each attribute
print(location2.name, location2.lat, location2.lon)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)
    # The below __str__ or __repr__ is done so the terminal print is more human readable.
    def __str__(self):
        return f'"Location: {self.name}", Difficulty: {self.difficulty}, Size: {self.size}, Lat: {self.lat}, Lon: {self.lon}'

location3 = Geocache("Denver, CO", "TOUGH", "MASSIVE", 39.7392, 104.9903)
print(f"name: {location3.name}, difficulty: {location3.difficulty}, size: {location3.size}, lat: {location3.lat}, lon: {location3.lon}")

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(f'location: "{waypoint.name}", lat: {41.70505}, lon: {-121.51521}')

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
